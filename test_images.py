import unittest

import numpy as np

from angle import Angle
import cv2ext
from print_interface import ConstString
from script import get_absolute_from_current_path, treat_file
from tests.mock_separate_page import MockDisableSeparatePage


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
                Angle.deg(90.46),
                Angle.deg(90.63),
            ),
            ConstString.separation_double_page_y(): ("range", 2481, 2489),
            ConstString.page_rotation(1): (
                "range",
                Angle.deg(0.54),
                Angle.deg(0.76),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(0.09),
                Angle.deg(0.21),
            ),
            ConstString.image_crop(1, "x1"): ("range", 327, 332),
            ConstString.image_crop(1, "y1"): ("range", 334, 337),
            ConstString.image_crop(1, "x2"): ("range", 2342, 2346),
            ConstString.image_crop(1, "y2"): ("range", 3221, 3223),
            ConstString.image_crop(2, "x1"): ("range", 166, 175),
            ConstString.image_crop(2, "y1"): ("range", 648, 649),
            ConstString.image_crop(2, "x2"): ("range", 2180, 2189),
            ConstString.image_crop(2, "y2"): ("range", 3360, 3362),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 317, 340),
            ConstString.image_border(1, 2): ("range", 260, 282),
            ConstString.image_border(1, 3): ("range", 220, 225),
            ConstString.image_border(1, 4): ("range", 220, 225),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 639, 674),
            ConstString.image_border(2, 2): ("range", 101, 134),
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
                Angle.deg(89.91),
                Angle.deg(90.32),
            ),
            ConstString.separation_double_page_y(): ("range", 2486, 2492),
            ConstString.page_rotation(1): (
                "range",
                Angle.deg(-0.01),
                Angle.deg(0.11),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(0.19),
                Angle.deg(0.41),
            ),
            ConstString.image_crop(1, "x1"): ("range", 1181, 1191),
            ConstString.image_crop(1, "y1"): ("range", 1719, 1751),
            ConstString.image_crop(1, "x2"): ("range", 1182, 1192),
            ConstString.image_crop(1, "y2"): ("range", 1720, 1752),
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
                Angle.deg(89.95),
                Angle.deg(90.1),
            ),
            ConstString.separation_double_page_y(): ("range", 2451, 2458),
            ConstString.page_rotation(1): (
                "range",
                Angle.deg(-0.01),
                Angle.deg(0.16),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(-0.21),
                Angle.deg(0.06),
            ),
            ConstString.image_crop(1, "x1"): ("range", 296, 299),
            ConstString.image_crop(1, "y1"): ("range", 140, 144),
            ConstString.image_crop(1, "x2"): ("range", 2306, 2309),
            ConstString.image_crop(1, "y2"): ("range", 3346, 3348),
            ConstString.image_crop(2, "x1"): ("range", 156, 159),
            ConstString.image_crop(2, "y1"): ("range", 144, 146),
            ConstString.image_crop(2, "x2"): ("range", 2168, 2172),
            ConstString.image_crop(2, "y2"): ("range", 3351, 3353),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 127, 134),
            ConstString.image_border(1, 2): ("range", 146, 157),
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
                Angle.deg(90.07),
                Angle.deg(90.50),
            ),
            ConstString.separation_double_page_y(): ("range", 2476, 2487),
            ConstString.page_rotation(1): (
                "range",
                Angle.deg(0.04),
                Angle.deg(0.46),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(0.19),
                Angle.deg(0.51),
            ),
            ConstString.image_crop(1, "x1"): ("range", 31, 91),
            ConstString.image_crop(1, "y1"): ("range", 1, 23),
            ConstString.image_crop(1, "x2"): ("range", 2456, 2483),
            ConstString.image_crop(1, "y2"): ("range", 3483, 3505),
            ConstString.image_crop(2, "x1"): ("range", 161, 183),
            ConstString.image_crop(2, "y1"): ("range", 231, 236),
            ConstString.image_crop(2, "x2"): ("range", 2245, 2261),
            ConstString.image_crop(2, "y2"): ("range", 3354, 3359),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 2, 19),
            ConstString.image_border(1, 2): ("range", 2, 19),
            ConstString.image_border(1, 3): ("range", 16, 55),
            ConstString.image_border(1, 4): ("range", 16, 55),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 206, 228),
            ConstString.image_border(2, 2): ("range", 140, 160),
            ConstString.image_border(2, 3): ("range", 186, 192),
            ConstString.image_border(2, 4): ("range", 186, 192),
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
                Angle.deg(89.89),
                Angle.deg(90.17),
            ),
            ConstString.separation_double_page_y(): ("range", 2477, 2486),
            ConstString.page_rotation(1): (
                "range",
                Angle.deg(-0.16),
                Angle.deg(0.21),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(-0.01),
                Angle.deg(0.21),
            ),
            ConstString.image_crop(1, "x1"): ("range", 41, 116),
            ConstString.image_crop(1, "y1"): ("range", 3, 13),
            ConstString.image_crop(1, "x2"): ("range", 2474, 2483),
            ConstString.image_crop(1, "y2"): ("range", 3499, 3505),
            ConstString.image_crop(2, "x1"): ("range", 155, 167),
            ConstString.image_crop(2, "y1"): ("range", 217, 220),
            ConstString.image_crop(2, "x2"): ("range", 2235, 2248),
            ConstString.image_crop(2, "y2"): ("range", 3348, 3350),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 5, 11),
            ConstString.image_border(1, 2): ("range", 5, 11),
            ConstString.image_border(1, 3): ("range", 21, 58),
            ConstString.image_border(1, 4): ("range", 21, 58),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 205, 225),
            ConstString.image_border(2, 2): ("range", 129, 150),
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
                Angle.deg(90.00),
                Angle.deg(90.22),
            ),
            ConstString.separation_double_page_y(): ("range", 2477, 2487),
            ConstString.page_rotation(1): (
                "range",
                Angle.deg(-0.01),
                Angle.deg(0.21),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(-0.01),
                Angle.deg(0.21),
            ),
            ConstString.image_crop(1, "x1"): ("range", 53, 61),
            ConstString.image_crop(1, "y1"): ("range", 6, 9),
            ConstString.image_crop(1, "x2"): ("range", 2472, 2485),
            ConstString.image_crop(1, "y2"): ("range", 3500, 3505),
            ConstString.image_crop(2, "x1"): ("range", 154, 167),
            ConstString.image_crop(2, "y1"): ("range", 217, 219),
            ConstString.image_crop(2, "x2"): ("range", 2237, 2248),
            ConstString.image_crop(2, "y2"): ("range", 3348, 3350),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 5, 8),
            ConstString.image_border(1, 2): ("range", 5, 8),
            ConstString.image_border(1, 3): ("range", 24, 33),
            ConstString.image_border(1, 4): ("range", 24, 33),
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
                Angle.deg(89.71),
                Angle.deg(89.81),
            ),
            ConstString.separation_double_page_y(): ("range", 2471, 2475),
            ConstString.page_rotation(1): (
                "range",
                Angle.deg(-0.46),
                Angle.deg(-0.14),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(0.04),
                Angle.deg(0.21),
            ),
            ConstString.image_crop(1, "x1"): ("range", 241, 245),
            ConstString.image_crop(1, "y1"): ("range", 156, 161),
            ConstString.image_crop(1, "x2"): ("range", 2350, 2357),
            ConstString.image_crop(1, "y2"): ("range", 3364, 3368),
            ConstString.image_crop(2, "x1"): ("range", 136, 153),
            ConstString.image_crop(2, "y1"): ("range", 145, 147),
            ConstString.image_crop(2, "x2"): ("range", 2243, 2260),
            ConstString.image_crop(2, "y2"): ("range", 3350, 3352),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 130, 145),
            ConstString.image_border(1, 2): ("range", 135, 152),
            ConstString.image_border(1, 3): ("range", 172, 177),
            ConstString.image_border(1, 4): ("range", 172, 177),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 116, 131),
            ConstString.image_border(2, 2): ("range", 151, 168),
            ConstString.image_border(2, 3): ("range", 174, 176),
            ConstString.image_border(2, 4): ("range", 174, 176),
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
                Angle.deg(89.81),
                Angle.deg(89.94),
            ),
            ConstString.separation_double_page_y(): ("range", 2463, 2465),
            ConstString.page_rotation(1): (
                "range",
                Angle.deg(-0.16),
                Angle.deg(0.01),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(0.49),
                Angle.deg(0.66),
            ),
            ConstString.image_crop(1, "x1"): ("range", 211, 213),
            ConstString.image_crop(1, "y1"): ("range", 155, 157),
            ConstString.image_crop(1, "x2"): ("range", 2322, 2324),
            ConstString.image_crop(1, "y2"): ("range", 3362, 3363),
            ConstString.image_crop(2, "x1"): ("range", 124, 126),
            ConstString.image_crop(2, "y1"): ("range", 165, 167),
            ConstString.image_crop(2, "x2"): ("range", 2235, 2237),
            ConstString.image_crop(2, "y2"): ("range", 3372, 3374),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 115, 180),
            ConstString.image_border(1, 2): ("range", 100, 167),
            ConstString.image_border(1, 3): ("range", 173, 175),
            ConstString.image_border(1, 4): ("range", 173, 175),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 129, 146),
            ConstString.image_border(2, 2): ("range", 134, 152),
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
                Angle.deg(90.10),
                Angle.deg(90.47),
            ),
            ConstString.separation_double_page_y(): ("range", 2453, 2463),
            ConstString.page_rotation(1): (
                "range",
                Angle.deg(-0.11),
                Angle.deg(0.01),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(0.19),
                Angle.deg(0.46),
            ),
            ConstString.image_crop(1, "x1"): ("range", 301, 303),
            ConstString.image_crop(1, "y1"): ("range", 147, 148),
            ConstString.image_crop(1, "x2"): ("range", 2313, 2315),
            ConstString.image_crop(1, "y2"): ("range", 3350, 3351),
            ConstString.image_crop(2, "x1"): ("range", 162, 180),
            ConstString.image_crop(2, "y1"): ("range", 151, 155),
            ConstString.image_crop(2, "x2"): ("range", 2177, 2191),
            ConstString.image_crop(2, "y2"): ("range", 3359, 3363),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 116, 134),
            ConstString.image_border(1, 2): ("range", 150, 168),
            ConstString.image_border(1, 3): ("range", 223, 225),
            ConstString.image_border(1, 4): ("range", 223, 225),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 95, 141),
            ConstString.image_border(2, 2): ("range", 142, 186),
            ConstString.image_border(2, 3): ("range", 218, 224),
            ConstString.image_border(2, 4): ("range", 218, 224),
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
                Angle.deg(89.22),
                Angle.deg(89.55),
            ),
            ConstString.separation_double_page_y(): ("range", 2508, 2512),
            ConstString.page_rotation(1): (
                "range",
                Angle.deg(-0.76),
                Angle.deg(-0.54),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(-0.11),
                Angle.deg(0.06),
            ),
            ConstString.image_crop(1, "x1"): ("range", 262, 265),
            ConstString.image_crop(1, "y1"): ("range", 149, 161),
            ConstString.image_crop(1, "x2"): ("range", 2375, 2380),
            ConstString.image_crop(1, "y2"): ("range", 3356, 3358),
            ConstString.image_crop(2, "x1"): ("range", 133, 141),
            ConstString.image_crop(2, "y1"): ("range", 139, 141),
            ConstString.image_crop(2, "x2"): ("range", 2259, 2263),
            ConstString.image_crop(2, "y2"): ("range", 3345, 3347),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 84, 134),
            ConstString.image_border(1, 2): ("range", 149, 208),
            ConstString.image_border(1, 3): ("range", 171, 175),
            ConstString.image_border(1, 4): ("range", 171, 175),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 128, 143),
            ConstString.image_border(2, 2): ("range", 140, 154),
            ConstString.image_border(2, 3): ("range", 167, 169),
            ConstString.image_border(2, 4): ("range", 167, 169),
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
                Angle.deg(90.11),
                Angle.deg(90.24),
            ),
            ConstString.separation_double_page_y(): ("range", 2475, 2482),
            ConstString.page_rotation(1): (
                "range",
                Angle.deg(0.14),
                Angle.deg(0.21),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(0.19),
                Angle.deg(0.21),
            ),
            ConstString.image_crop(1, "x1"): ("range", 330, 332),
            ConstString.image_crop(1, "y1"): ("range", 131, 132),
            ConstString.image_crop(1, "x2"): ("range", 2342, 2342),
            ConstString.image_crop(1, "y2"): ("range", 3335, 3336),
            ConstString.image_crop(2, "x1"): ("range", 162, 169),
            ConstString.image_crop(2, "y1"): ("range", 139, 139),
            ConstString.image_crop(2, "x2"): ("range", 2175, 2182),
            ConstString.image_crop(2, "y2"): ("range", 3345, 3345),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 112, 122),
            ConstString.image_border(1, 2): ("range", 162, 170),
            ConstString.image_border(1, 3): ("range", 224, 225),
            ConstString.image_border(1, 4): ("range", 224, 225),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 123, 133),
            ConstString.image_border(2, 2): ("range", 148, 157),
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
                Angle.deg(90.17),
                Angle.deg(90.40),
            ),
            ConstString.separation_double_page_y(): ("range", 2436, 2442),
            ConstString.page_rotation(1): (
                "range",
                Angle.deg(0.04),
                Angle.deg(0.21),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(0.19),
                Angle.deg(0.41),
            ),
            ConstString.image_crop(1, "x1"): ("range", 294, 294),
            ConstString.image_crop(1, "y1"): ("range", 136, 137),
            ConstString.image_crop(1, "x2"): ("range", 2324, 2326),
            ConstString.image_crop(1, "y2"): ("range", 3375, 3376),
            ConstString.image_crop(2, "x1"): ("range", 136, 146),
            ConstString.image_crop(2, "y1"): ("range", 190, 193),
            ConstString.image_crop(2, "x2"): ("range", 2165, 2175),
            ConstString.image_crop(2, "y2"): ("range", 3386, 3389),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 121, 131),
            ConstString.image_border(1, 2): ("range", 116, 126),
            ConstString.image_border(1, 3): ("range", 214, 215),
            ConstString.image_border(1, 4): ("range", 214, 215),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 181, 185),
            ConstString.image_border(2, 2): ("range", 107, 111),
            ConstString.image_border(2, 3): ("range", 212, 216),
            ConstString.image_border(2, 4): ("range", 212, 216),
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
                Angle.deg(90.58),
                Angle.deg(90.64),
            ),
            ConstString.separation_double_page_y(): ("range", 2491, 2500),
            ConstString.page_rotation(1): (
                "range",
                Angle.deg(0.59),
                Angle.deg(0.81),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(0.64),
                Angle.deg(0.81),
            ),
            ConstString.image_crop(1, "x1"): ("range", 319, 324),
            ConstString.image_crop(1, "y1"): ("range", 197, 199),
            ConstString.image_crop(1, "x2"): ("range", 2351, 2354),
            ConstString.image_crop(1, "y2"): ("range", 3393, 3395),
            ConstString.image_crop(2, "x1"): ("range", 130, 139),
            ConstString.image_crop(2, "y1"): ("range", 222, 224),
            ConstString.image_crop(2, "x2"): ("range", 2160, 2168),
            ConstString.image_crop(2, "y2"): ("range", 3418, 3420),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 174, 180),
            ConstString.image_border(1, 2): ("range", 111, 116),
            ConstString.image_border(1, 3): ("range", 212, 215),
            ConstString.image_border(1, 4): ("range", 212, 215),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 191, 197),
            ConstString.image_border(2, 2): ("range", 92, 102),
            ConstString.image_border(2, 3): ("range", 213, 216),
            ConstString.image_border(2, 4): ("range", 213, 216),
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
                Angle.deg(90.41),
                Angle.deg(90.45),
            ),
            ConstString.separation_double_page_y(): ("range", 2495, 2498),
            ConstString.page_rotation(1): (
                "range",
                Angle.deg(0.19),
                Angle.deg(0.36),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(0.84),
                Angle.deg(0.96),
            ),
            ConstString.image_crop(1, "x1"): ("range", 331, 331),
            ConstString.image_crop(1, "y1"): ("range", 164, 166),
            ConstString.image_crop(1, "x2"): ("range", 2375, 2377),
            ConstString.image_crop(1, "y2"): ("range", 3375, 3377),
            ConstString.image_crop(2, "x1"): ("range", 102, 104),
            ConstString.image_crop(2, "y1"): ("range", 207, 209),
            ConstString.image_crop(2, "x2"): ("range", 2132, 2135),
            ConstString.image_crop(2, "y2"): ("range", 3413, 3414),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 148, 158),
            ConstString.image_border(1, 2): ("range", 116, 128),
            ConstString.image_border(1, 3): ("range", 207, 208),
            ConstString.image_border(1, 4): ("range", 207, 208),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 186, 192),
            ConstString.image_border(2, 2): ("range", 90, 95),
            ConstString.image_border(2, 3): ("range", 213, 215),
            ConstString.image_border(2, 4): ("range", 213, 215),
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
                Angle.deg(90.37),
                Angle.deg(90.54),
            ),
            ConstString.separation_double_page_y(): ("range", 2500, 2503),
            ConstString.page_rotation(1): (
                "range",
                Angle.deg(-0.16),
                Angle.deg(-0.14),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(0.79),
                Angle.deg(0.91),
            ),
            ConstString.image_crop(1, "x1"): ("range", 385, 385),
            ConstString.image_crop(1, "y1"): ("range", 179, 179),
            ConstString.image_crop(1, "x2"): ("range", 2411, 2411),
            ConstString.image_crop(1, "y2"): ("range", 3374, 3374),
            ConstString.image_crop(2, "x1"): ("range", 2, 124),
            ConstString.image_crop(2, "y1"): ("range", 0, 58),
            ConstString.image_crop(2, "x2"): ("range", 2399, 2489),
            ConstString.image_crop(2, "y2"): ("range", 3391, 3505),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 167, 173),
            ConstString.image_border(1, 2): ("range", 119, 124),
            ConstString.image_border(1, 3): ("range", 217, 217),
            ConstString.image_border(1, 4): ("range", 217, 217),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 0, 10),
            ConstString.image_border(2, 2): ("range", 1, 163),
            ConstString.image_border(2, 3): ("range", 9, 92),
            ConstString.image_border(2, 4): ("range", 9, 92),
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
                Angle.deg(89.46),
                Angle.deg(89.48),
            ),
            ConstString.separation_double_page_y(): ("range", 2476, 2476),
            ConstString.page_rotation(1): (
                "range",
                Angle.deg(-0.16),
                Angle.deg(-0.09),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(-0.46),
                Angle.deg(-0.14),
            ),
            ConstString.image_crop(1, "x1"): ("range", 204, 205),
            ConstString.image_crop(1, "y1"): ("range", 157, 158),
            ConstString.image_crop(1, "x2"): ("range", 2320, 2321),
            ConstString.image_crop(1, "y2"): ("range", 3366, 3366),
            ConstString.image_crop(2, "x1"): ("range", 185, 186),
            ConstString.image_crop(2, "y1"): ("range", 221, 225),
            ConstString.image_crop(2, "x2"): ("range", 2201, 2204),
            ConstString.image_crop(2, "y2"): ("range", 3362, 3366),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 137, 145),
            ConstString.image_border(1, 2): ("range", 133, 142),
            ConstString.image_border(1, 3): ("range", 171, 172),
            ConstString.image_border(1, 4): ("range", 171, 172),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 215, 225),
            ConstString.image_border(2, 2): ("range", 117, 128),
            ConstString.image_border(2, 3): ("range", 220, 222),
            ConstString.image_border(2, 4): ("range", 220, 222),
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
                Angle.deg(90.0),
                Angle.deg(90.05),
            ),
            ConstString.separation_double_page_y(): ("range", 2573, 2576),
            ConstString.page_rotation(1): (
                "range",
                Angle.deg(-0.16),
                Angle.deg(0.01),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(-0.11),
                Angle.deg(0.11),
            ),
            ConstString.image_crop(1, "x1"): ("range", 407, 411),
            ConstString.image_crop(1, "y1"): ("range", 2925, 2927),
            ConstString.image_crop(1, "x2"): ("range", 2419, 2422),
            ConstString.image_crop(1, "y2"): ("range", 3172, 3174),
            ConstString.image_crop(2, "x1"): ("range", 1180, 1189),
            ConstString.image_crop(2, "y1"): ("range", 1724, 1748),
            ConstString.image_crop(2, "x2"): ("range", 1181, 1190),
            ConstString.image_crop(2, "y2"): ("range", 1725, 1749),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 2917, 2930),
            ConstString.image_border(1, 2): ("range", 308, 323),
            ConstString.image_border(1, 3): ("range", 224, 224),
            ConstString.image_border(1, 4): ("range", 224, 224),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 1752, 1753),
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
                Angle.deg(89.97),
                Angle.deg(90.05),
            ),
            ConstString.separation_double_page_y(): ("range", 2497, 2500),
            ConstString.page_rotation(1): (
                "range",
                Angle.deg(-0.01),
                Angle.deg(0.06),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(0.49),
                Angle.deg(0.61),
            ),
            ConstString.image_crop(1, "x1"): ("range", 271, 272),
            ConstString.image_crop(1, "y1"): ("range", 149, 149),
            ConstString.image_crop(1, "x2"): ("range", 2382, 2383),
            ConstString.image_crop(1, "y2"): ("range", 3353, 3354),
            ConstString.image_crop(2, "x1"): ("range", 107, 124),
            ConstString.image_crop(2, "y1"): ("range", 154, 155),
            ConstString.image_crop(2, "x2"): ("range", 2230, 2247),
            ConstString.image_crop(2, "y2"): ("range", 3350, 3351),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 137, 141),
            ConstString.image_border(1, 2): ("range", 141, 146),
            ConstString.image_border(1, 3): ("range", 174, 174),
            ConstString.image_border(1, 4): ("range", 174, 174),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 134, 146),
            ConstString.image_border(2, 2): ("range", 145, 158),
            ConstString.image_border(2, 3): ("range", 167, 168),
            ConstString.image_border(2, 4): ("range", 167, 168),
        },
    )


