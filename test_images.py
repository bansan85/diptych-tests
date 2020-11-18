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
            ConstString.image_border(1, 1): ("range", 324, 326),
            ConstString.image_border(1, 2): ("range", 275, 276),
            ConstString.image_border(1, 3): ("range", 223, 225),
            ConstString.image_border(1, 4): ("range", 223, 225),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 671, 674),
            ConstString.image_border(2, 2): ("range", 101, 104),
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
                90.08,
                90.32,
            ),
            ConstString.separation_double_page_y(): ("range", 2486, 2489),
            ConstString.page_rotation(1): ("range", -0.01, 0.11),
            ConstString.page_rotation(2): ("range", 0.19, 0.41),
            ConstString.image_crop(1, "x1"): ("range", 1181, 1186),
            ConstString.image_crop(1, "y1"): ("range", 1719, 1722),
            ConstString.image_crop(1, "x2"): ("range", 1182, 1187),
            ConstString.image_crop(1, "y2"): ("range", 1720, 1723),
            ConstString.image_crop(2, "x1"): ("range", 99, 114),
            ConstString.image_crop(2, "y1"): ("range", 240, 241),
            ConstString.image_crop(2, "x2"): ("range", 2144, 2159),
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
            ConstString.separation_double_page_y(): ("range", 2451, 2455),
            ConstString.page_rotation(1): ("range", -0.01, 0.06),
            ConstString.page_rotation(2): ("range", -0.21, 0.01),
            ConstString.image_crop(1, "x1"): ("range", 297, 299),
            ConstString.image_crop(1, "y1"): ("range", 142, 144),
            ConstString.image_crop(1, "x2"): ("range", 2307, 2309),
            ConstString.image_crop(1, "y2"): ("range", 3346, 3347),
            ConstString.image_crop(2, "x1"): ("range", 157, 159),
            ConstString.image_crop(2, "y1"): ("range", 144, 146),
            ConstString.image_crop(2, "x2"): ("range", 2169, 2172),
            ConstString.image_crop(2, "y2"): ("range", 3351, 3353),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 127, 129),
            ConstString.image_border(1, 2): ("range", 155, 157),
            ConstString.image_border(1, 3): ("range", 224, 226),
            ConstString.image_border(1, 4): ("range", 224, 226),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 130, 132),
            ConstString.image_border(2, 2): ("range", 146, 151),
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
                90.14,
                90.50,
            ),
            ConstString.separation_double_page_y(): ("range", 2476, 2487),
            ConstString.page_rotation(1): ("range", 0.29, 0.41),
            ConstString.page_rotation(2): ("range", 0.34, 0.51),
            ConstString.image_crop(1, "x1"): ("range", 34, 91),
            ConstString.image_crop(1, "y1"): ("range", 1, 23),
            ConstString.image_crop(1, "x2"): ("range", 2456, 2481),
            ConstString.image_crop(1, "y2"): ("range", 3483, 3501),
            ConstString.image_crop(2, "x1"): ("range", 170, 183),
            ConstString.image_crop(2, "y1"): ("range", 234, 236),
            ConstString.image_crop(2, "x2"): ("range", 2249, 2261),
            ConstString.image_crop(2, "y2"): ("range", 3354, 3356),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 4, 19),
            ConstString.image_border(1, 2): ("range", 4, 19),
            ConstString.image_border(1, 3): ("range", 20, 55),
            ConstString.image_border(1, 4): ("range", 20, 55),
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
                89.97,
                90.17,
            ),
            ConstString.separation_double_page_y(): ("range", 2479, 2486),
            ConstString.page_rotation(1): ("range", -0.01, 0.21),
            ConstString.page_rotation(2): ("range", -0.01, 0.21),
            ConstString.image_crop(1, "x1"): ("range", 52, 116),
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
            ConstString.image_border(1, 3): ("range", 25, 58),
            ConstString.image_border(1, 4): ("range", 25, 58),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 209, 212),
            ConstString.image_border(2, 2): ("range", 145, 147),
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
                90.13,
                90.22,
            ),
            ConstString.separation_double_page_y(): ("range", 2482, 2487),
            ConstString.page_rotation(1): ("range", -0.01, 0.21),
            ConstString.page_rotation(2): ("range", -0.01, 0.21),
            ConstString.image_crop(1, "x1"): ("range", 53, 61),
            ConstString.image_crop(1, "y1"): ("range", 7, 8),
            ConstString.image_crop(1, "x2"): ("range", 2476, 2482),
            ConstString.image_crop(1, "y2"): ("range", 3500, 3505),
            ConstString.image_crop(2, "x1"): ("range", 159, 165),
            ConstString.image_crop(2, "y1"): ("range", 217, 219),
            ConstString.image_crop(2, "x2"): ("range", 2239, 2248),
            ConstString.image_crop(2, "y2"): ("range", 3348, 3350),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 5, 8),
            ConstString.image_border(1, 2): ("range", 5, 8),
            ConstString.image_border(1, 3): ("range", 26, 31),
            ConstString.image_border(1, 4): ("range", 26, 31),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 195, 208),
            ConstString.image_border(2, 2): ("range", 150, 159),
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
                89.73,
                89.74,
            ),
            ConstString.separation_double_page_y(): ("range", 2471, 2471),
            ConstString.page_rotation(1): ("range", -0.46, -0.44),
            ConstString.page_rotation(2): ("range", 0.19, 0.21),
            ConstString.image_crop(1, "x1"): ("range", 245, 245),
            ConstString.image_crop(1, "y1"): ("range", 161, 161),
            ConstString.image_crop(1, "x2"): ("range", 2351, 2351),
            ConstString.image_crop(1, "y2"): ("range", 3364, 3364),
            ConstString.image_crop(2, "x1"): ("range", 153, 153),
            ConstString.image_crop(2, "y1"): ("range", 147, 147),
            ConstString.image_crop(2, "x2"): ("range", 2260, 2260),
            ConstString.image_crop(2, "y2"): ("range", 3350, 3350),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 131, 131),
            ConstString.image_border(1, 2): ("range", 152, 152),
            ConstString.image_border(1, 3): ("range", 177, 177),
            ConstString.image_border(1, 4): ("range", 177, 177),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 118, 118),
            ConstString.image_border(2, 2): ("range", 166, 166),
            ConstString.image_border(2, 3): ("range", 176, 176),
            ConstString.image_border(2, 4): ("range", 176, 176),
        },
    )
