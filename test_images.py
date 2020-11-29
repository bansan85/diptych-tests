import unittest

import numpy as np

from script import treat_file, get_absolute_from_current_path
from print_interface import ConstString
from tests.mock_separate_page import MockDisableSeparatePage
import cv2ext

np.seterr(all="raise")
tc = unittest.TestCase()


MAX_VAL = 6


def test_0001_png() -> None:
    """first good page"""
    treat_file(
        MockDisableSeparatePage(MAX_VAL),
        get_absolute_from_current_path(__file__, "0001.png"),
        {
            ConstString.separation_double_page_angle(): (
                "range",
                90.46,
                90.63,
            ),
            ConstString.separation_double_page_y(): ("range", 2481, 2489),
            ConstString.page_rotation(1): ("range", 0.65, 0.76),
            ConstString.page_rotation(2): ("range", 0.14, 0.21),
            ConstString.image_crop(1, "x1"): ("range", 330, 332),
            ConstString.image_crop(1, "y1"): ("range", 335, 337),
            ConstString.image_crop(1, "x2"): ("range", 2342, 2343),
            ConstString.image_crop(1, "y2"): ("range", 3222, 3223),
            ConstString.image_crop(2, "x1"): ("range", 168, 175),
            ConstString.image_crop(2, "y1"): ("range", 648, 649),
            ConstString.image_crop(2, "x2"): ("range", 2180, 2189),
            ConstString.image_crop(2, "y2"): ("range", 3360, 3361),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 324, 340),
            ConstString.image_border(1, 2): ("range", 260, 276),
            ConstString.image_border(1, 3): ("range", 223, 225),
            ConstString.image_border(1, 4): ("range", 223, 225),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 646, 674),
            ConstString.image_border(2, 2): ("range", 101, 128),
            ConstString.image_border(2, 3): ("range", 221, 224),
            ConstString.image_border(2, 4): ("range", 221, 224),
        },
    )


def test_2_pages_2_contours_png() -> None:
    """There is not one contour for the two pages,
    but one contour for each page.
    """
    treat_file(
        MockDisableSeparatePage(MAX_VAL),
        get_absolute_from_current_path(__file__, "2-pages-2-contours.png"),
        {
            ConstString.separation_double_page_angle(): (
                "range",
                89.92,
                90.32,
            ),
            ConstString.separation_double_page_y(): ("range", 2486, 2492),
            ConstString.page_rotation(1): ("range", -0.01, 0.11),
            ConstString.page_rotation(2): ("range", 0.19, 0.41),
            ConstString.image_crop(1, "x1"): ("range", 1181, 1191),
            ConstString.image_crop(1, "y1"): ("range", 1719, 1733),
            ConstString.image_crop(1, "x2"): ("range", 1182, 1192),
            ConstString.image_crop(1, "y2"): ("range", 1720, 1734),
            ConstString.image_crop(2, "x1"): ("range", 89, 114),
            ConstString.image_crop(2, "y1"): ("range", 240, 241),
            ConstString.image_crop(2, "x2"): ("range", 2136, 2159),
            ConstString.image_crop(2, "y2"): ("range", 3239, 3240),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 1752, 1753),
            ConstString.image_border(1, 2): ("range", 1753, 1753),
            ConstString.image_border(1, 3): ("range", 1239, 1239),
            ConstString.image_border(1, 4): ("range", 1239, 1239),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 226, 240),
            ConstString.image_border(2, 2): ("range", 248, 262),
            ConstString.image_border(2, 3): ("range", 206, 207),
            ConstString.image_border(2, 4): ("range", 206, 207),
        },
    )