def test_crop_too_much_3_png() -> None:
    """Failed to compute line for split line with line detection alog."""
    treat_file(
        MockDisableSeparatePage(MAX_VAL),
        get_absolute_from_current_path(__file__, "crop_too_much_3.png"),
        {
            ConstString.separation_double_page_angle(): (
                "range",
                Angle.deg(89.49),
                Angle.deg(89.56),
            ),
            ConstString.separation_double_page_y(): ("range", 2494, 2499),
            ConstString.page_rotation(1): (
                "range",
                Angle.deg(-0.96),
                Angle.deg(-0.89),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(-0.16),
                Angle.deg(-0.14),
            ),
            ConstString.image_crop(1, "x1"): ("range", 373, 374),
            ConstString.image_crop(1, "y1"): ("range", 258, 258),
            ConstString.image_crop(1, "x2"): ("range", 2385, 2386),
            ConstString.image_crop(1, "y2"): ("range", 3458, 3459),
            ConstString.image_crop(2, "x1"): ("range", 167, 172),
            ConstString.image_crop(2, "y1"): ("range", 228, 228),
            ConstString.image_crop(2, "x2"): ("range", 2180, 2185),
            ConstString.image_crop(2, "y2"): ("range", 3417, 3417),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 237, 239),
            ConstString.image_border(1, 2): ("range", 46, 50),
            ConstString.image_border(1, 3): ("range", 223, 224),
            ConstString.image_border(1, 4): ("range", 223, 224),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 192, 214),
            ConstString.image_border(2, 2): ("range", 84, 106),
            ConstString.image_border(2, 3): ("range", 223, 223),
            ConstString.image_border(2, 4): ("range", 223, 223),
        },
    )


