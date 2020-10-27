from typing import Optional, Any, Dict, Union, Tuple
import unittest

import numpy as np

from script import SeparatePage
from print_interface import ConstString
from tests.mock_separate_page import MockDisableSeparatePage
import fsext

np.seterr(all="raise")
tc = unittest.TestCase()


def get_absolute_from_current_path(filename: str) -> str:
    return fsext.get_absolute_from_current_path(__file__, filename)


def treat_file(
    sep: SeparatePage,
    filename: str,
    dict_test: Optional[Dict[str, Any]] = None,
    dict_default_values: Optional[
        Dict[str, Union[int, float, Tuple[int, int]]]
    ] = None,
    enable_debug: bool = True,
) -> None:
    sep.treat_file(
        get_absolute_from_current_path(filename),
        dict_test,
        dict_default_values,
        enable_debug,
    )


def test_0001_png() -> None:
    """first good page"""
    treat_file(
        SeparatePage(),
        get_absolute_from_current_path("0001.png"),
        {
            ConstString.separation_double_page_angle(): (
                "range",
                90.51,
                90.55,
            ),
            ConstString.separation_double_page_y(): ("range", 2483, 2485),
            ConstString.page_rotation(1): ("range", 0.65, 0.76),
            ConstString.page_rotation(2): ("range", 0.14, 0.21),
            ConstString.image_crop(1, "x1"): ("range", 330, 332),
            ConstString.image_crop(1, "y1"): ("range", 336, 336),
            ConstString.image_crop(1, "x2"): ("range", 2342, 2343),
            ConstString.image_crop(1, "y2"): ("range", 3222, 3223),
            ConstString.image_crop(2, "x1"): ("range", 168, 170),
            ConstString.image_crop(2, "y1"): ("range", 649, 649),
            ConstString.image_crop(2, "x2"): ("range", 2180, 2185),
            ConstString.image_crop(2, "y2"): ("range", 3360, 3361),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 324, 326),
            ConstString.image_border(1, 2): ("range", 275, 276),
            ConstString.image_border(1, 3): ("range", 223, 224),
            ConstString.image_border(1, 4): ("range", 223, 224),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 672, 674),
            ConstString.image_border(2, 2): ("range", 101, 104),
            ConstString.image_border(2, 3): ("range", 222, 224),
            ConstString.image_border(2, 4): ("range", 222, 224),
        },
    )


def test_2_pages_2_contours_png() -> None:
    """There is not one contour for the two pages,
    but one contour for each page.
    """
    treat_file(
        SeparatePage(),
        get_absolute_from_current_path("2-pages-2-contours.png"),
        {
            ConstString.separation_double_page_angle(): (
                "range",
                90.22,
                90.32,
            ),
            ConstString.separation_double_page_y(): ("range", 2487, 2488),
            ConstString.page_rotation(1): ("range", -0.01, 0.11),
            ConstString.page_rotation(2): ("range", 0.24, 0.41),
            ConstString.image_crop(1, "x1"): ("range", 1181, 1185),
            ConstString.image_crop(1, "y1"): ("range", 1720, 1722),
            ConstString.image_crop(1, "x2"): ("range", 1182, 1186),
            ConstString.image_crop(1, "y2"): ("range", 1721, 1723),
            ConstString.image_crop(2, "x1"): ("range", 108, 114),
            ConstString.image_crop(2, "y1"): ("range", 241, 241),
            ConstString.image_crop(2, "x2"): ("range", 2153, 2159),
            ConstString.image_crop(2, "y2"): ("range", 3239, 3240),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 1752, 1752),
            ConstString.image_border(1, 2): ("range", 1753, 1753),
            ConstString.image_border(1, 3): ("range", 1239, 1239),
            ConstString.image_border(1, 4): ("range", 1239, 1239),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 230, 240),
            ConstString.image_border(2, 2): ("range", 248, 259),
            ConstString.image_border(2, 3): ("range", 207, 207),
            ConstString.image_border(2, 4): ("range", 207, 207),
        },
    )