def test_black_border_not_removed_png() -> None:
    """The border on the right is still there."""
    treat_file(
        MockDisableSeparatePage(MAX_VAL),
        get_absolute_from_current_path(
            __file__, "black-border-not-removed.png"
        ),
        {
            ConstString.separation_double_page_angle(): (
                "range",
                89.95,
                90.1,
            ),
            ConstString.separation_double_page_y(): ("range", 2451, 2458),
            ConstString.page_rotation(1): ("range", -0.01, 0.06),
            ConstString.page_rotation(2): ("range", -0.21, 0.01),
            ConstString.image_crop(1, "x1"): ("range", 297, 299),
            ConstString.image_crop(1, "y1"): ("range", 142, 144),
            ConstString.image_crop(1, "x2"): ("range", 2307, 2309),
            ConstString.image_crop(1, "y2"): ("range", 3346, 3347),
            ConstString.image_crop(2, "x1"): ("range", 156, 159),
            ConstString.image_crop(2, "y1"): ("range", 144, 146),
            ConstString.image_crop(2, "x2"): ("range", 2168, 2172),
            ConstString.image_crop(2, "y2"): ("range", 3351, 3353),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 127, 130),
            ConstString.image_border(1, 2): ("range", 154, 157),
            ConstString.image_border(1, 3): ("range", 224, 226),
            ConstString.image_border(1, 4): ("range", 224, 226),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 130, 139),
            ConstString.image_border(2, 2): ("range", 141, 151),
            ConstString.image_border(2, 3): ("range", 223, 224),
            ConstString.image_border(2, 4): ("range", 223, 224),
        },
    )


def test_image_failed_to_rotate_png() -> None:
    """Failed to compute angle to rotate. The image takes the whole page."""
    treat_file(
        MockDisableSeparatePage(MAX_VAL),
        get_absolute_from_current_path(__file__, "image_failed_to_rotate.png"),
        {
            ConstString.separation_double_page_angle(): (
                "range",
                90.07,
                90.50,
            ),
            ConstString.separation_double_page_y(): ("range", 2476, 2487),
            ConstString.page_rotation(1): ("range", 0.29, 0.41),
            ConstString.page_rotation(2): ("range", 0.34, 0.51),
            ConstString.image_crop(1, "x1"): ("range", 33, 91),
            ConstString.image_crop(1, "y1"): ("range", 1, 23),
            ConstString.image_crop(1, "x2"): ("range", 2456, 2482),
            ConstString.image_crop(1, "y2"): ("range", 3483, 3501),
            ConstString.image_crop(2, "x1"): ("range", 166, 183),
            ConstString.image_crop(2, "y1"): ("range", 234, 236),
            ConstString.image_crop(2, "x2"): ("range", 2245, 2261),
            ConstString.image_crop(2, "y2"): ("range", 3354, 3356),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 4, 19),
            ConstString.image_border(1, 2): ("range", 4, 19),
            ConstString.image_border(1, 3): ("range", 16, 55),
            ConstString.image_border(1, 4): ("range", 16, 55),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 206, 228),
            ConstString.image_border(2, 2): ("range", 140, 160),
            ConstString.image_border(2, 3): ("range", 189, 192),
            ConstString.image_border(2, 4): ("range", 189, 192),
        },
    )


def test_image_failed_to_crop_data_png() -> None:
    """Failed to detect edges. The image takes the whole page and is too closed
    to the border of the image.
    """
    treat_file(
        MockDisableSeparatePage(MAX_VAL),
        get_absolute_from_current_path(
            __file__, "image_failed_to_crop_data.png"
        ),
        {
            ConstString.separation_double_page_angle(): (
                "range",
                89.89,
                90.17,
            ),
            ConstString.separation_double_page_y(): ("range", 2477, 2486),
            ConstString.page_rotation(1): ("range", -0.16, 0.21),
            ConstString.page_rotation(2): ("range", -0.01, 0.21),
            ConstString.image_crop(1, "x1"): ("range", 43, 116),
            ConstString.image_crop(1, "y1"): ("range", 3, 13),
            ConstString.image_crop(1, "x2"): ("range", 2476, 2483),
            ConstString.image_crop(1, "y2"): ("range", 3499, 3505),
            ConstString.image_crop(2, "x1"): ("range", 155, 167),
            ConstString.image_crop(2, "y1"): ("range", 217, 220),
            ConstString.image_crop(2, "x2"): ("range", 2235, 2245),
            ConstString.image_crop(2, "y2"): ("range", 3348, 3350),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 5, 11),
            ConstString.image_border(1, 2): ("range", 5, 11),
            ConstString.image_border(1, 3): ("range", 21, 58),
            ConstString.image_border(1, 4): ("range", 21, 58),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 209, 225),
            ConstString.image_border(2, 2): ("range", 129, 147),
            ConstString.image_border(2, 3): ("range", 189, 192),
            ConstString.image_border(2, 4): ("range", 189, 192),
        },
    )