def test_wrong_wave_split_line_2_png() -> None:
    """Need to relax tolerance to have the split line by wave algo."""
    treat_file(
        MockDisableSeparatePage(MAX_VAL),
        get_absolute_from_current_path(
            __file__, "wrong_wave_split_line_2.png"
        ),
        {
            ConstString.separation_double_page_angle(): (
                "range",
                Angle.deg(90.77),
                Angle.deg(90.78),
            ),
            ConstString.separation_double_page_y(): ("range", 2490, 2490),
            ConstString.page_rotation(1): (
                "range",
                Angle.deg(0.19),
                Angle.deg(0.41),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(1.64),
                Angle.deg(1.81),
            ),
            ConstString.image_crop(1, "x1"): ("range", 224, 227),
            ConstString.image_crop(1, "y1"): ("range", 147, 148),
            ConstString.image_crop(1, "x2"): ("range", 2337, 2342),
            ConstString.image_crop(1, "y2"): ("range", 3353, 3355),
            ConstString.image_crop(2, "x1"): ("range", 72, 108),
            ConstString.image_crop(2, "y1"): ("range", 195, 197),
            ConstString.image_crop(2, "x2"): ("range", 2194, 2231),
            ConstString.image_crop(2, "y2"): ("range", 3396, 3398),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 126, 140),
            ConstString.image_border(1, 2): ("range", 140, 153),
            ConstString.image_border(1, 3): ("range", 172, 173),
            ConstString.image_border(1, 4): ("range", 172, 173),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 165, 171),
            ConstString.image_border(2, 2): ("range", 116, 121),
            ConstString.image_border(2, 3): ("range", 167, 169),
            ConstString.image_border(2, 4): ("range", 167, 169),
        },
    )


