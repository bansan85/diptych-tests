import unittest

import numpy as np

from diptych.angle import Angle
from diptych.cv2ext import charge_image
from diptych.fsext import get_absolute_from_current_path
from diptych.print_interface import ConstString
from tests.mock_separate_page import MockDisableSeparatePage

np.seterr(all="raise")
tc = unittest.TestCase()


MAX_VAL = 6
FUZZING = False


def test_0001_png() -> None:
    """first good page"""
    MockDisableSeparatePage(MAX_VAL, FUZZING).treat_file(
        get_absolute_from_current_path(__file__, "0001.png"),
        {
            ConstString.separation_double_page_angle(): (
                "range",
                Angle.deg(90.42),
                Angle.deg(90.68),
            ),
            ConstString.separation_double_page_y(): ("range", 2480, 2489),
            ConstString.page_rotation(1): (
                "range",
                Angle.deg(0.49),
                Angle.deg(0.81),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(0.09),
                Angle.deg(0.21),
            ),
            ConstString.image_crop(1, "x1"): ("range", 325, 332),
            ConstString.image_crop(1, "y1"): ("range", 334, 337),
            ConstString.image_crop(1, "x2"): ("range", 2342, 2347),
            ConstString.image_crop(1, "y2"): ("range", 3221, 3223),
            ConstString.image_crop(2, "x1"): ("range", 165, 175),
            ConstString.image_crop(2, "y1"): ("range", 648, 649),
            ConstString.image_crop(2, "x2"): ("range", 2180, 2190),
            ConstString.image_crop(2, "y2"): ("range", 3360, 3362),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 317, 340),
            ConstString.image_border(1, 2): ("range", 260, 282),
            ConstString.image_border(1, 3): ("range", 219, 225),
            ConstString.image_border(1, 4): ("range", 219, 225),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 638, 674),
            ConstString.image_border(2, 2): ("range", 101, 136),
            ConstString.image_border(2, 3): ("range", 221, 224),
            ConstString.image_border(2, 4): ("range", 221, 224),
        },
    )


def test_2_pages_2_contours_png() -> None:
    """There is not one contour for the two pages,
    but one contour for each page.
    """
    MockDisableSeparatePage(MAX_VAL, FUZZING).treat_file(
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
                Angle.deg(-0.11),
                Angle.deg(0.21),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(0.04),
                Angle.deg(0.41),
            ),
            ConstString.image_crop(1, "x1"): ("range", 1181, 1199),
            ConstString.image_crop(1, "y1"): ("range", 1719, 1751),
            ConstString.image_crop(1, "x2"): ("range", 1182, 1200),
            ConstString.image_crop(1, "y2"): ("range", 1720, 1752),
            ConstString.image_crop(2, "x1"): ("range", 89, 114),
            ConstString.image_crop(2, "y1"): ("range", 240, 241),
            ConstString.image_crop(2, "x2"): ("range", 2136, 2159),
            ConstString.image_crop(2, "y2"): ("range", 3239, 3242),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 1752, 1753),
            ConstString.image_border(1, 2): ("range", 1753, 1753),
            ConstString.image_border(1, 3): ("range", 1239, 1239),
            ConstString.image_border(1, 4): ("range", 1239, 1239),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 226, 240),
            ConstString.image_border(2, 2): ("range", 248, 262),
            ConstString.image_border(2, 3): ("range", 203, 207),
            ConstString.image_border(2, 4): ("range", 203, 207),
        },
    )


def test_black_border_not_removed_png() -> None:
    """The border on the right is still there."""
    MockDisableSeparatePage(MAX_VAL, FUZZING).treat_file(
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
                Angle.deg(-0.11),
                Angle.deg(0.21),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(-0.21),
                Angle.deg(0.16),
            ),
            ConstString.image_crop(1, "x1"): ("range", 294, 299),
            ConstString.image_crop(1, "y1"): ("range", 139, 144),
            ConstString.image_crop(1, "x2"): ("range", 2305, 2312),
            ConstString.image_crop(1, "y2"): ("range", 3345, 3349),
            ConstString.image_crop(2, "x1"): ("range", 153, 159),
            ConstString.image_crop(2, "y1"): ("range", 143, 146),
            ConstString.image_crop(2, "x2"): ("range", 2168, 2173),
            ConstString.image_crop(2, "y2"): ("range", 3350, 3353),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 127, 137),
            ConstString.image_border(1, 2): ("range", 145, 157),
            ConstString.image_border(1, 3): ("range", 221, 226),
            ConstString.image_border(1, 4): ("range", 221, 226),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 130, 139),
            ConstString.image_border(2, 2): ("range", 141, 151),
            ConstString.image_border(2, 3): ("range", 222, 224),
            ConstString.image_border(2, 4): ("range", 222, 224),
        },
    )