def test_wrong_angle_split_line_png() -> None:
    """Failed to detect edges. The image takes the whole page and is too closed
    to the border of the image.
    """
    treat_file(
        MockDisableSeparatePage(MAX_VAL),
        get_absolute_from_current_path(__file__, "wrong_angle_split_line.png"),
        {
            ConstString.separation_double_page_angle(): (
                "range",
                90.00,
                90.22,
            ),
            ConstString.separation_double_page_y(): ("range", 2478, 2487),
            ConstString.page_rotation(1): ("range", -0.01, 0.21),
            ConstString.page_rotation(2): ("range", -0.01, 0.21),
            ConstString.image_crop(1, "x1"): ("range", 53, 61),
            ConstString.image_crop(1, "y1"): ("range", 6, 9),
            ConstString.image_crop(1, "x2"): ("range", 2475, 2485),
            ConstString.image_crop(1, "y2"): ("range", 3500, 3505),
            ConstString.image_crop(2, "x1"): ("range", 154, 165),
            ConstString.image_crop(2, "y1"): ("range", 217, 219),
            ConstString.image_crop(2, "x2"): ("range", 2237, 2248),
            ConstString.image_crop(2, "y2"): ("range", 3348, 3350),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 5, 8),
            ConstString.image_border(1, 2): ("range", 5, 8),
            ConstString.image_border(1, 3): ("range", 24, 31),
            ConstString.image_border(1, 4): ("range", 24, 31),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 195, 219),
            ConstString.image_border(2, 2): ("range", 136, 159),
            ConstString.image_border(2, 3): ("range", 188, 192),
            ConstString.image_border(2, 4): ("range", 188, 192),
        },
    )
    tc.assertEqual(
        cv2ext.charge_image(
            get_absolute_from_current_path(
                __file__, "wrong_angle_split_line.png_page_1.png"
            )
        ).shape[2],
        3,
    )


def test_angle_page_lower_split_line_png() -> None:
    """Failed when angle of a page in lower than
    the angle of the split line.
    """
    treat_file(
        MockDisableSeparatePage(MAX_VAL),
        get_absolute_from_current_path(
            __file__, "angle_page_lower_split_line.png"
        ),
        {
            ConstString.separation_double_page_angle(): (
                "range",
                89.71,
                89.75,
            ),
            ConstString.separation_double_page_y(): ("range", 2471, 2473),
            ConstString.page_rotation(1): ("range", -0.46, -0.39),
            ConstString.page_rotation(2): ("range", 0.19, 0.21),
            ConstString.image_crop(1, "x1"): ("range", 244, 245),
            ConstString.image_crop(1, "y1"): ("range", 160, 161),
            ConstString.image_crop(1, "x2"): ("range", 2350, 2351),
            ConstString.image_crop(1, "y2"): ("range", 3364, 3365),
            ConstString.image_crop(2, "x1"): ("range", 151, 153),
            ConstString.image_crop(2, "y1"): ("range", 147, 147),
            ConstString.image_crop(2, "x2"): ("range", 2258, 2260),
            ConstString.image_crop(2, "y2"): ("range", 3350, 3350),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 130, 132),
            ConstString.image_border(1, 2): ("range", 151, 152),
            ConstString.image_border(1, 3): ("range", 177, 177),
            ConstString.image_border(1, 4): ("range", 177, 177),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 116, 118),
            ConstString.image_border(2, 2): ("range", 166, 168),
            ConstString.image_border(2, 3): ("range", 176, 176),
            ConstString.image_border(2, 4): ("range", 176, 176),
        },
    )