def test_wrong_wave_split_line_3_png() -> None:
    """Need to relax tolerance to have the split line by wave algo."""
    treat_file(
        MockDisableSeparatePage(MAX_VAL),
        get_absolute_from_current_path(
            __file__, "wrong_wave_split_line_3.png"
        ),
        {
            ConstString.separation_double_page_angle(): (
                "range",
                Angle.deg(90.03),
                Angle.deg(90.09),
            ),
            ConstString.separation_double_page_y(): ("range", 2510, 2514),
            ConstString.page_rotation(1): (
                "range",
                Angle.deg(-0.01),
                Angle.deg(0.11),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(0.19),
                Angle.deg(0.36),
            ),
            ConstString.image_crop(1, "x1"): ("range", 272, 274),
            ConstString.image_crop(1, "y1"): ("range", 219, 221),
            ConstString.image_crop(1, "x2"): ("range", 2383, 2383),
            ConstString.image_crop(1, "y2"): ("range", 3422, 3423),
            ConstString.image_crop(2, "x1"): ("range", 112, 119),
            ConstString.image_crop(2, "y1"): ("range", 225, 226),
            ConstString.image_crop(2, "x2"): ("range", 2235, 2240),
            ConstString.image_crop(2, "y2"): ("range", 3413, 3415),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 190, 202),
            ConstString.image_border(1, 2): ("range", 81, 93),
            ConstString.image_border(1, 3): ("range", 174, 175),
            ConstString.image_border(1, 4): ("range", 174, 175),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 190, 207),
            ConstString.image_border(2, 2): ("range", 90, 110),
            ConstString.image_border(2, 3): ("range", 167, 169),
            ConstString.image_border(2, 4): ("range", 167, 169),
        },
    )