def test_black_border_not_removed_png() -> None:
    """The border on the right is still there."""
    treat_file(
        SeparatePage(),
        get_absolute_from_current_path("black-border-not-removed.png"),
        {
            ConstString.separation_double_page_angle(): (
                "range",
                89.96,
                90.1,
            ),
            ConstString.separation_double_page_y(): ("range", 2454, 2455),
            ConstString.page_rotation(1): ("range", -0.01, 0.01),
            ConstString.page_rotation(2): ("range", -0.21, 0.01),
            ConstString.image_crop(1, "x1"): ("range", 298, 298),
            ConstString.image_crop(1, "y1"): ("range", 143, 144),
            ConstString.image_crop(1, "x2"): ("range", 2308, 2308),
            ConstString.image_crop(1, "y2"): ("range", 3346, 3346),
            ConstString.image_crop(2, "x1"): ("range", 158, 158),
            ConstString.image_crop(2, "y1"): ("range", 144, 146),
            ConstString.image_crop(2, "x2"): ("range", 2169, 2172),
            ConstString.image_crop(2, "y2"): ("range", 3351, 3353),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 127, 129),
            ConstString.image_border(1, 2): ("range", 156, 157),
            ConstString.image_border(1, 3): ("range", 225, 225),
            ConstString.image_border(1, 4): ("range", 225, 225),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 131, 132),
            ConstString.image_border(2, 2): ("range", 146, 151),
            ConstString.image_border(2, 3): ("range", 223, 224),
            ConstString.image_border(2, 4): ("range", 223, 224),
        },
    )


def test_image_failed_to_rotate_png() -> None:
    """Failed to compute angle to rotate. The image takes the whole page."""
    treat_file(
        SeparatePage(),
        get_absolute_from_current_path("image_failed_to_rotate.png"),
        {
            ConstString.separation_double_page_angle(): (
                "range",
                90.32,
                90.50,
            ),
            ConstString.separation_double_page_y(): ("range", 2487, 2487),
            ConstString.page_rotation(1): ("range", 0.29, 0.41),
            ConstString.page_rotation(2): ("range", 0.34, 0.45),
            ConstString.image_crop(1, "x1"): ("range", 77, 86),
            ConstString.image_crop(1, "y1"): ("range", 1, 8),
            ConstString.image_crop(1, "x2"): ("range", 2456, 2481),
            ConstString.image_crop(1, "y2"): ("range", 3483, 3486),
            ConstString.image_crop(2, "x1"): ("range", 170, 183),
            ConstString.image_crop(2, "y1"): ("range", 234, 235),
            ConstString.image_crop(2, "x2"): ("range", 2250, 2261),
            ConstString.image_crop(2, "y2"): ("range", 3355, 3356),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 12, 15),
            ConstString.image_border(1, 2): ("range", 12, 15),
            ConstString.image_border(1, 3): ("range", 38, 55),
            ConstString.image_border(1, 4): ("range", 38, 55),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 206, 207),
            ConstString.image_border(2, 2): ("range", 159, 160),
            ConstString.image_border(2, 3): ("range", 189, 191),
            ConstString.image_border(2, 4): ("range", 189, 191),
        },
    )


def test_image_failed_to_crop_data_png() -> None:
    """Failed to detect edges. The image takes the whole page and is too closed
    to the border of the image.
    """
    treat_file(
        SeparatePage(),
        get_absolute_from_current_path("image_failed_to_crop_data.png"),
        {
            ConstString.separation_double_page_angle(): (
                "range",
                90.06,
                90.17,
            ),
            ConstString.separation_double_page_y(): ("range", 2484, 2485),
            ConstString.page_rotation(1): ("range", -0.01, 0.01),
            ConstString.page_rotation(2): ("range", -0.01, 0.16),
            ConstString.image_crop(1, "x1"): ("range", 116, 116),
            ConstString.image_crop(1, "y1"): ("range", 7, 7),
            ConstString.image_crop(1, "x2"): ("range", 2476, 2476),
            ConstString.image_crop(1, "y2"): ("range", 3503, 3503),
            ConstString.image_crop(2, "x1"): ("range", 160, 164),
            ConstString.image_crop(2, "y1"): ("range", 218, 220),
            ConstString.image_crop(2, "x2"): ("range", 2237, 2242),
            ConstString.image_crop(2, "y2"): ("range", 3348, 3350),
            ConstString.image_dpi(1): ("difference", 300, 0.0000001),
            ConstString.image_border(1, 1): ("range", 5, 5),
            ConstString.image_border(1, 2): ("range", 5, 5),
            ConstString.image_border(1, 3): ("range", 55, 55),
            ConstString.image_border(1, 4): ("range", 55, 55),
            ConstString.image_dpi(2): ("difference", 300, 0.0000001),
            ConstString.image_border(2, 1): ("range", 210, 212),
            ConstString.image_border(2, 2): ("range", 145, 147),
            ConstString.image_border(2, 3): ("range", 190, 191),
            ConstString.image_border(2, 4): ("range", 190, 191),
        },
    )


