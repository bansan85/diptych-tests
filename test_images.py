import unittest

import numpy as np
import pytest

from script import treat_file, get_absolute_from_current_path
from print_interface import ConstString
from tests.mock_separate_page import MockDisableSeparatePage
import cv2ext
from angle import Angle


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
                Angle.deg(0.65),
                Angle.deg(0.76),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(0.14),
                Angle.deg(0.21),
            ),
            ConstString.image_crop(1, "x1"): ("range", 330, 332),
            ConstString.image_crop(1, "y1"): ("range", 335, 337),
            ConstString.image_crop(1, "x2"): ("range", 2342, 2343),
            ConstString.image_crop(1, "y2"): ("range", 3222, 3223),
            ConstString.image_crop(2, "x1"): ("range", 168, 175),
            ConstString.image_crop(2, "y1"): ("range", 648, 649),
            ConstString.image_crop(2, "x2"): ("range", 2180, 2189),
            ConstString.image_crop(2, "y2"): ("range", 3360, 3361),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 317, 340),
            ConstString.image_border(1, 2): ("range", 260, 282),
            ConstString.image_border(1, 3): ("range", 223, 225),
            ConstString.image_border(1, 4): ("range", 223, 225),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 643, 674),
            ConstString.image_border(2, 2): ("range", 101, 131),
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
            ConstString.image_crop(1, "y1"): ("range", 1719, 1748),
            ConstString.image_crop(1, "x2"): ("range", 1182, 1192),
            ConstString.image_crop(1, "y2"): ("range", 1720, 1749),
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
                Angle.deg(0.06),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(-0.21),
                Angle.deg(0.01),
            ),
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
                Angle.deg(90.07),
                Angle.deg(90.50),
            ),
            ConstString.separation_double_page_y(): ("range", 2476, 2487),
            ConstString.page_rotation(1): (
                "range",
                Angle.deg(0.29),
                Angle.deg(0.41),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(0.34),
                Angle.deg(0.51),
            ),
            ConstString.image_crop(1, "x1"): ("range", 33, 91),
            ConstString.image_crop(1, "y1"): ("range", 1, 23),
            ConstString.image_crop(1, "x2"): ("range", 2456, 2483),
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
            ConstString.image_crop(1, "x1"): ("range", 43, 116),
            ConstString.image_crop(1, "y1"): ("range", 3, 13),
            ConstString.image_crop(1, "x2"): ("range", 2476, 2483),
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
            ConstString.image_border(2, 2): ("range", 129, 149),
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
            ConstString.image_crop(2, "x1"): ("range", 154, 165),
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
                Angle.deg(-0.34),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(0.09),
                Angle.deg(0.21),
            ),
            ConstString.image_crop(1, "x1"): ("range", 243, 245),
            ConstString.image_crop(1, "y1"): ("range", 159, 161),
            ConstString.image_crop(1, "x2"): ("range", 2350, 2351),
            ConstString.image_crop(1, "y2"): ("range", 3364, 3365),
            ConstString.image_crop(2, "x1"): ("range", 136, 153),
            ConstString.image_crop(2, "y1"): ("range", 146, 147),
            ConstString.image_crop(2, "x2"): ("range", 2243, 2260),
            ConstString.image_crop(2, "y2"): ("range", 3350, 3351),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 130, 143),
            ConstString.image_border(1, 2): ("range", 140, 152),
            ConstString.image_border(1, 3): ("range", 176, 177),
            ConstString.image_border(1, 4): ("range", 176, 177),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 116, 130),
            ConstString.image_border(2, 2): ("range", 153, 168),
            ConstString.image_border(2, 3): ("range", 175, 176),
            ConstString.image_border(2, 4): ("range", 175, 176),
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
                Angle.deg(-0.04),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(0.49),
                Angle.deg(0.66),
            ),
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
            ConstString.image_border(2, 2): ("range", 137, 152),
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
                Angle.deg(90.12),
                Angle.deg(90.47),
            ),
            ConstString.separation_double_page_y(): ("range", 2453, 2463),
            ConstString.page_rotation(1): (
                "range",
                Angle.deg(-0.01),
                Angle.deg(0.01),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(0.39),
                Angle.deg(0.46),
            ),
            ConstString.image_crop(1, "x1"): ("range", 303, 303),
            ConstString.image_crop(1, "y1"): ("range", 148, 148),
            ConstString.image_crop(1, "x2"): ("range", 2313, 2313),
            ConstString.image_crop(1, "y2"): ("range", 3351, 3351),
            ConstString.image_crop(2, "x1"): ("range", 165, 180),
            ConstString.image_crop(2, "y1"): ("range", 154, 155),
            ConstString.image_crop(2, "x2"): ("range", 2179, 2191),
            ConstString.image_crop(2, "y2"): ("range", 3359, 3360),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 116, 133),
            ConstString.image_border(1, 2): ("range", 151, 168),
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
                Angle.deg(89.22),
                Angle.deg(89.55),
            ),
            ConstString.separation_double_page_y(): ("range", 2508, 2512),
            ConstString.page_rotation(1): (
                "range",
                Angle.deg(-0.76),
                Angle.deg(-0.64),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(-0.01),
                Angle.deg(0.06),
            ),
            ConstString.image_crop(1, "x1"): ("range", 263, 265),
            ConstString.image_crop(1, "y1"): ("range", 150, 161),
            ConstString.image_crop(1, "x2"): ("range", 2375, 2377),
            ConstString.image_crop(1, "y2"): ("range", 3356, 3357),
            ConstString.image_crop(2, "x1"): ("range", 135, 141),
            ConstString.image_crop(2, "y1"): ("range", 141, 141),
            ConstString.image_crop(2, "x2"): ("range", 2259, 2263),
            ConstString.image_crop(2, "y2"): ("range", 3345, 3345),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 84, 134),
            ConstString.image_border(1, 2): ("range", 149, 208),
            ConstString.image_border(1, 3): ("range", 173, 175),
            ConstString.image_border(1, 4): ("range", 173, 175),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 129, 143),
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
                Angle.deg(0.19),
                Angle.deg(0.21),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(0.19),
                Angle.deg(0.21),
            ),
            ConstString.image_crop(1, "x1"): ("range", 332, 332),
            ConstString.image_crop(1, "y1"): ("range", 131, 131),
            ConstString.image_crop(1, "x2"): ("range", 2342, 2342),
            ConstString.image_crop(1, "y2"): ("range", 3336, 3336),
            ConstString.image_crop(2, "x1"): ("range", 162, 169),
            ConstString.image_crop(2, "y1"): ("range", 139, 139),
            ConstString.image_crop(2, "x2"): ("range", 2175, 2182),
            ConstString.image_crop(2, "y2"): ("range", 3345, 3345),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 112, 118),
            ConstString.image_border(1, 2): ("range", 164, 170),
            ConstString.image_border(1, 3): ("range", 225, 225),
            ConstString.image_border(1, 4): ("range", 225, 225),
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
                Angle.deg(0.34),
                Angle.deg(0.41),
            ),
            ConstString.image_crop(1, "x1"): ("range", 294, 294),
            ConstString.image_crop(1, "y1"): ("range", 136, 137),
            ConstString.image_crop(1, "x2"): ("range", 2325, 2326),
            ConstString.image_crop(1, "y2"): ("range", 3375, 3376),
            ConstString.image_crop(2, "x1"): ("range", 138, 146),
            ConstString.image_crop(2, "y1"): ("range", 192, 193),
            ConstString.image_crop(2, "x2"): ("range", 2165, 2175),
            ConstString.image_crop(2, "y2"): ("range", 3386, 3387),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 121, 128),
            ConstString.image_border(1, 2): ("range", 119, 126),
            ConstString.image_border(1, 3): ("range", 214, 214),
            ConstString.image_border(1, 4): ("range", 214, 214),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 183, 185),
            ConstString.image_border(2, 2): ("range", 108, 110),
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
                Angle.deg(90.61),
                Angle.deg(90.64),
            ),
            ConstString.separation_double_page_y(): ("range", 2491, 2498),
            ConstString.page_rotation(1): (
                "range",
                Angle.deg(0.69),
                Angle.deg(0.81),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(0.69),
                Angle.deg(0.81),
            ),
            ConstString.image_crop(1, "x1"): ("range", 322, 324),
            ConstString.image_crop(1, "y1"): ("range", 197, 199),
            ConstString.image_crop(1, "x2"): ("range", 2351, 2353),
            ConstString.image_crop(1, "y2"): ("range", 3394, 3395),
            ConstString.image_crop(2, "x1"): ("range", 133, 139),
            ConstString.image_crop(2, "y1"): ("range", 223, 224),
            ConstString.image_crop(2, "x2"): ("range", 2161, 2168),
            ConstString.image_crop(2, "y2"): ("range", 3418, 3419),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 174, 178),
            ConstString.image_border(1, 2): ("range", 114, 115),
            ConstString.image_border(1, 3): ("range", 215, 215),
            ConstString.image_border(1, 4): ("range", 215, 215),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 191, 196),
            ConstString.image_border(2, 2): ("range", 95, 102),
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
                Angle.deg(90.41),
                Angle.deg(90.45),
            ),
            ConstString.separation_double_page_y(): ("range", 2495, 2498),
            ConstString.page_rotation(1): (
                "range",
                Angle.deg(0.29),
                Angle.deg(0.36),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(0.89),
                Angle.deg(0.96),
            ),
            ConstString.image_crop(1, "x1"): ("range", 331, 331),
            ConstString.image_crop(1, "y1"): ("range", 164, 165),
            ConstString.image_crop(1, "x2"): ("range", 2375, 2375),
            ConstString.image_crop(1, "y2"): ("range", 3376, 3377),
            ConstString.image_crop(2, "x1"): ("range", 102, 104),
            ConstString.image_crop(2, "y1"): ("range", 208, 209),
            ConstString.image_crop(2, "x2"): ("range", 2133, 2135),
            ConstString.image_crop(2, "y2"): ("range", 3413, 3413),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 148, 150),
            ConstString.image_border(1, 2): ("range", 125, 128),
            ConstString.image_border(1, 3): ("range", 208, 208),
            ConstString.image_border(1, 4): ("range", 208, 208),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 187, 191),
            ConstString.image_border(2, 2): ("range", 91, 95),
            ConstString.image_border(2, 3): ("range", 214, 215),
            ConstString.image_border(2, 4): ("range", 214, 215),
        },
    )