def test_no_split_line_wave_algo_png() -> None:
    """Failed to detect wave due to image."""
    treat_file(
        MockDisableSeparatePage(MAX_VAL),
        get_absolute_from_current_path(
            __file__, "no_split_line_wave_algo.png"
        ),
        {
            ConstString.separation_double_page_angle(): (
                "range",
                Angle.deg(89.72),
                Angle.deg(89.94),
            ),
            ConstString.separation_double_page_y(): ("range", 2475, 2484),
            ConstString.page_rotation(1): (
                "range",
                Angle.deg(-0.06),
                Angle.deg(0.05),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(-0.56),
                Angle.deg(-0.44),
            ),
            ConstString.image_crop(1, "x1"): ("range", 97, 101),
            ConstString.image_crop(1, "y1"): ("range", 27, 79),
            ConstString.image_crop(1, "x2"): ("range", 2477, 2498),
            ConstString.image_crop(1, "y2"): ("range", 3505, 3505),
            ConstString.image_crop(2, "x1"): ("range", 162, 171),
            ConstString.image_crop(2, "y1"): ("range", 266, 267),
            ConstString.image_crop(2, "x2"): ("range", 2238, 2248),
            ConstString.image_crop(2, "y2"): ("range", 3380, 3382),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 15, 41),
            ConstString.image_border(1, 2): ("range", 15, 41),
            ConstString.image_border(1, 3): ("range", 42, 52),
            ConstString.image_border(1, 4): ("range", 42, 52),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 252, 261),
            ConstString.image_border(2, 2): ("range", 110, 120),
            ConstString.image_border(2, 3): ("range", 191, 198),
            ConstString.image_border(2, 4): ("range", 191, 198),
        },
    )