def test_image_failed_to_rotate_png() -> None:
    """Failed to compute angle to rotate. The image takes the whole page."""
    MockDisableSeparatePage(MAX_VAL, FUZZING).treat_file(
        get_absolute_from_current_path(__file__, "image_failed_to_rotate.png"),
        {
            ConstString.separation_double_page_angle(): (
                "range",
                Angle.deg(90.07),
                Angle.deg(90.50),
            ),
            ConstString.separation_double_page_y(): ("range", 2476, 2488),
            ConstString.page_rotation(1): (
                "range",
                Angle.deg(-0.01),
                Angle.deg(0.66),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(0.19),
                Angle.deg(0.51),
            ),
            ConstString.image_crop(1, "x1"): ("range", 19, 91),
            ConstString.image_crop(1, "y1"): ("range", 1, 23),
            ConstString.image_crop(1, "x2"): ("range", 2456, 2486),
            ConstString.image_crop(1, "y2"): ("range", 3483, 3505),
            ConstString.image_crop(2, "x1"): ("range", 159, 183),
            ConstString.image_crop(2, "y1"): ("range", 231, 236),
            ConstString.image_crop(2, "x2"): ("range", 2242, 2261),
            ConstString.image_crop(2, "y2"): ("range", 3354, 3359),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 2, 19),
            ConstString.image_border(1, 2): ("range", 2, 19),
            ConstString.image_border(1, 3): ("range", 10, 55),
            ConstString.image_border(1, 4): ("range", 10, 55),
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
    MockDisableSeparatePage(MAX_VAL, FUZZING).treat_file(
        get_absolute_from_current_path(
            __file__, "image_failed_to_crop_data.png"
        ),
        {
            ConstString.separation_double_page_angle(): (
                "range",
                Angle.deg(89.86),
                Angle.deg(90.20),
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
            ConstString.image_crop(1, "x1"): ("range", 40, 116),
            ConstString.image_crop(1, "y1"): ("range", 1, 13),
            ConstString.image_crop(1, "x2"): ("range", 2469, 2483),
            ConstString.image_crop(1, "y2"): ("range", 3499, 3505),
            ConstString.image_crop(2, "x1"): ("range", 155, 168),
            ConstString.image_crop(2, "y1"): ("range", 217, 220),
            ConstString.image_crop(2, "x2"): ("range", 2235, 2248),
            ConstString.image_crop(2, "y2"): ("range", 3348, 3350),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 2, 11),
            ConstString.image_border(1, 2): ("range", 2, 11),
            ConstString.image_border(1, 3): ("range", 19, 58),
            ConstString.image_border(1, 4): ("range", 19, 58),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 205, 225),
            ConstString.image_border(2, 2): ("range", 129, 151),
            ConstString.image_border(2, 3): ("range", 189, 192),
            ConstString.image_border(2, 4): ("range", 189, 192),
        },
    )


def test_wrong_angle_split_line_png() -> None:
    """Failed to detect edges. The image takes the whole page and is too closed
    to the border of the image.
    """
    MockDisableSeparatePage(MAX_VAL, FUZZING).treat_file(
        get_absolute_from_current_path(__file__, "wrong_angle_split_line.png"),
        {
            ConstString.separation_double_page_angle(): (
                "range",
                Angle.deg(90.00),
                Angle.deg(90.22),
            ),
            ConstString.separation_double_page_y(): ("range", 2476, 2487),
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
            ConstString.image_crop(1, "x1"): ("range", 28, 61),
            ConstString.image_crop(1, "y1"): ("range", 1, 10),
            ConstString.image_crop(1, "x2"): ("range", 2470, 2485),
            ConstString.image_crop(1, "y2"): ("range", 3500, 3505),
            ConstString.image_crop(2, "x1"): ("range", 154, 171),
            ConstString.image_crop(2, "y1"): ("range", 217, 219),
            ConstString.image_crop(2, "x2"): ("range", 2237, 2249),
            ConstString.image_crop(2, "y2"): ("range", 3348, 3350),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 2, 8),
            ConstString.image_border(1, 2): ("range", 2, 8),
            ConstString.image_border(1, 3): ("range", 15, 34),
            ConstString.image_border(1, 4): ("range", 15, 34),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 195, 219),
            ConstString.image_border(2, 2): ("range", 136, 159),
            ConstString.image_border(2, 3): ("range", 188, 192),
            ConstString.image_border(2, 4): ("range", 188, 192),
        },
    )
    tc.assertEqual(
        charge_image(
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
    MockDisableSeparatePage(MAX_VAL, FUZZING).treat_file(
        get_absolute_from_current_path(
            __file__, "angle_page_lower_split_line.png"
        ),
        {
            ConstString.separation_double_page_angle(): (
                "range",
                Angle.deg(89.71),
                Angle.deg(89.81),
            ),
            ConstString.separation_double_page_y(): ("range", 2470, 2475),
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
            ConstString.image_crop(2, "x1"): ("range", 136, 154),
            ConstString.image_crop(2, "y1"): ("range", 145, 147),
            ConstString.image_crop(2, "x2"): ("range", 2243, 2264),
            ConstString.image_crop(2, "y2"): ("range", 3350, 3352),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 130, 147),
            ConstString.image_border(1, 2): ("range", 135, 152),
            ConstString.image_border(1, 3): ("range", 172, 177),
            ConstString.image_border(1, 4): ("range", 172, 177),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 116, 132),
            ConstString.image_border(2, 2): ("range", 151, 168),
            ConstString.image_border(2, 3): ("range", 174, 176),
            ConstString.image_border(2, 4): ("range", 174, 176),
        },
    )


def test_wrong_split_line_png() -> None:
    """Improve choice of the split line between different algorithm."""
    MockDisableSeparatePage(MAX_VAL, FUZZING).treat_file(
        get_absolute_from_current_path(__file__, "wrong_split_line.png"),
        {
            ConstString.separation_double_page_angle(): (
                "range",
                Angle.deg(89.80),
                Angle.deg(89.99),
            ),
            ConstString.separation_double_page_y(): ("range", 2461, 2471),
            ConstString.page_rotation(1): (
                "range",
                Angle.deg(-0.16),
                Angle.deg(0.01),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(0.19),
                Angle.deg(0.71),
            ),
            ConstString.image_crop(1, "x1"): ("range", 211, 213),
            ConstString.image_crop(1, "y1"): ("range", 155, 157),
            ConstString.image_crop(1, "x2"): ("range", 2322, 2324),
            ConstString.image_crop(1, "y2"): ("range", 3362, 3363),
            ConstString.image_crop(2, "x1"): ("range", 115, 129),
            ConstString.image_crop(2, "y1"): ("range", 160, 167),
            ConstString.image_crop(2, "x2"): ("range", 2230, 2243),
            ConstString.image_crop(2, "y2"): ("range", 3371, 3378),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 115, 180),
            ConstString.image_border(1, 2): ("range", 100, 167),
            ConstString.image_border(1, 3): ("range", 173, 175),
            ConstString.image_border(1, 4): ("range", 173, 175),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 129, 148),
            ConstString.image_border(2, 2): ("range", 129, 152),
            ConstString.image_border(2, 3): ("range", 168, 174),
            ConstString.image_border(2, 4): ("range", 168, 174),
        },
    )