def test_disabled_enable_debug() -> None:
    """Check that enable_debug=False works."""
    tc.assertTrue(
        fsext.is_file_exists(get_absolute_from_current_path("0001.png"))
    )
    fsext.copy_file(
        get_absolute_from_current_path("0001.png"),
        get_absolute_from_current_path("0001_debug.png"),
    )
    treat_file(
        SeparatePage(),
        get_absolute_from_current_path("0001_debug.png"),
        enable_debug=False,
    )
    fsext.delete_file(get_absolute_from_current_path("0001_debug.png"))


def test_mock_stop_at_0() -> None:
    """Check that enable_debug=False works."""
    tc.assertTrue(
        fsext.is_file_exists(get_absolute_from_current_path("0001.png"))
    )
    fsext.copy_file(
        get_absolute_from_current_path("0001.png"),
        get_absolute_from_current_path("0001_0.png"),
    )
    fsext.del_pattern(fsext.extract_path(__file__), "0001_0.png_*")
    treat_file(
        MockDisableSeparatePage(0),
        get_absolute_from_current_path("0001_0.png"),
        enable_debug=True,
    )
    fsext.delete_file(get_absolute_from_current_path("0001_0.png"))
    tc.assertFalse(
        fsext.is_file_exists(
            get_absolute_from_current_path("0001_0.png_1_7.png")
        )
    )
    tc.assertFalse(
        fsext.is_file_exists(
            get_absolute_from_current_path("0001_0.png_2_7.png")
        )
    )
    tc.assertFalse(
        fsext.is_file_exists(
            get_absolute_from_current_path("0001_0.png_3_1.png")
        )
    )
    tc.assertFalse(
        fsext.is_file_exists(
            get_absolute_from_current_path("0001_0.png_3_2.png")
        )
    )
    tc.assertFalse(
        fsext.is_file_exists(
            get_absolute_from_current_path("0001_0.png_4_1_5.png")
        )
    )
    tc.assertFalse(
        fsext.is_file_exists(
            get_absolute_from_current_path("0001_0.png_4_2_5.png")
        )
    )
    tc.assertFalse(
        fsext.is_file_exists(
            get_absolute_from_current_path("0001_0.png_page_1.png")
        )
    )
    tc.assertFalse(
        fsext.is_file_exists(
            get_absolute_from_current_path("0001_0.png_page_2.png")
        )
    )