def test_no_split_line_wave_algo_2_png() -> None:
    """Failed to detect wave due to missing wave at the bottom."""
    treat_file(
        MockDisableSeparatePage(MAX_VAL),
        get_absolute_from_current_path(
            __file__, "no_split_line_wave_algo_2.png"
        ),
        {
            ConstString.separation_double_page_angle(): (
                "range",
                Angle.deg(90.47),
                Angle.deg(91.22),
            ),
            ConstString.separation_double_page_y(): ("range", 2478, 2488),
            ConstString.page_rotation(1): (
                "range",
                Angle.deg(1.04),
                Angle.deg(1.16),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(0.09),
                Angle.deg(0.21),
            ),
            ConstString.image_crop(1, "x1"): ("range", 266, 267),
            ConstString.image_crop(1, "y1"): ("range", 209, 210),
            ConstString.image_crop(1, "x2"): ("range", 2342, 2343),
            ConstString.image_crop(1, "y2"): ("range", 3412, 3413),
            ConstString.image_crop(2, "x1"): ("range", 163, 199),
            ConstString.image_crop(2, "y1"): ("range", 240, 241),
            ConstString.image_crop(2, "x2"): ("range", 2246, 2282),
            ConstString.image_crop(2, "y2"): ("range", 3433, 3433),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 180, 194),
            ConstString.image_border(1, 2): ("range", 90, 103),
            ConstString.image_border(1, 3): ("range", 192, 192),
            ConstString.image_border(1, 4): ("range", 192, 192),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 209, 226),
            ConstString.image_border(2, 2): ("range", 69, 86),
            ConstString.image_border(2, 3): ("range", 186, 188),
            ConstString.image_border(2, 4): ("range", 186, 188),
        },
    )