def test_crop_too_much_png() -> None:
    """Reduce distance to ignore black area closed to the edge."""
    MockDisableSeparatePage(MAX_VAL, FUZZING).treat_file(
        get_absolute_from_current_path(__file__, "crop_too_much.png"),
        {
            ConstString.separation_double_page_angle(): (
                "range",
                Angle.deg(90.03),
                Angle.deg(90.47),
            ),
            ConstString.separation_double_page_y(): ("range", 2452, 2463),
            ConstString.page_rotation(1): (
                "range",
                Angle.deg(-0.16),
                Angle.deg(0.16),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(0.19),
                Angle.deg(0.51),
            ),
            ConstString.image_crop(1, "x1"): ("range", 300, 303),
            ConstString.image_crop(1, "y1"): ("range", 145, 148),
            ConstString.image_crop(1, "x2"): ("range", 2313, 2317),
            ConstString.image_crop(1, "y2"): ("range", 3350, 3353),
            ConstString.image_crop(2, "x1"): ("range", 158, 180),
            ConstString.image_crop(2, "y1"): ("range", 151, 156),
            ConstString.image_crop(2, "x2"): ("range", 2176, 2192),
            ConstString.image_crop(2, "y2"): ("range", 3359, 3363),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 116, 135),
            ConstString.image_border(1, 2): ("range", 147, 168),
            ConstString.image_border(1, 3): ("range", 221, 225),
            ConstString.image_border(1, 4): ("range", 221, 225),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 95, 142),
            ConstString.image_border(2, 2): ("range", 140, 186),
            ConstString.image_border(2, 3): ("range", 218, 224),
            ConstString.image_border(2, 4): ("range", 218, 224),
        },
    )


def test_crop_too_few_png() -> None:
    """Improve detection of black area to ignored
    and that are closed to the edge.
    """
    MockDisableSeparatePage(MAX_VAL, FUZZING).treat_file(
        get_absolute_from_current_path(__file__, "crop_too_few.png"),
        {
            ConstString.separation_double_page_angle(): (
                "range",
                Angle.deg(89.22),
                Angle.deg(89.62),
            ),
            ConstString.separation_double_page_y(): ("range", 2508, 2515),
            ConstString.page_rotation(1): (
                "range",
                Angle.deg(-0.81),
                Angle.deg(-0.49),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(-0.16),
                Angle.deg(0.16),
            ),
            ConstString.image_crop(1, "x1"): ("range", 261, 265),
            ConstString.image_crop(1, "y1"): ("range", 148, 161),
            ConstString.image_crop(1, "x2"): ("range", 2375, 2381),
            ConstString.image_crop(1, "y2"): ("range", 3356, 3359),
            ConstString.image_crop(2, "x1"): ("range", 130, 141),
            ConstString.image_crop(2, "y1"): ("range", 138, 141),
            ConstString.image_crop(2, "x2"): ("range", 2256, 2263),
            ConstString.image_crop(2, "y2"): ("range", 3343, 3347),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 84, 137),
            ConstString.image_border(1, 2): ("range", 141, 208),
            ConstString.image_border(1, 3): ("range", 170, 175),
            ConstString.image_border(1, 4): ("range", 170, 175),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 126, 143),
            ConstString.image_border(2, 2): ("range", 140, 158),
            ConstString.image_border(2, 3): ("range", 166, 169),
            ConstString.image_border(2, 4): ("range", 166, 169),
        },
    )


def test_crop_too_much_2_png() -> None:
    """Reduce distance to ignore black area closed to the edge."""
    MockDisableSeparatePage(MAX_VAL, FUZZING).treat_file(
        get_absolute_from_current_path(__file__, "crop_too_much_2.png"),
        {
            ConstString.separation_double_page_angle(): (
                "range",
                Angle.deg(90.08),
                Angle.deg(90.29),
            ),
            ConstString.separation_double_page_y(): ("range", 2475, 2482),
            ConstString.page_rotation(1): (
                "range",
                Angle.deg(0.04),
                Angle.deg(0.21),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(0.04),
                Angle.deg(0.21),
            ),
            ConstString.image_crop(1, "x1"): ("range", 328, 332),
            ConstString.image_crop(1, "y1"): ("range", 131, 134),
            ConstString.image_crop(1, "x2"): ("range", 2342, 2345),
            ConstString.image_crop(1, "y2"): ("range", 3334, 3336),
            ConstString.image_crop(2, "x1"): ("range", 159, 170),
            ConstString.image_crop(2, "y1"): ("range", 137, 139),
            ConstString.image_crop(2, "x2"): ("range", 2175, 2183),
            ConstString.image_crop(2, "y2"): ("range", 3345, 3347),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 112, 127),
            ConstString.image_border(1, 2): ("range", 157, 170),
            ConstString.image_border(1, 3): ("range", 221, 225),
            ConstString.image_border(1, 4): ("range", 221, 225),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 123, 133),
            ConstString.image_border(2, 2): ("range", 148, 157),
            ConstString.image_border(2, 3): ("range", 219, 223),
            ConstString.image_border(2, 4): ("range", 219, 223),
        },
    )