def test_wrong_split_line_png() -> None:
    """Improve choice of the split line between different algorithm."""
    treat_file(
        MockDisableSeparatePage(MAX_VAL),
        get_absolute_from_current_path(__file__, "wrong_split_line.png"),
        {
            ConstString.separation_double_page_angle(): (
                "range",
                89.81,
                89.92,
            ),
            ConstString.separation_double_page_y(): ("range", 2463, 2465),
            ConstString.page_rotation(1): ("range", -0.16, -0.04),
            ConstString.page_rotation(2): ("range", 0.49, 0.66),
            ConstString.image_crop(1, "x1"): ("range", 211, 213),
            ConstString.image_crop(1, "y1"): ("range", 156, 157),
            ConstString.image_crop(1, "x2"): ("range", 2323, 2323),
            ConstString.image_crop(1, "y2"): ("range", 3362, 3363),
            ConstString.image_crop(2, "x1"): ("range", 124, 126),
            ConstString.image_crop(2, "y1"): ("range", 165, 167),
            ConstString.image_crop(2, "x2"): ("range", 2236, 2237),
            ConstString.image_crop(2, "y2"): ("range", 3372, 3374),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 115, 180),
            ConstString.image_border(1, 2): ("range", 100, 167),
            ConstString.image_border(1, 3): ("range", 174, 175),
            ConstString.image_border(1, 4): ("range", 174, 175),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 129, 142),
            ConstString.image_border(2, 2): ("range", 139, 152),
            ConstString.image_border(2, 3): ("range", 174, 174),
            ConstString.image_border(2, 4): ("range", 174, 174),
        },
    )


def test_crop_too_much_png() -> None:
    """Reduce distance to ignore black area closed to the edge."""
    treat_file(
        MockDisableSeparatePage(MAX_VAL),
        get_absolute_from_current_path(__file__, "crop_too_much.png"),
        {
            ConstString.separation_double_page_angle(): (
                "range",
                90.12,
                90.47,
            ),
            ConstString.separation_double_page_y(): ("range", 2453, 2463),
            ConstString.page_rotation(1): ("range", -0.01, 0.01),
            ConstString.page_rotation(2): ("range", 0.39, 0.46),
            ConstString.image_crop(1, "x1"): ("range", 303, 303),
            ConstString.image_crop(1, "y1"): ("range", 148, 148),
            ConstString.image_crop(1, "x2"): ("range", 2313, 2313),
            ConstString.image_crop(1, "y2"): ("range", 3351, 3351),
            ConstString.image_crop(2, "x1"): ("range", 165, 180),
            ConstString.image_crop(2, "y1"): ("range", 154, 155),
            ConstString.image_crop(2, "x2"): ("range", 2179, 2191),
            ConstString.image_crop(2, "y2"): ("range", 3359, 3360),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 116, 131),
            ConstString.image_border(1, 2): ("range", 153, 168),
            ConstString.image_border(1, 3): ("range", 225, 225),
            ConstString.image_border(1, 4): ("range", 225, 225),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 95, 139),
            ConstString.image_border(2, 2): ("range", 143, 186),
            ConstString.image_border(2, 3): ("range", 223, 224),
            ConstString.image_border(2, 4): ("range", 223, 224),
        },
    )


def test_crop_too_few_png() -> None:
    """Improve detection of black area to ignored
    and that are closed to the edge.
    """
    treat_file(
        MockDisableSeparatePage(MAX_VAL),
        get_absolute_from_current_path(__file__, "crop_too_few.png"),
        {
            ConstString.separation_double_page_angle(): (
                "range",
                89.22,
                89.49,
            ),
            ConstString.separation_double_page_y(): ("range", 2508, 2511),
            ConstString.page_rotation(1): ("range", -0.76, -0.69),
            ConstString.page_rotation(2): ("range", -0.01, 0.01),
            ConstString.image_crop(1, "x1"): ("range", 264, 265),
            ConstString.image_crop(1, "y1"): ("range", 151, 161),
            ConstString.image_crop(1, "x2"): ("range", 2375, 2376),
            ConstString.image_crop(1, "y2"): ("range", 3356, 3357),
            ConstString.image_crop(2, "x1"): ("range", 138, 141),
            ConstString.image_crop(2, "y1"): ("range", 141, 141),
            ConstString.image_crop(2, "x2"): ("range", 2260, 2263),
            ConstString.image_crop(2, "y2"): ("range", 3345, 3345),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 84, 116),
            ConstString.image_border(1, 2): ("range", 167, 208),
            ConstString.image_border(1, 3): ("range", 174, 175),
            ConstString.image_border(1, 4): ("range", 174, 175),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 130, 140),
            ConstString.image_border(2, 2): ("range", 143, 153),
            ConstString.image_border(2, 3): ("range", 169, 169),
            ConstString.image_border(2, 4): ("range", 169, 169),
        },
    )