def test_mock_stop_at_1() -> None:
    """Check that enable_debug=False works."""
    tc.assertTrue(
        fsext.is_file_exists(get_absolute_from_current_path("0001.png"))
    )
    fsext.copy_file(
        get_absolute_from_current_path("0001.png"),
        get_absolute_from_current_path("0001_1.png"),
    )
    fsext.del_pattern(fsext.extract_path(__file__), "0001_1.png_*")
    treat_file(
        MockDisableSeparatePage(1),
        get_absolute_from_current_path("0001_1.png"),
        enable_debug=True,
    )
    fsext.delete_file(get_absolute_from_current_path("0001_1.png"))
    tc.assertTrue(
        fsext.is_file_exists(
            get_absolute_from_current_path("0001_1.png_1_7.png")
        )
    )
    tc.assertTrue(
        fsext.is_file_exists(
            get_absolute_from_current_path("0001_1.png_2_7.png")
        )
    )
    tc.assertTrue(
        fsext.is_file_exists(
            get_absolute_from_current_path("0001_1.png_3_1.png")
        )
    )
    tc.assertTrue(
        fsext.is_file_exists(
            get_absolute_from_current_path("0001_1.png_3_2.png")
        )
    )
    tc.assertFalse(
        fsext.is_file_exists(
            get_absolute_from_current_path("0001_1.png_4_1_5.png")
        )
    )
    tc.assertFalse(
        fsext.is_file_exists(
            get_absolute_from_current_path("0001_1.png_4_2_5.png")
        )
    )
    tc.assertFalse(
        fsext.is_file_exists(
            get_absolute_from_current_path("0001_1.png_page_1.png")
        )
    )
    tc.assertFalse(
        fsext.is_file_exists(
            get_absolute_from_current_path("0001_1.png_page_2.png")
        )
    )


def test_mock_stop_at_2() -> None:
    """Check that enable_debug=False works."""
    tc.assertTrue(
        fsext.is_file_exists(get_absolute_from_current_path("0001.png"))
    )
    fsext.copy_file(
        get_absolute_from_current_path("0001.png"),
        get_absolute_from_current_path("0001_2.png"),
    )
    fsext.del_pattern(fsext.extract_path(__file__), "0001_2.png_*")
    treat_file(
        MockDisableSeparatePage(2),
        get_absolute_from_current_path("0001_2.png"),
        enable_debug=True,
    )
    fsext.delete_file(get_absolute_from_current_path("0001_2.png"))
    tc.assertTrue(
        fsext.is_file_exists(
            get_absolute_from_current_path("0001_2.png_1_7.png")
        )
    )
    tc.assertTrue(
        fsext.is_file_exists(
            get_absolute_from_current_path("0001_2.png_2_7.png")
        )
    )
    tc.assertTrue(
        fsext.is_file_exists(
            get_absolute_from_current_path("0001_2.png_3_1.png")
        )
    )
    tc.assertTrue(
        fsext.is_file_exists(
            get_absolute_from_current_path("0001_2.png_3_2.png")
        )
    )
    tc.assertTrue(
        fsext.is_file_exists(
            get_absolute_from_current_path("0001_2.png_4_1_5.png")
        )
    )
    tc.assertTrue(
        fsext.is_file_exists(
            get_absolute_from_current_path("0001_2.png_4_2_5.png")
        )
    )
    tc.assertFalse(
        fsext.is_file_exists(
            get_absolute_from_current_path("0001_2.png_page_1.png")
        )
    )
    tc.assertFalse(
        fsext.is_file_exists(
            get_absolute_from_current_path("0001_2.png_page_2.png")
        )
    )


def test_mock_stop_at_3() -> None:
    """Check that enable_debug=False works."""
    tc.assertTrue(
        fsext.is_file_exists(get_absolute_from_current_path("0001.png"))
    )
    fsext.copy_file(
        get_absolute_from_current_path("0001.png"),
        get_absolute_from_current_path("0001_3.png"),
    )
    fsext.del_pattern(fsext.extract_path(__file__), "0001_3.png_*")
    treat_file(
        MockDisableSeparatePage(3),
        get_absolute_from_current_path("0001_3.png"),
        enable_debug=True,
    )
    fsext.delete_file(get_absolute_from_current_path("0001_3.png"))
    tc.assertTrue(
        fsext.is_file_exists(
            get_absolute_from_current_path("0001_3.png_1_7.png")
        )
    )
    tc.assertTrue(
        fsext.is_file_exists(
            get_absolute_from_current_path("0001_3.png_2_7.png")
        )
    )
    tc.assertTrue(
        fsext.is_file_exists(
            get_absolute_from_current_path("0001_3.png_3_1.png")
        )
    )
    tc.assertTrue(
        fsext.is_file_exists(
            get_absolute_from_current_path("0001_3.png_3_2.png")
        )
    )
    tc.assertTrue(
        fsext.is_file_exists(
            get_absolute_from_current_path("0001_3.png_4_1_5.png")
        )
    )
    tc.assertTrue(
        fsext.is_file_exists(
            get_absolute_from_current_path("0001_3.png_4_2_5.png")
        )
    )
    tc.assertFalse(
        fsext.is_file_exists(
            get_absolute_from_current_path("0001_3.png_page_1.png")
        )
    )
    tc.assertFalse(
        fsext.is_file_exists(
            get_absolute_from_current_path("0001_3.png_page_2.png")
        )
    )