def test_wrong_split_line_2_png() -> None:
    """Improve choice of the split line between different algorithm."""
    MockDisableSeparatePage(MAX_VAL, FUZZING).treat_file(
        get_absolute_from_current_path(__file__, "wrong_split_line_2.png"),
        {
            ConstString.separation_double_page_angle(): (
                "range",
                Angle.deg(90.15),
                Angle.deg(90.40),
            ),
            ConstString.separation_double_page_y(): ("range", 2435, 2442),
            ConstString.page_rotation(1): (
                "range",
                Angle.deg(-0.01),
                Angle.deg(0.21),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(0.19),
                Angle.deg(0.41),
            ),
            ConstString.image_crop(1, "x1"): ("range", 294, 294),
            ConstString.image_crop(1, "y1"): ("range", 136, 138),
            ConstString.image_crop(1, "x2"): ("range", 2324, 2327),
            ConstString.image_crop(1, "y2"): ("range", 3374, 3376),
            ConstString.image_crop(2, "x1"): ("range", 135, 146),
            ConstString.image_crop(2, "y1"): ("range", 190, 193),
            ConstString.image_crop(2, "x2"): ("range", 2165, 2175),
            ConstString.image_crop(2, "y2"): ("range", 3386, 3389),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 121, 131),
            ConstString.image_border(1, 2): ("range", 116, 126),
            ConstString.image_border(1, 3): ("range", 213, 215),
            ConstString.image_border(1, 4): ("range", 213, 215),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 180, 185),
            ConstString.image_border(2, 2): ("range", 105, 111),
            ConstString.image_border(2, 3): ("range", 212, 216),
            ConstString.image_border(2, 4): ("range", 212, 216),
        },
    )


def test_small_wave_png() -> None:
    """The wave at the bottom of the image is very small."""
    MockDisableSeparatePage(MAX_VAL, FUZZING).treat_file(
        get_absolute_from_current_path(__file__, "small_wave.png"),
        {
            ConstString.separation_double_page_angle(): (
                "range",
                Angle.deg(90.51),
                Angle.deg(90.70),
            ),
            ConstString.separation_double_page_y(): ("range", 2491, 2500),
            ConstString.page_rotation(1): (
                "range",
                Angle.deg(0.49),
                Angle.deg(0.81),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(0.54),
                Angle.deg(0.86),
            ),
            ConstString.image_crop(1, "x1"): ("range", 316, 324),
            ConstString.image_crop(1, "y1"): ("range", 197, 199),
            ConstString.image_crop(1, "x2"): ("range", 2351, 2356),
            ConstString.image_crop(1, "y2"): ("range", 3392, 3395),
            ConstString.image_crop(2, "x1"): ("range", 127, 139),
            ConstString.image_crop(2, "y1"): ("range", 220, 224),
            ConstString.image_crop(2, "x2"): ("range", 2158, 2168),
            ConstString.image_crop(2, "y2"): ("range", 3417, 3421),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 174, 182),
            ConstString.image_border(1, 2): ("range", 110, 117),
            ConstString.image_border(1, 3): ("range", 210, 215),
            ConstString.image_border(1, 4): ("range", 210, 215),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 191, 203),
            ConstString.image_border(2, 2): ("range", 83, 102),
            ConstString.image_border(2, 3): ("range", 211, 216),
            ConstString.image_border(2, 4): ("range", 211, 216),
        },
    )


def test_wrong_split_line_3_png() -> None:
    """The split line was not the right one."""
    MockDisableSeparatePage(MAX_VAL, FUZZING).treat_file(
        get_absolute_from_current_path(__file__, "wrong_split_line_3.png"),
        {
            ConstString.separation_double_page_angle(): (
                "range",
                Angle.deg(90.36),
                Angle.deg(90.69),
            ),
            ConstString.separation_double_page_y(): ("range", 2494, 2504),
            ConstString.page_rotation(1): (
                "range",
                Angle.deg(0.14),
                Angle.deg(0.41),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(0.64),
                Angle.deg(1.01),
            ),
            ConstString.image_crop(1, "x1"): ("range", 331, 331),
            ConstString.image_crop(1, "y1"): ("range", 163, 166),
            ConstString.image_crop(1, "x2"): ("range", 2375, 2379),
            ConstString.image_crop(1, "y2"): ("range", 3375, 3377),
            ConstString.image_crop(2, "x1"): ("range", 96, 113),
            ConstString.image_crop(2, "y1"): ("range", 203, 210),
            ConstString.image_crop(2, "x2"): ("range", 2130, 2144),
            ConstString.image_crop(2, "y2"): ("range", 3412, 3416),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 148, 161),
            ConstString.image_border(1, 2): ("range", 114, 128),
            ConstString.image_border(1, 3): ("range", 206, 208),
            ConstString.image_border(1, 4): ("range", 206, 208),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 183, 201),
            ConstString.image_border(2, 2): ("range", 80, 95),
            ConstString.image_border(2, 3): ("range", 208, 215),
            ConstString.image_border(2, 4): ("range", 208, 215),
        },
    )


def test_wrong_wave_split_line_png() -> None:
    """The split line by wave method was wrong."""
    MockDisableSeparatePage(MAX_VAL, FUZZING).treat_file(
        get_absolute_from_current_path(__file__, "wrong_wave_split_line.png"),
        {
            ConstString.separation_double_page_angle(): (
                "range",
                Angle.deg(90.36),
                Angle.deg(90.54),
            ),
            ConstString.separation_double_page_y(): ("range", 2499, 2505),
            ConstString.page_rotation(1): (
                "range",
                Angle.deg(-0.16),
                Angle.deg(0.01),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(0.74),
                Angle.deg(0.91),
            ),
            ConstString.image_crop(1, "x1"): ("range", 383, 385),
            ConstString.image_crop(1, "y1"): ("range", 178, 179),
            ConstString.image_crop(1, "x2"): ("range", 2411, 2412),
            ConstString.image_crop(1, "y2"): ("range", 3374, 3375),
            ConstString.image_crop(2, "x1"): ("range", 0, 124),
            ConstString.image_crop(2, "y1"): ("range", 0, 58),
            ConstString.image_crop(2, "x2"): ("range", 2398, 2489),
            ConstString.image_crop(2, "y2"): ("range", 3391, 3505),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 167, 174),
            ConstString.image_border(1, 2): ("range", 118, 124),
            ConstString.image_border(1, 3): ("range", 215, 217),
            ConstString.image_border(1, 4): ("range", 215, 217),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 0, 11),
            ConstString.image_border(2, 2): ("range", 1, 163),
            ConstString.image_border(2, 3): ("range", 9, 95),
            ConstString.image_border(2, 4): ("range", 9, 95),
        },
    )