def test_crop_too_much_2_png() -> None:
    """Reduce distance to ignore black area closed to the edge."""
    treat_file(
        MockDisableSeparatePage(MAX_VAL),
        get_absolute_from_current_path(__file__, "crop_too_much_2.png"),
        {
            ConstString.separation_double_page_angle(): (
                "range",
                90.11,
                90.24,
            ),
            ConstString.separation_double_page_y(): ("range", 2475, 2482),
            ConstString.page_rotation(1): ("range", 0.19, 0.21),
            ConstString.page_rotation(2): ("range", 0.19, 0.21),
            ConstString.image_crop(1, "x1"): ("range", 332, 332),
            ConstString.image_crop(1, "y1"): ("range", 131, 131),
            ConstString.image_crop(1, "x2"): ("range", 2342, 2342),
            ConstString.image_crop(1, "y2"): ("range", 3336, 3336),
            ConstString.image_crop(2, "x1"): ("range", 164, 169),
            ConstString.image_crop(2, "y1"): ("range", 139, 139),
            ConstString.image_crop(2, "x2"): ("range", 2177, 2182),
            ConstString.image_crop(2, "y2"): ("range", 3345, 3345),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 116, 116),
            ConstString.image_border(1, 2): ("range", 166, 166),
            ConstString.image_border(1, 3): ("range", 225, 225),
            ConstString.image_border(1, 4): ("range", 225, 225),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 133, 133),
            ConstString.image_border(2, 2): ("range", 148, 148),
            ConstString.image_border(2, 3): ("range", 223, 223),
            ConstString.image_border(2, 4): ("range", 223, 223),
        },
    )


def test_wrong_split_line_2_png() -> None:
    """Improve choice of the split line between different algorithm."""
    treat_file(
        MockDisableSeparatePage(MAX_VAL),
        get_absolute_from_current_path(__file__, "wrong_split_line_2.png"),
        {
            ConstString.separation_double_page_angle(): (
                "range",
                90.26,
                90.40,
            ),
            ConstString.separation_double_page_y(): ("range", 2436, 2442),
            ConstString.page_rotation(1): ("range", 0.04, 0.21),
            ConstString.page_rotation(2): ("range", 0.34, 0.41),
            ConstString.image_crop(1, "x1"): ("range", 294, 294),
            ConstString.image_crop(1, "y1"): ("range", 136, 137),
            ConstString.image_crop(1, "x2"): ("range", 2325, 2326),
            ConstString.image_crop(1, "y2"): ("range", 3375, 3376),
            ConstString.image_crop(2, "x1"): ("range", 142, 146),
            ConstString.image_crop(2, "y1"): ("range", 192, 193),
            ConstString.image_crop(2, "x2"): ("range", 2169, 2175),
            ConstString.image_crop(2, "y2"): ("range", 3386, 3387),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 125, 128),
            ConstString.image_border(1, 2): ("range", 119, 124),
            ConstString.image_border(1, 3): ("range", 214, 214),
            ConstString.image_border(1, 4): ("range", 214, 214),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 184, 184),
            ConstString.image_border(2, 2): ("range", 109, 109),
            ConstString.image_border(2, 3): ("range", 215, 216),
            ConstString.image_border(2, 4): ("range", 215, 216),
        },
    )


def test_small_wave_png() -> None:
    """The wave at the bottom of the image is very small."""
    treat_file(
        MockDisableSeparatePage(MAX_VAL),
        get_absolute_from_current_path(__file__, "small_wave.png"),
        {
            ConstString.separation_double_page_angle(): (
                "range",
                90.61,
                90.64,
            ),
            ConstString.separation_double_page_y(): ("range", 2491, 2498),
            ConstString.page_rotation(1): ("range", 0.69, 0.81),
            ConstString.page_rotation(2): ("range", 0.69, 0.81),
            ConstString.image_crop(1, "x1"): ("range", 322, 324),
            ConstString.image_crop(1, "y1"): ("range", 197, 199),
            ConstString.image_crop(1, "x2"): ("range", 2351, 2353),
            ConstString.image_crop(1, "y2"): ("range", 3394, 3395),
            ConstString.image_crop(2, "x1"): ("range", 133, 139),
            ConstString.image_crop(2, "y1"): ("range", 223, 224),
            ConstString.image_crop(2, "x2"): ("range", 2161, 2168),
            ConstString.image_crop(2, "y2"): ("range", 3418, 3419),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 174, 177),
            ConstString.image_border(1, 2): ("range", 115, 115),
            ConstString.image_border(1, 3): ("range", 215, 215),
            ConstString.image_border(1, 4): ("range", 215, 215),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 191, 192),
            ConstString.image_border(2, 2): ("range", 100, 102),
            ConstString.image_border(2, 3): ("range", 215, 216),
            ConstString.image_border(2, 4): ("range", 215, 216),
        },
    )