def test_mock_stop_at_4() -> None:
    """Check that enable_debug=False works."""
    tc.assertTrue(
        fsext.is_file_exists(get_absolute_from_current_path("0001.png"))
    )
    fsext.copy_file(
        get_absolute_from_current_path("0001.png"),
        get_absolute_from_current_path("0001_4.png"),
    )
    fsext.del_pattern(fsext.extract_path(__file__), "0001_4.png_*")
    treat_file(
        MockDisableSeparatePage(4),
        get_absolute_from_current_path("0001_4.png"),
        enable_debug=True,
    )
    fsext.delete_file(get_absolute_from_current_path("0001_4.png"))
    tc.assertTrue(
        fsext.is_file_exists(
            get_absolute_from_current_path("0001_4.png_1_7.png")
        )
    )
    tc.assertTrue(
        fsext.is_file_exists(
            get_absolute_from_current_path("0001_4.png_2_7.png")
        )
    )
    tc.assertTrue(
        fsext.is_file_exists(
            get_absolute_from_current_path("0001_4.png_3_1.png")
        )
    )
    tc.assertTrue(
        fsext.is_file_exists(
            get_absolute_from_current_path("0001_4.png_3_2.png")
        )
    )
    tc.assertTrue(
        fsext.is_file_exists(
            get_absolute_from_current_path("0001_4.png_4_1_5.png")
        )
    )
    tc.assertTrue(
        fsext.is_file_exists(
            get_absolute_from_current_path("0001_4.png_4_2_5.png")
        )
    )
    tc.assertFalse(
        fsext.is_file_exists(
            get_absolute_from_current_path("0001_4.png_page_1.png")
        )
    )
    tc.assertFalse(
        fsext.is_file_exists(
            get_absolute_from_current_path("0001_4.png_page_2.png")
        )
    )


def test_mock_stop_at_5() -> None:
    """Check that enable_debug=False works."""
    tc.assertTrue(
        fsext.is_file_exists(get_absolute_from_current_path("0001.png"))
    )
    fsext.copy_file(
        get_absolute_from_current_path("0001.png"),
        get_absolute_from_current_path("0001_5.png"),
    )
    fsext.del_pattern(fsext.extract_path(__file__), "0001_5.png_*")
    treat_file(
        MockDisableSeparatePage(5),
        get_absolute_from_current_path("0001_5.png"),
        enable_debug=True,
    )
    fsext.delete_file(get_absolute_from_current_path("0001_5.png"))
    tc.assertTrue(
        fsext.is_file_exists(
            get_absolute_from_current_path("0001_5.png_1_7.png")
        )
    )
    tc.assertTrue(
        fsext.is_file_exists(
            get_absolute_from_current_path("0001_5.png_2_7.png")
        )
    )
    tc.assertTrue(
        fsext.is_file_exists(
            get_absolute_from_current_path("0001_5.png_3_1.png")
        )
    )
    tc.assertTrue(
        fsext.is_file_exists(
            get_absolute_from_current_path("0001_5.png_3_2.png")
        )
    )
    tc.assertTrue(
        fsext.is_file_exists(
            get_absolute_from_current_path("0001_5.png_4_1_5.png")
        )
    )
    tc.assertTrue(
        fsext.is_file_exists(
            get_absolute_from_current_path("0001_5.png_4_2_5.png")
        )
    )
    tc.assertTrue(
        fsext.is_file_exists(
            get_absolute_from_current_path("0001_5.png_page_1.png")
        )
    )
    tc.assertTrue(
        fsext.is_file_exists(
            get_absolute_from_current_path("0001_5.png_page_2.png")
        )
    )