def test_no_split_line_line_algo_png() -> None:
    """No line for split line with line detection algo."""
    MockDisableSeparatePage(MAX_VAL, FUZZING).treat_file(
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
                Angle.deg(0.01),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(-0.46),
                Angle.deg(-0.14),
            ),
            ConstString.image_crop(1, "x1"): ("range", 203, 205),
            ConstString.image_crop(1, "y1"): ("range", 156, 158),
            ConstString.image_crop(1, "x2"): ("range", 2320, 2323),
            ConstString.image_crop(1, "y2"): ("range", 3366, 3367),
            ConstString.image_crop(2, "x1"): ("range", 185, 187),
            ConstString.image_crop(2, "y1"): ("range", 221, 225),
            ConstString.image_crop(2, "x2"): ("range", 2200, 2204),
            ConstString.image_crop(2, "y2"): ("range", 3362, 3366),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 137, 145),
            ConstString.image_border(1, 2): ("range", 132, 142),
            ConstString.image_border(1, 3): ("range", 170, 172),
            ConstString.image_border(1, 4): ("range", 170, 172),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 215, 225),
            ConstString.image_border(2, 2): ("range", 117, 132),
            ConstString.image_border(2, 3): ("range", 220, 223),
            ConstString.image_border(2, 4): ("range", 220, 223),
        },
    )


def test_failed_split_line_line_algo_png() -> None:
    """Failed to compute line for split line with line detection alog."""
    MockDisableSeparatePage(MAX_VAL, FUZZING).treat_file(
        get_absolute_from_current_path(
            __file__, "failed_split_line_line_algo.png"
        ),
        {
            ConstString.separation_double_page_angle(): (
                "range",
                Angle.deg(89.96),
                Angle.deg(90.08),
            ),
            ConstString.separation_double_page_y(): ("range", 2573, 2576),
            ConstString.page_rotation(1): (
                "range",
                Angle.deg(-0.16),
                Angle.deg(0.16),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(-0.16),
                Angle.deg(0.21),
            ),
            ConstString.image_crop(1, "x1"): ("range", 407, 414),
            ConstString.image_crop(1, "y1"): ("range", 2925, 2928),
            ConstString.image_crop(1, "x2"): ("range", 2419, 2426),
            ConstString.image_crop(1, "y2"): ("range", 3171, 3174),
            ConstString.image_crop(2, "x1"): ("range", 1180, 1192),
            ConstString.image_crop(2, "y1"): ("range", 1724, 1750),
            ConstString.image_crop(2, "x2"): ("range", 1181, 1193),
            ConstString.image_crop(2, "y2"): ("range", 1725, 1751),
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
    MockDisableSeparatePage(MAX_VAL, FUZZING).treat_file(
        get_absolute_from_current_path(
            __file__, "failed_split_line_line_algo_2.png"
        ),
        {
            ConstString.separation_double_page_angle(): (
                "range",
                Angle.deg(89.97),
                Angle.deg(90.06),
            ),
            ConstString.separation_double_page_y(): ("range", 2497, 2500),
            ConstString.page_rotation(1): (
                "range",
                Angle.deg(-0.16),
                Angle.deg(0.21),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(0.44),
                Angle.deg(0.66),
            ),
            ConstString.image_crop(1, "x1"): ("range", 269, 274),
            ConstString.image_crop(1, "y1"): ("range", 146, 149),
            ConstString.image_crop(1, "x2"): ("range", 2381, 2387),
            ConstString.image_crop(1, "y2"): ("range", 3352, 3355),
            ConstString.image_crop(2, "x1"): ("range", 107, 124),
            ConstString.image_crop(2, "y1"): ("range", 153, 155),
            ConstString.image_crop(2, "x2"): ("range", 2230, 2248),
            ConstString.image_crop(2, "y2"): ("range", 3349, 3352),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 135, 142),
            ConstString.image_border(1, 2): ("range", 138, 146),
            ConstString.image_border(1, 3): ("range", 173, 174),
            ConstString.image_border(1, 4): ("range", 173, 174),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 133, 146),
            ConstString.image_border(2, 2): ("range", 145, 159),
            ConstString.image_border(2, 3): ("range", 166, 169),
            ConstString.image_border(2, 4): ("range", 166, 169),
        },
    )


def test_crop_too_much_3_png() -> None:
    """Failed to compute line for split line with line detection alog."""
    MockDisableSeparatePage(MAX_VAL, FUZZING).treat_file(
        get_absolute_from_current_path(__file__, "crop_too_much_3.png"),
        {
            ConstString.separation_double_page_angle(): (
                "range",
                Angle.deg(89.36),
                Angle.deg(89.75),
            ),
            ConstString.separation_double_page_y(): ("range", 2494, 2504),
            ConstString.page_rotation(1): (
                "range",
                Angle.deg(-1.01),
                Angle.deg(-0.54),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(-0.16),
                Angle.deg(0.01),
            ),
            ConstString.image_crop(1, "x1"): ("range", 368, 375),
            ConstString.image_crop(1, "y1"): ("range", 252, 258),
            ConstString.image_crop(1, "x2"): ("range", 2385, 2394),
            ConstString.image_crop(1, "y2"): ("range", 3458, 3463),
            ConstString.image_crop(2, "x1"): ("range", 162, 172),
            ConstString.image_crop(2, "y1"): ("range", 228, 230),
            ConstString.image_crop(2, "x2"): ("range", 2175, 2186),
            ConstString.image_crop(2, "y2"): ("range", 3415, 3417),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 237, 241),
            ConstString.image_border(1, 2): ("range", 35, 50),
            ConstString.image_border(1, 3): ("range", 217, 224),
            ConstString.image_border(1, 4): ("range", 217, 224),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 192, 215),
            ConstString.image_border(2, 2): ("range", 84, 106),
            ConstString.image_border(2, 3): ("range", 219, 223),
            ConstString.image_border(2, 4): ("range", 219, 223),
        },
    )