def test_wrong_split_line_3_png() -> None:
    """The split line was not the right one."""
    treat_file(
        MockDisableSeparatePage(MAX_VAL),
        get_absolute_from_current_path(__file__, "wrong_split_line_3.png"),
        {
            ConstString.separation_double_page_angle(): (
                "range",
                90.44,
                90.45,
            ),
            ConstString.separation_double_page_y(): ("range", 2498, 2498),
            ConstString.page_rotation(1): ("range", 0.29, 0.36),
            ConstString.page_rotation(2): ("range", 0.89, 0.91),
            ConstString.image_crop(1, "x1"): ("range", 331, 331),
            ConstString.image_crop(1, "y1"): ("range", 164, 165),
            ConstString.image_crop(1, "x2"): ("range", 2375, 2375),
            ConstString.image_crop(1, "y2"): ("range", 3376, 3377),
            ConstString.image_crop(2, "x1"): ("range", 102, 103),
            ConstString.image_crop(2, "y1"): ("range", 208, 208),
            ConstString.image_crop(2, "x2"): ("range", 2133, 2134),
            ConstString.image_crop(2, "y2"): ("range", 3413, 3413),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 149, 150),
            ConstString.image_border(1, 2): ("range", 125, 126),
            ConstString.image_border(1, 3): ("range", 208, 208),
            ConstString.image_border(1, 4): ("range", 208, 208),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 190, 190),
            ConstString.image_border(2, 2): ("range", 92, 92),
            ConstString.image_border(2, 3): ("range", 214, 214),
            ConstString.image_border(2, 4): ("range", 214, 214),
        },
    )


def test_wrong_wave_split_line_png() -> None:
    """The split line by wave method was wrong."""
    treat_file(
        MockDisableSeparatePage(MAX_VAL),
        get_absolute_from_current_path(__file__, "wrong_wave_split_line.png"),
        {
            ConstString.separation_double_page_angle(): (
                "range",
                90.53,
                90.54,
            ),
            ConstString.separation_double_page_y(): ("range", 2502, 2502),
            ConstString.page_rotation(1): ("range", -0.16, -0.14),
            ConstString.page_rotation(2): ("range", 0.84, 0.86),
            ConstString.image_crop(1, "x1"): ("range", 385, 385),
            ConstString.image_crop(1, "y1"): ("range", 179, 179),
            ConstString.image_crop(1, "x2"): ("range", 2411, 2411),
            ConstString.image_crop(1, "y2"): ("range", 3374, 3374),
            ConstString.image_crop(2, "x1"): ("range", 124, 124),
            ConstString.image_crop(2, "y1"): ("range", 58, 58),
            ConstString.image_crop(2, "x2"): ("range", 2410, 2410),
            ConstString.image_crop(2, "y2"): ("range", 3392, 3392),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 167, 167),
            ConstString.image_border(1, 2): ("range", 124, 124),
            ConstString.image_border(1, 3): ("range", 217, 217),
            ConstString.image_border(1, 4): ("range", 217, 217),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 0, 0),
            ConstString.image_border(2, 2): ("range", 163, 163),
            ConstString.image_border(2, 3): ("range", 92, 92),
            ConstString.image_border(2, 4): ("range", 92, 92),
        },
    )