def test_crop_too_few_2_png() -> None:
    """Use different area on the left and the right to detect
    black noise."""
    treat_file(
        MockDisableSeparatePage(MAX_VAL),
        get_absolute_from_current_path(__file__, "crop_too_few_2.png"),
        {
            ConstString.separation_double_page_angle(): (
                "range",
                Angle.deg(90.25),
                Angle.deg(90.35),
            ),
            ConstString.separation_double_page_y(): ("range", 2531, 2534),
            ConstString.page_rotation(1): (
                "range",
                Angle.deg(1.09),
                Angle.deg(1.21),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(-0.11),
                Angle.deg(0.01),
            ),
            ConstString.image_crop(1, "x1"): ("range", 287, 289),
            ConstString.image_crop(1, "y1"): ("range", 165, 165),
            ConstString.image_crop(1, "x2"): ("range", 2398, 2400),
            ConstString.image_crop(1, "y2"): ("range", 3367, 3368),
            ConstString.image_crop(2, "x1"): ("range", 145, 151),
            ConstString.image_crop(2, "y1"): ("range", 175, 190),
            ConstString.image_crop(2, "x2"): ("range", 2271, 2275),
            ConstString.image_crop(2, "y2"): ("range", 3373, 3386),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 139, 157),
            ConstString.image_border(1, 2): ("range", 127, 145),
            ConstString.image_border(1, 3): ("range", 174, 174),
            ConstString.image_border(1, 4): ("range", 174, 174),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 175, 181),
            ConstString.image_border(2, 2): ("range", 109, 116),
            ConstString.image_border(2, 3): ("range", 167, 169),
            ConstString.image_border(2, 4): ("range", 167, 169),
        },
    )


def test_failed_detect_rectangle_png() -> None:
    """Before, approxPolyDP algo was used to detect shape.

    But, due to noise on the edge with background other pages,
    the contour have lost of noise.
    So use HoughLinesP to detect shape."""
    treat_file(
        MockDisableSeparatePage(MAX_VAL),
        get_absolute_from_current_path(
            __file__, "failed_detect_rectangle.png"
        ),
        {
            ConstString.separation_double_page_angle(): (
                "range",
                Angle.deg(90.19),
                Angle.deg(90.23),
            ),
            ConstString.separation_double_page_y(): ("range", 2471, 2474),
            ConstString.page_rotation(1): (
                "range",
                Angle.deg(0.14),
                Angle.deg(0.21),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(0.14),
                Angle.deg(0.21),
            ),
            ConstString.image_crop(1, "x1"): ("range", 257, 258),
            ConstString.image_crop(1, "y1"): ("range", 201, 202),
            ConstString.image_crop(1, "x2"): ("range", 2333, 2334),
            ConstString.image_crop(1, "y2"): ("range", 3401, 3402),
            ConstString.image_crop(2, "x1"): ("range", 135, 139),
            ConstString.image_crop(2, "y1"): ("range", 214, 215),
            ConstString.image_crop(2, "x2"): ("range", 2219, 2222),
            ConstString.image_crop(2, "y2"): ("range", 3406, 3406),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 188, 188),
            ConstString.image_border(1, 2): ("range", 97, 100),
            ConstString.image_border(1, 3): ("range", 192, 192),
            ConstString.image_border(1, 4): ("range", 192, 192),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 199, 202),
            ConstString.image_border(2, 2): ("range", 93, 95),
            ConstString.image_border(2, 3): ("range", 188, 188),
            ConstString.image_border(2, 4): ("range", 188, 188),
        },
    )


def test_single_page_png() -> None:
    """Detect that the scan is single page."""
    treat_file(
        MockDisableSeparatePage(MAX_VAL),
        get_absolute_from_current_path(__file__, "single_page.png"),
        {
            ConstString.separation_double_page_angle(): (
                "range",
                Angle.deg(89.97),
                Angle.deg(90.06),
            ),
            ConstString.separation_double_page_y(): ("range", 2469, 2476),
            ConstString.page_rotation(1): (
                "range",
                Angle.deg(-0.01),
                Angle.deg(0.01),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(-0.01),
                Angle.deg(0.01),
            ),
            ConstString.image_crop(1, "x1"): ("range", 1, 1),
            ConstString.image_crop(1, "y1"): ("range", 8, 9),
            ConstString.image_crop(1, "x2"): ("range", 2464, 2470),
            ConstString.image_crop(1, "y2"): ("range", 3505, 3505),
            ConstString.image_crop(2, "x1"): ("range", 0, 0),
            ConstString.image_crop(2, "y1"): ("range", 0, 0),
            ConstString.image_crop(2, "x2"): ("range", 0, 0),
            ConstString.image_crop(2, "y2"): ("range", 0, 0),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 5, 6),
            ConstString.image_border(1, 2): ("range", 5, 6),
            ConstString.image_border(1, 3): ("range", 6, 9),
            ConstString.image_border(1, 4): ("range", 6, 9),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 0, 0),
            ConstString.image_border(2, 2): ("range", 0, 0),
            ConstString.image_border(2, 3): ("range", 0, 0),
            ConstString.image_border(2, 4): ("range", 0, 0),
        },
    )