def test_wrong_wave_split_line_2_png() -> None:
    """Need to relax tolerance to have the split line by wave algo."""
    MockDisableSeparatePage(MAX_VAL, FUZZING).treat_file(
        get_absolute_from_current_path(
            __file__, "wrong_wave_split_line_2.png"
        ),
        {
            ConstString.separation_double_page_angle(): (
                "range",
                Angle.deg(90.64),
                Angle.deg(91.02),
            ),
            ConstString.separation_double_page_y(): ("range", 2483, 2494),
            ConstString.page_rotation(1): (
                "range",
                Angle.deg(0.19),
                Angle.deg(0.51),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(1.59),
                Angle.deg(1.86),
            ),
            ConstString.image_crop(1, "x1"): ("range", 223, 227),
            ConstString.image_crop(1, "y1"): ("range", 146, 148),
            ConstString.image_crop(1, "x2"): ("range", 2335, 2342),
            ConstString.image_crop(1, "y2"): ("range", 3353, 3356),
            ConstString.image_crop(2, "x1"): ("range", 72, 118),
            ConstString.image_crop(2, "y1"): ("range", 194, 198),
            ConstString.image_crop(2, "x2"): ("range", 2194, 2240),
            ConstString.image_crop(2, "y2"): ("range", 3396, 3399),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 126, 141),
            ConstString.image_border(1, 2): ("range", 138, 153),
            ConstString.image_border(1, 3): ("range", 172, 174),
            ConstString.image_border(1, 4): ("range", 172, 174),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 164, 179),
            ConstString.image_border(2, 2): ("range", 108, 123),
            ConstString.image_border(2, 3): ("range", 167, 169),
            ConstString.image_border(2, 4): ("range", 167, 169),
        },
    )


def test_wrong_wave_split_line_3_png() -> None:
    """Need to relax tolerance to have the split line by wave algo."""
    MockDisableSeparatePage(MAX_VAL, FUZZING).treat_file(
        get_absolute_from_current_path(
            __file__, "wrong_wave_split_line_3.png"
        ),
        {
            ConstString.separation_double_page_angle(): (
                "range",
                Angle.deg(90.00),
                Angle.deg(90.16),
            ),
            ConstString.separation_double_page_y(): ("range", 2510, 2516),
            ConstString.page_rotation(1): (
                "range",
                Angle.deg(-0.01),
                Angle.deg(0.16),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(0.14),
                Angle.deg(0.36),
            ),
            ConstString.image_crop(1, "x1"): ("range", 272, 274),
            ConstString.image_crop(1, "y1"): ("range", 218, 221),
            ConstString.image_crop(1, "x2"): ("range", 2383, 2384),
            ConstString.image_crop(1, "y2"): ("range", 3422, 3424),
            ConstString.image_crop(2, "x1"): ("range", 110, 119),
            ConstString.image_crop(2, "y1"): ("range", 224, 226),
            ConstString.image_crop(2, "x2"): ("range", 2235, 2244),
            ConstString.image_crop(2, "y2"): ("range", 3413, 3415),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 190, 203),
            ConstString.image_border(1, 2): ("range", 79, 93),
            ConstString.image_border(1, 3): ("range", 174, 175),
            ConstString.image_border(1, 4): ("range", 174, 175),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 190, 208),
            ConstString.image_border(2, 2): ("range", 90, 110),
            ConstString.image_border(2, 3): ("range", 165, 169),
            ConstString.image_border(2, 4): ("range", 165, 169),
        },
    )


def test_no_split_line_wave_algo_png() -> None:
    """Failed to detect wave due to image."""
    MockDisableSeparatePage(MAX_VAL, FUZZING).treat_file(
        get_absolute_from_current_path(
            __file__, "no_split_line_wave_algo.png"
        ),
        {
            ConstString.separation_double_page_angle(): (
                "range",
                Angle.deg(89.45),
                Angle.deg(90.30),
            ),
            ConstString.separation_double_page_y(): ("range", 2471, 2493),
            ConstString.page_rotation(1): (
                "range",
                Angle.deg(-0.56),
                Angle.deg(0.21),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(-0.56),
                Angle.deg(-0.39),
            ),
            ConstString.image_crop(1, "x1"): ("range", 81, 102),
            ConstString.image_crop(1, "y1"): ("range", 25, 81),
            ConstString.image_crop(1, "x2"): ("range", 2477, 2502),
            ConstString.image_crop(1, "y2"): ("range", 3505, 3505),
            ConstString.image_crop(2, "x1"): ("range", 157, 180),
            ConstString.image_crop(2, "y1"): ("range", 266, 268),
            ConstString.image_crop(2, "x2"): ("range", 2233, 2251),
            ConstString.image_crop(2, "y2"): ("range", 3380, 3382),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 14, 42),
            ConstString.image_border(1, 2): ("range", 14, 42),
            ConstString.image_border(1, 3): ("range", 30, 52),
            ConstString.image_border(1, 4): ("range", 30, 52),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 252, 265),
            ConstString.image_border(2, 2): ("range", 106, 122),
            ConstString.image_border(2, 3): ("range", 191, 198),
            ConstString.image_border(2, 4): ("range", 191, 198),
        },
    )