def test_no_split_line_line_algo_png() -> None:
    """No line for split line with line detection algo."""
    treat_file(
        MockDisableSeparatePage(MAX_VAL),
        get_absolute_from_current_path(
            __file__, "no_split_line_line_algo.png"
        ),
        {
            ConstString.separation_double_page_angle(): (
                "range",
                89.46,
                89.47,
            ),
            ConstString.separation_double_page_y(): ("range", 2476, 2476),
            ConstString.page_rotation(1): ("range", -0.16, -0.14),
            ConstString.page_rotation(2): ("range", -0.46, -0.44),
            ConstString.image_crop(1, "x1"): ("range", 205, 205),
            ConstString.image_crop(1, "y1"): ("range", 158, 158),
            ConstString.image_crop(1, "x2"): ("range", 2320, 2320),
            ConstString.image_crop(1, "y2"): ("range", 3366, 3366),
            ConstString.image_crop(2, "x1"): ("range", 185, 185),
            ConstString.image_crop(2, "y1"): ("range", 221, 221),
            ConstString.image_crop(2, "x2"): ("range", 2201, 2201),
            ConstString.image_crop(2, "y2"): ("range", 3366, 3366),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 137, 137),
            ConstString.image_border(1, 2): ("range", 142, 142),
            ConstString.image_border(1, 3): ("range", 172, 172),
            ConstString.image_border(1, 4): ("range", 172, 172),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 225, 225),
            ConstString.image_border(2, 2): ("range", 117, 117),
            ConstString.image_border(2, 3): ("range", 222, 222),
            ConstString.image_border(2, 4): ("range", 222, 222),
        },
    )


def test_failed_split_line_line_algo_png() -> None:
    """Failed to compute line for split line with line detection alog."""
    treat_file(
        MockDisableSeparatePage(MAX_VAL),
        get_absolute_from_current_path(
            __file__, "failed_split_line_line_algo.png"
        ),
        {
            ConstString.separation_double_page_angle(): (
                "range",
                90.01,
                90.02,
            ),
            ConstString.separation_double_page_y(): ("range", 2575, 2575),
            ConstString.page_rotation(1): ("range", -0.16, -0.14),
            ConstString.page_rotation(2): ("range", 0.04, 0.06),
            ConstString.image_crop(1, "x1"): ("range", 407, 407),
            ConstString.image_crop(1, "y1"): ("range", 2925, 2925),
            ConstString.image_crop(1, "x2"): ("range", 2419, 2419),
            ConstString.image_crop(1, "y2"): ("range", 3174, 3174),
            ConstString.image_crop(2, "x1"): ("range", 1180, 1180),
            ConstString.image_crop(2, "y1"): ("range", 1724, 1724),
            ConstString.image_crop(2, "x2"): ("range", 1181, 1181),
            ConstString.image_crop(2, "y2"): ("range", 1725, 1725),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 2930, 2930),
            ConstString.image_border(1, 2): ("range", 308, 308),
            ConstString.image_border(1, 3): ("range", 224, 224),
            ConstString.image_border(1, 4): ("range", 224, 224),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 1753, 1753),
            ConstString.image_border(2, 2): ("range", 1753, 1753),
            ConstString.image_border(2, 3): ("range", 1239, 1239),
            ConstString.image_border(2, 4): ("range", 1239, 1239),
        },
    )


def test_failed_split_line_line_algo_2_png() -> None:
    """Failed to compute line for split line with line detection alog."""
    treat_file(
        MockDisableSeparatePage(MAX_VAL),
        get_absolute_from_current_path(
            __file__, "failed_split_line_line_algo_2.png"
        ),
        {
            ConstString.separation_double_page_angle(): (
                "range",
                89.97,
                89.98,
            ),
            ConstString.separation_double_page_y(): ("range", 2497, 2497),
            ConstString.page_rotation(1): ("range", -0.01, 0.01),
            ConstString.page_rotation(2): ("range", 0.59, 0.61),
            ConstString.image_crop(1, "x1"): ("range", 272, 272),
            ConstString.image_crop(1, "y1"): ("range", 149, 149),
            ConstString.image_crop(1, "x2"): ("range", 2383, 2383),
            ConstString.image_crop(1, "y2"): ("range", 3353, 3353),
            ConstString.image_crop(2, "x1"): ("range", 122, 122),
            ConstString.image_crop(2, "y1"): ("range", 155, 155),
            ConstString.image_crop(2, "x2"): ("range", 2245, 2245),
            ConstString.image_crop(2, "y2"): ("range", 3350, 3350),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 137, 137),
            ConstString.image_border(1, 2): ("range", 146, 146),
            ConstString.image_border(1, 3): ("range", 174, 174),
            ConstString.image_border(1, 4): ("range", 174, 174),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 138, 138),
            ConstString.image_border(2, 2): ("range", 154, 154),
            ConstString.image_border(2, 3): ("range", 168, 168),
            ConstString.image_border(2, 4): ("range", 168, 168),
        },
    )