def test_no_split_line_wave_algo_3_png() -> None:
    """Failed to detect wave due to missing wave at the bottom."""
    treat_file(
        MockDisableSeparatePage(MAX_VAL),
        get_absolute_from_current_path(
            __file__, "no_split_line_wave_algo_3.png"
        ),
        {
            ConstString.separation_double_page_angle(): (
                "range",
                Angle.deg(90.14),
                Angle.deg(90.21),
            ),
            ConstString.separation_double_page_y(): ("range", 2403, 2408),
            ConstString.page_rotation(1): (
                "range",
                Angle.deg(-0.11),
                Angle.deg(0.16),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(-0.01),
                Angle.deg(0.36),
            ),
            ConstString.image_crop(1, "x1"): ("range", 182, 188),
            ConstString.image_crop(1, "y1"): ("range", 2955, 2959),
            ConstString.image_crop(1, "x2"): ("range", 2199, 2205),
            ConstString.image_crop(1, "y2"): ("range", 3201, 3203),
            ConstString.image_crop(2, "x1"): ("range", 0, 0),
            ConstString.image_crop(2, "y1"): ("range", 0, 0),
            ConstString.image_crop(2, "x2"): ("range", 0, 0),
            ConstString.image_crop(2, "y2"): ("range", 0, 0),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 2950, 2956),
            ConstString.image_border(1, 2): ("range", 288, 292),
            ConstString.image_border(1, 3): ("range", 221, 221),
            ConstString.image_border(1, 4): ("range", 221, 221),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 0, 0),
            ConstString.image_border(2, 2): ("range", 0, 0),
            ConstString.image_border(2, 3): ("range", 0, 0),
            ConstString.image_border(2, 4): ("range", 0, 0),
        },
    )


def test_wrong_split_line_4_png() -> None:
    """Detect wrong split line with line algo."""
    treat_file(
        MockDisableSeparatePage(MAX_VAL),
        get_absolute_from_current_path(
            __file__, "wrong_split_line_4.png"
        ),
        {
            ConstString.separation_double_page_angle(): (
                "range",
                Angle.deg(91.04),
                Angle.deg(91.06),
            ),
            ConstString.separation_double_page_y(): ("range", 60, 60),
            ConstString.page_rotation(1): (
                "range",
                Angle.deg(0.74),
                Angle.deg(1.06),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(1.04),
                Angle.deg(1.16),
            ),
            ConstString.image_crop(1, "x1"): ("range", 0, 0),
            ConstString.image_crop(1, "y1"): ("range", 0, 0),
            ConstString.image_crop(1, "x2"): ("range", 0, 0),
            ConstString.image_crop(1, "y2"): ("range", 0, 0),
            ConstString.image_crop(2, "x1"): ("range", 291, 292),
            ConstString.image_crop(2, "y1"): ("range", 330, 330),
            ConstString.image_crop(2, "x2"): ("range", 2314, 2316),
            ConstString.image_crop(2, "y2"): ("range", 3217, 3218),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 0, 0),
            ConstString.image_border(1, 2): ("range", 0, 0),
            ConstString.image_border(1, 3): ("range", 0, 0),
            ConstString.image_border(1, 4): ("range", 0, 0),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 322, 322),
            ConstString.image_border(2, 2): ("range", 277, 278),
            ConstString.image_border(2, 3): ("range", 217, 219),
            ConstString.image_border(2, 4): ("range", 217, 219),
        },
    )


def test_failed_split_line_line_algo_3_png() -> None:
    """get_rectangle_from_contour_hough_lines fails
    because fewer than 4 lines are detected."""
    treat_file(
        MockDisableSeparatePage(MAX_VAL),
        get_absolute_from_current_path(
            __file__, "failed_split_line_line_algo_3.png"
        ),
        {
            ConstString.separation_double_page_angle(): (
                "range",
                Angle.deg(89.99),
                Angle.deg(90.01),
            ),
            ConstString.separation_double_page_y(): ("range", 40, 40),
            ConstString.page_rotation(1): (
                "range",
                Angle.deg(-0.16),
                Angle.deg(0.01),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(-0.11),
                Angle.deg(0.01),
            ),
            ConstString.image_crop(1, "x1"): ("range", 0, 0),
            ConstString.image_crop(1, "y1"): ("range", 0, 0),
            ConstString.image_crop(1, "x2"): ("range", 0, 0),
            ConstString.image_crop(1, "y2"): ("range", 0, 0),
            ConstString.image_crop(2, "x1"): ("range", 246, 248),
            ConstString.image_crop(2, "y1"): ("range", 152, 154),
            ConstString.image_crop(2, "x2"): ("range", 2259, 2262),
            ConstString.image_crop(2, "y2"): ("range", 3359, 3361),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 0, 0),
            ConstString.image_border(1, 2): ("range", 0, 0),
            ConstString.image_border(1, 3): ("range", 0, 0),
            ConstString.image_border(1, 4): ("range", 0, 0),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 144, 146),
            ConstString.image_border(2, 2): ("range", 134, 136),
            ConstString.image_border(2, 3): ("range", 223, 223),
            ConstString.image_border(2, 4): ("range", 223, 223),
        },
    )