def test_no_split_line_wave_algo_2_png() -> None:
    """Failed to detect wave due to missing wave at the bottom."""
    MockDisableSeparatePage(MAX_VAL, FUZZING).treat_file(
        get_absolute_from_current_path(
            __file__, "no_split_line_wave_algo_2.png"
        ),
        {
            ConstString.separation_double_page_angle(): (
                "range",
                Angle.deg(90.29),
                Angle.deg(91.22),
            ),
            ConstString.separation_double_page_y(): ("range", 2466, 2488),
            ConstString.page_rotation(1): (
                "range",
                Angle.deg(0.94),
                Angle.deg(1.16),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(0.04),
                Angle.deg(0.21),
            ),
            ConstString.image_crop(1, "x1"): ("range", 266, 268),
            ConstString.image_crop(1, "y1"): ("range", 209, 210),
            ConstString.image_crop(1, "x2"): ("range", 2342, 2346),
            ConstString.image_crop(1, "y2"): ("range", 3411, 3413),
            ConstString.image_crop(2, "x1"): ("range", 161, 199),
            ConstString.image_crop(2, "y1"): ("range", 239, 241),
            ConstString.image_crop(2, "x2"): ("range", 2245, 2282),
            ConstString.image_crop(2, "y2"): ("range", 3433, 3434),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 180, 202),
            ConstString.image_border(1, 2): ("range", 82, 103),
            ConstString.image_border(1, 3): ("range", 191, 192),
            ConstString.image_border(1, 4): ("range", 191, 192),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 209, 226),
            ConstString.image_border(2, 2): ("range", 69, 86),
            ConstString.image_border(2, 3): ("range", 185, 188),
            ConstString.image_border(2, 4): ("range", 185, 188),
        },
    )


def test_crop_too_few_2_png() -> None:
    """Use different area on the left and the right to detect
    black noise."""
    MockDisableSeparatePage(MAX_VAL, FUZZING).treat_file(
        get_absolute_from_current_path(__file__, "crop_too_few_2.png"),
        {
            ConstString.separation_double_page_angle(): (
                "range",
                Angle.deg(90.20),
                Angle.deg(90.61),
            ),
            ConstString.separation_double_page_y(): ("range", 2530, 2540),
            ConstString.page_rotation(1): (
                "range",
                Angle.deg(0.99),
                Angle.deg(1.31),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(-0.16),
                Angle.deg(0.16),
            ),
            ConstString.image_crop(1, "x1"): ("range", 286, 290),
            ConstString.image_crop(1, "y1"): ("range", 163, 165),
            ConstString.image_crop(1, "x2"): ("range", 2396, 2403),
            ConstString.image_crop(1, "y2"): ("range", 3366, 3370),
            ConstString.image_crop(2, "x1"): ("range", 145, 163),
            ConstString.image_crop(2, "y1"): ("range", 175, 191),
            ConstString.image_crop(2, "x2"): ("range", 2266, 2287),
            ConstString.image_crop(2, "y2"): ("range", 3373, 3387),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 139, 157),
            ConstString.image_border(1, 2): ("range", 125, 145),
            ConstString.image_border(1, 3): ("range", 173, 175),
            ConstString.image_border(1, 4): ("range", 173, 175),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 173, 182),
            ConstString.image_border(2, 2): ("range", 107, 116),
            ConstString.image_border(2, 3): ("range", 166, 171),
            ConstString.image_border(2, 4): ("range", 166, 171),
        },
    )


def test_failed_detect_rectangle_png() -> None:
    """Before, approxPolyDP algo was used to detect shape.

    But, due to noise on the edge with background other pages,
    the contour have lost of noise.
    So use HoughLinesP to detect shape."""
    MockDisableSeparatePage(MAX_VAL, FUZZING).treat_file(
        get_absolute_from_current_path(
            __file__, "failed_detect_rectangle.png"
        ),
        {
            ConstString.separation_double_page_angle(): (
                "range",
                Angle.deg(90.12),
                Angle.deg(90.31),
            ),
            ConstString.separation_double_page_y(): ("range", 2471, 2477),
            ConstString.page_rotation(1): (
                "range",
                Angle.deg(0.14),
                Angle.deg(0.21),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(0.09),
                Angle.deg(0.21),
            ),
            ConstString.image_crop(1, "x1"): ("range", 257, 258),
            ConstString.image_crop(1, "y1"): ("range", 201, 202),
            ConstString.image_crop(1, "x2"): ("range", 2333, 2334),
            ConstString.image_crop(1, "y2"): ("range", 3401, 3402),
            ConstString.image_crop(2, "x1"): ("range", 131, 139),
            ConstString.image_crop(2, "y1"): ("range", 213, 215),
            ConstString.image_crop(2, "x2"): ("range", 2216, 2222),
            ConstString.image_crop(2, "y2"): ("range", 3406, 3406),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 186, 188),
            ConstString.image_border(1, 2): ("range", 97, 101),
            ConstString.image_border(1, 3): ("range", 192, 192),
            ConstString.image_border(1, 4): ("range", 192, 192),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 197, 204),
            ConstString.image_border(2, 2): ("range", 91, 97),
            ConstString.image_border(2, 3): ("range", 187, 188),
            ConstString.image_border(2, 4): ("range", 187, 188),
        },
    )