@pytest.mark.skip(reason="Need to work on crop data")
def test_wrong_wave_split_line_png() -> None:
    """The split line by wave method was wrong."""
    treat_file(
        MockDisableSeparatePage(MAX_VAL),
        get_absolute_from_current_path(__file__, "wrong_wave_split_line.png"),
        {
            ConstString.separation_double_page_angle(): (
                "range",
                Angle.deg(90.42),
                Angle.deg(90.54),
            ),
            ConstString.separation_double_page_y(): ("range", 2502, 2503),
            ConstString.page_rotation(1): (
                "range",
                Angle.deg(-0.16),
                Angle.deg(-0.14),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(0.84),
                Angle.deg(0.86),
            ),
            ConstString.image_crop(1, "x1"): ("range", 385, 385),
            ConstString.image_crop(1, "y1"): ("range", 179, 179),
            ConstString.image_crop(1, "x2"): ("range", 2411, 2411),
            ConstString.image_crop(1, "y2"): ("range", 3374, 3374),
            ConstString.image_crop(2, "x1"): ("range", 27, 124),
            ConstString.image_crop(2, "y1"): ("range", 1, 58),
            ConstString.image_crop(2, "x2"): ("range", 2410, 2489),
            ConstString.image_crop(2, "y2"): ("range", 3392, 3505),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 167, 169),
            ConstString.image_border(1, 2): ("range", 123, 124),
            ConstString.image_border(1, 3): ("range", 217, 217),
            ConstString.image_border(1, 4): ("range", 217, 217),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 0, 2),
            ConstString.image_border(2, 2): ("range", 2, 163),
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
                Angle.deg(-0.14),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(-0.46),
                Angle.deg(-0.44),
            ),
            ConstString.image_crop(1, "x1"): ("range", 205, 205),
            ConstString.image_crop(1, "y1"): ("range", 158, 158),
            ConstString.image_crop(1, "x2"): ("range", 2320, 2320),
            ConstString.image_crop(1, "y2"): ("range", 3366, 3366),
            ConstString.image_crop(2, "x1"): ("range", 185, 185),
            ConstString.image_crop(2, "y1"): ("range", 221, 221),
            ConstString.image_crop(2, "x2"): ("range", 2201, 2201),
            ConstString.image_crop(2, "y2"): ("range", 3366, 3366),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 137, 141),
            ConstString.image_border(1, 2): ("range", 138, 142),
            ConstString.image_border(1, 3): ("range", 172, 172),
            ConstString.image_border(1, 4): ("range", 172, 172),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 215, 225),
            ConstString.image_border(2, 2): ("range", 117, 127),
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
                Angle.deg(90.01),
                Angle.deg(90.02),
            ),
            ConstString.separation_double_page_y(): ("range", 2573, 2576),
            ConstString.page_rotation(1): (
                "range",
                Angle.deg(-0.16),
                Angle.deg(-0.14),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(-0.01),
                Angle.deg(0.06),
            ),
            ConstString.image_crop(1, "x1"): ("range", 407, 407),
            ConstString.image_crop(1, "y1"): ("range", 2925, 2925),
            ConstString.image_crop(1, "x2"): ("range", 2419, 2419),
            ConstString.image_crop(1, "y2"): ("range", 3174, 3174),
            ConstString.image_crop(2, "x1"): ("range", 1180, 1185),
            ConstString.image_crop(2, "y1"): ("range", 1724, 1747),
            ConstString.image_crop(2, "x2"): ("range", 1181, 1186),
            ConstString.image_crop(2, "y2"): ("range", 1725, 1748),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 2917, 2930),
            ConstString.image_border(1, 2): ("range", 308, 321),
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
            ConstString.separation_double_page_y(): ("range", 2497, 2499),
            ConstString.page_rotation(1): (
                "range",
                Angle.deg(-0.01),
                Angle.deg(0.01),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(0.59),
                Angle.deg(0.61),
            ),
            ConstString.image_crop(1, "x1"): ("range", 272, 272),
            ConstString.image_crop(1, "y1"): ("range", 149, 149),
            ConstString.image_crop(1, "x2"): ("range", 2383, 2383),
            ConstString.image_crop(1, "y2"): ("range", 3353, 3353),
            ConstString.image_crop(2, "x1"): ("range", 107, 124),
            ConstString.image_crop(2, "y1"): ("range", 155, 155),
            ConstString.image_crop(2, "x2"): ("range", 2230, 2247),
            ConstString.image_crop(2, "y2"): ("range", 3350, 3350),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 137, 139),
            ConstString.image_border(1, 2): ("range", 144, 146),
            ConstString.image_border(1, 3): ("range", 174, 174),
            ConstString.image_border(1, 4): ("range", 174, 174),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 136, 146),
            ConstString.image_border(2, 2): ("range", 145, 156),
            ConstString.image_border(2, 3): ("range", 168, 168),
            ConstString.image_border(2, 4): ("range", 168, 168),
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
                Angle.deg(89.52),
                Angle.deg(89.56),
            ),
            ConstString.separation_double_page_y(): ("range", 2497, 2499),
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
            ConstString.image_crop(2, "x1"): ("range", 167, 169),
            ConstString.image_crop(2, "y1"): ("range", 228, 228),
            ConstString.image_crop(2, "x2"): ("range", 2180, 2182),
            ConstString.image_crop(2, "y2"): ("range", 3417, 3417),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 237, 239),
            ConstString.image_border(1, 2): ("range", 48, 50),
            ConstString.image_border(1, 3): ("range", 223, 224),
            ConstString.image_border(1, 4): ("range", 223, 224),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 192, 208),
            ConstString.image_border(2, 2): ("range", 90, 106),
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
                Angle.deg(0.39),
                Angle.deg(0.41),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(1.79),
                Angle.deg(1.81),
            ),
            ConstString.image_crop(1, "x1"): ("range", 224, 224),
            ConstString.image_crop(1, "y1"): ("range", 147, 147),
            ConstString.image_crop(1, "x2"): ("range", 2337, 2337),
            ConstString.image_crop(1, "y2"): ("range", 3355, 3355),
            ConstString.image_crop(2, "x1"): ("range", 72, 107),
            ConstString.image_crop(2, "y1"): ("range", 197, 197),
            ConstString.image_crop(2, "x2"): ("range", 2194, 2229),
            ConstString.image_crop(2, "y2"): ("range", 3396, 3396),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 126, 133),
            ConstString.image_border(1, 2): ("range", 146, 153),
            ConstString.image_border(1, 3): ("range", 173, 173),
            ConstString.image_border(1, 4): ("range", 173, 173),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 167, 170),
            ConstString.image_border(2, 2): ("range", 118, 121),
            ConstString.image_border(2, 3): ("range", 169, 169),
            ConstString.image_border(2, 4): ("range", 169, 169),
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
                Angle.deg(0.04),
                Angle.deg(0.11),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(0.29),
                Angle.deg(0.36),
            ),
            ConstString.image_crop(1, "x1"): ("range", 272, 273),
            ConstString.image_crop(1, "y1"): ("range", 219, 220),
            ConstString.image_crop(1, "x2"): ("range", 2383, 2383),
            ConstString.image_crop(1, "y2"): ("range", 3423, 3423),
            ConstString.image_crop(2, "x1"): ("range", 114, 119),
            ConstString.image_crop(2, "y1"): ("range", 226, 226),
            ConstString.image_crop(2, "x2"): ("range", 2235, 2240),
            ConstString.image_crop(2, "y2"): ("range", 3413, 3414),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 190, 202),
            ConstString.image_border(1, 2): ("range", 81, 93),
            ConstString.image_border(1, 3): ("range", 174, 175),
            ConstString.image_border(1, 4): ("range", 174, 175),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 190, 204),
            ConstString.image_border(2, 2): ("range", 96, 110),
            ConstString.image_border(2, 3): ("range", 168, 169),
            ConstString.image_border(2, 4): ("range", 168, 169),
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
                Angle.deg(89.84),
                Angle.deg(89.94),
            ),
            ConstString.separation_double_page_y(): ("range", 2482, 2484),
            ConstString.page_rotation(1): (
                "range",
                Angle.deg(-0.01),
                Angle.deg(0.01),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(-0.56),
                Angle.deg(-0.49),
            ),
            ConstString.image_crop(1, "x1"): ("range", 97, 97),
            ConstString.image_crop(1, "y1"): ("range", 27, 77),
            ConstString.image_crop(1, "x2"): ("range", 2483, 2486),
            ConstString.image_crop(1, "y2"): ("range", 3505, 3505),
            ConstString.image_crop(2, "x1"): ("range", 163, 164),
            ConstString.image_crop(2, "y1"): ("range", 266, 266),
            ConstString.image_crop(2, "x2"): ("range", 2238, 2241),
            ConstString.image_crop(2, "y2"): ("range", 3381, 3382),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 15, 40),
            ConstString.image_border(1, 2): ("range", 15, 40),
            ConstString.image_border(1, 3): ("range", 46, 47),
            ConstString.image_border(1, 4): ("range", 46, 47),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 254, 255),
            ConstString.image_border(2, 2): ("range", 116, 118),
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
                Angle.deg(90.49),
                Angle.deg(91.22),
            ),
            ConstString.separation_double_page_y(): ("range", 2478, 2488),
            ConstString.page_rotation(1): (
                "range",
                Angle.deg(1.09),
                Angle.deg(1.16),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(0.19),
                Angle.deg(0.21),
            ),
            ConstString.image_crop(1, "x1"): ("range", 266, 266),
            ConstString.image_crop(1, "y1"): ("range", 209, 210),
            ConstString.image_crop(1, "x2"): ("range", 2342, 2342),
            ConstString.image_crop(1, "y2"): ("range", 3413, 3413),
            ConstString.image_crop(2, "x1"): ("range", 165, 199),
            ConstString.image_crop(2, "y1"): ("range", 241, 241),
            ConstString.image_crop(2, "x2"): ("range", 2248, 2282),
            ConstString.image_crop(2, "y2"): ("range", 3433, 3433),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 180, 194),
            ConstString.image_border(1, 2): ("range", 90, 103),
            ConstString.image_border(1, 3): ("range", 192, 192),
            ConstString.image_border(1, 4): ("range", 192, 192),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 209, 226),
            ConstString.image_border(2, 2): ("range", 69, 86),
            ConstString.image_border(2, 3): ("range", 188, 188),
            ConstString.image_border(2, 4): ("range", 188, 188),
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
                Angle.deg(1.19),
                Angle.deg(1.21),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(-0.11),
                Angle.deg(-0.04),
            ),
            ConstString.image_crop(1, "x1"): ("range", 287, 287),
            ConstString.image_crop(1, "y1"): ("range", 165, 165),
            ConstString.image_crop(1, "x2"): ("range", 2398, 2398),
            ConstString.image_crop(1, "y2"): ("range", 3368, 3368),
            ConstString.image_crop(2, "x1"): ("range", 145, 151),
            ConstString.image_crop(2, "y1"): ("range", 175, 189),
            ConstString.image_crop(2, "x2"): ("range", 2271, 2275),
            ConstString.image_crop(2, "y2"): ("range", 3373, 3386),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 139, 157),
            ConstString.image_border(1, 2): ("range", 127, 145),
            ConstString.image_border(1, 3): ("range", 174, 174),
            ConstString.image_border(1, 4): ("range", 174, 174),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 175, 180),
            ConstString.image_border(2, 2): ("range", 109, 114),
            ConstString.image_border(2, 3): ("range", 167, 168),
            ConstString.image_border(2, 4): ("range", 167, 168),
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
                Angle.deg(0.19),
                Angle.deg(0.21),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(0.19),
                Angle.deg(0.21),
            ),
            ConstString.image_crop(1, "x1"): ("range", 257, 257),
            ConstString.image_crop(1, "y1"): ("range", 201, 201),
            ConstString.image_crop(1, "x2"): ("range", 2333, 2333),
            ConstString.image_crop(1, "y2"): ("range", 3402, 3402),
            ConstString.image_crop(2, "x1"): ("range", 136, 139),
            ConstString.image_crop(2, "y1"): ("range", 215, 215),
            ConstString.image_crop(2, "x2"): ("range", 2219, 2222),
            ConstString.image_crop(2, "y2"): ("range", 3406, 3406),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 188, 188),
            ConstString.image_border(1, 2): ("range", 97, 98),
            ConstString.image_border(1, 3): ("range", 192, 192),
            ConstString.image_border(1, 4): ("range", 192, 192),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 200, 201),
            ConstString.image_border(2, 2): ("range", 95, 95),
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
                Angle.deg(90.01),
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
                Angle.deg(90.16),
                Angle.deg(90.21),
            ),
            ConstString.separation_double_page_y(): ("range", 2403, 2408),
            ConstString.page_rotation(1): (
                "range",
                Angle.deg(-0.01),
                Angle.deg(0.16),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(-0.01),
                Angle.deg(0.16),
            ),
            ConstString.image_crop(1, "x1"): ("range", 184, 188),
            ConstString.image_crop(1, "y1"): ("range", 2957, 2959),
            ConstString.image_crop(1, "x2"): ("range", 2201, 2205),
            ConstString.image_crop(1, "y2"): ("range", 3201, 3202),
            ConstString.image_crop(2, "x1"): ("range", 0, 0),
            ConstString.image_crop(2, "y1"): ("range", 0, 0),
            ConstString.image_crop(2, "x2"): ("range", 0, 0),
            ConstString.image_crop(2, "y2"): ("range", 0, 0),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 2950, 2956),
            ConstString.image_border(1, 2): ("range", 289, 292),
            ConstString.image_border(1, 3): ("range", 221, 221),
            ConstString.image_border(1, 4): ("range", 221, 221),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 0, 0),
            ConstString.image_border(2, 2): ("range", 0, 0),
            ConstString.image_border(2, 3): ("range", 0, 0),
            ConstString.image_border(2, 4): ("range", 0, 0),
        },
    )