def test_single_page_png() -> None:
    """Detect that the scan is single page."""
    MockDisableSeparatePage(MAX_VAL, FUZZING).treat_file(
        get_absolute_from_current_path(__file__, "single_page.png"),
        {
            ConstString.separation_double_page_angle(): (
                "range",
                Angle.deg(89.71),
                Angle.deg(90.06),
            ),
            ConstString.separation_double_page_y(): ("range", 2464, 2476),
            ConstString.page_rotation(1): (
                "range",
                Angle.deg(-0.16),
                Angle.deg(0.16),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(-0.26),
                Angle.deg(0.01),
            ),
            ConstString.image_crop(1, "x1"): ("range", 1, 9),
            ConstString.image_crop(1, "y1"): ("range", 7, 9),
            ConstString.image_crop(1, "x2"): ("range", 2464, 2478),
            ConstString.image_crop(1, "y2"): ("range", 3500, 3505),
            ConstString.image_crop(2, "x1"): ("range", 0, 0),
            ConstString.image_crop(2, "y1"): ("range", 0, 0),
            ConstString.image_crop(2, "x2"): ("range", 0, 0),
            ConstString.image_crop(2, "y2"): ("range", 0, 0),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 5, 8),
            ConstString.image_border(1, 2): ("range", 5, 8),
            ConstString.image_border(1, 3): ("range", 2, 11),
            ConstString.image_border(1, 4): ("range", 2, 11),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 0, 0),
            ConstString.image_border(2, 2): ("range", 0, 0),
            ConstString.image_border(2, 3): ("range", 0, 0),
            ConstString.image_border(2, 4): ("range", 0, 0),
        },
    )


def test_no_split_line_wave_algo_3_png() -> None:
    """Failed to detect wave due to missing wave at the bottom."""
    MockDisableSeparatePage(MAX_VAL, FUZZING).treat_file(
        get_absolute_from_current_path(
            __file__, "no_split_line_wave_algo_3.png"
        ),
        {
            ConstString.separation_double_page_angle(): (
                "range",
                Angle.deg(90.04),
                Angle.deg(90.31),
            ),
            ConstString.separation_double_page_y(): ("range", 2399, 2411),
            ConstString.page_rotation(1): (
                "range",
                Angle.deg(-0.16),
                Angle.deg(0.21),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(-0.11),
                Angle.deg(0.46),
            ),
            ConstString.image_crop(1, "x1"): ("range", 181, 189),
            ConstString.image_crop(1, "y1"): ("range", 2955, 2960),
            ConstString.image_crop(1, "x2"): ("range", 2198, 2206),
            ConstString.image_crop(1, "y2"): ("range", 3201, 3203),
            ConstString.image_crop(2, "x1"): ("range", 0, 0),
            ConstString.image_crop(2, "y1"): ("range", 0, 0),
            ConstString.image_crop(2, "x2"): ("range", 0, 0),
            ConstString.image_crop(2, "y2"): ("range", 0, 0),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 2950, 2958),
            ConstString.image_border(1, 2): ("range", 287, 293),
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
    MockDisableSeparatePage(MAX_VAL, FUZZING).treat_file(
        get_absolute_from_current_path(__file__, "wrong_split_line_4.png"),
        {
            ConstString.separation_double_page_angle(): (
                "range",
                Angle.deg(90.55),
                Angle.deg(91.47),
            ),
            ConstString.separation_double_page_y(): ("range", 49, 69),
            ConstString.page_rotation(1): (
                "range",
                Angle.deg(-0.01),
                Angle.deg(1.41),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(0.99),
                Angle.deg(1.21),
            ),
            ConstString.image_crop(1, "x1"): ("range", 0, 0),
            ConstString.image_crop(1, "y1"): ("range", 0, 0),
            ConstString.image_crop(1, "x2"): ("range", 0, 0),
            ConstString.image_crop(1, "y2"): ("range", 0, 0),
            ConstString.image_crop(2, "x1"): ("range", 276, 292),
            ConstString.image_crop(2, "y1"): ("range", 329, 331),
            ConstString.image_crop(2, "x2"): ("range", 2300, 2318),
            ConstString.image_crop(2, "y2"): ("range", 3216, 3219),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 0, 0),
            ConstString.image_border(1, 2): ("range", 0, 0),
            ConstString.image_border(1, 3): ("range", 0, 0),
            ConstString.image_border(1, 4): ("range", 0, 0),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 321, 323),
            ConstString.image_border(2, 2): ("range", 276, 279),
            ConstString.image_border(2, 3): ("range", 216, 219),
            ConstString.image_border(2, 4): ("range", 216, 219),
        },
    )


def test_failed_split_line_line_algo_3_png() -> None:
    """get_rectangle_from_contour_hough_lines fails
    because fewer than 4 lines are detected."""
    MockDisableSeparatePage(MAX_VAL, FUZZING).treat_file(
        get_absolute_from_current_path(
            __file__, "failed_split_line_line_algo_3.png"
        ),
        {
            ConstString.separation_double_page_angle(): (
                "range",
                Angle.deg(89.95),
                Angle.deg(90.10),
            ),
            ConstString.separation_double_page_y(): ("range", 37, 41),
            ConstString.page_rotation(1): (
                "range",
                Angle.deg(-0.16),
                Angle.deg(0.01),
            ),
            ConstString.page_rotation(2): (
                "range",
                Angle.deg(-0.16),
                Angle.deg(0.06),
            ),
            ConstString.image_crop(1, "x1"): ("range", 0, 0),
            ConstString.image_crop(1, "y1"): ("range", 0, 0),
            ConstString.image_crop(1, "x2"): ("range", 0, 0),
            ConstString.image_crop(1, "y2"): ("range", 0, 0),
            ConstString.image_crop(2, "x1"): ("range", 244, 256),
            ConstString.image_crop(2, "y1"): ("range", 152, 155),
            ConstString.image_crop(2, "x2"): ("range", 2259, 2270),
            ConstString.image_crop(2, "y2"): ("range", 3359, 3361),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 0, 0),
            ConstString.image_border(1, 2): ("range", 0, 0),
            ConstString.image_border(1, 3): ("range", 0, 0),
            ConstString.image_border(1, 4): ("range", 0, 0),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 143, 146),
            ConstString.image_border(2, 2): ("range", 134, 137),
            ConstString.image_border(2, 3): ("range", 221, 223),
            ConstString.image_border(2, 4): ("range", 221, 223),
        },
    )
