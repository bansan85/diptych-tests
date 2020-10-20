from typing import Optional, Any, Dict, Union, Tuple
import os
import numpy as np

import script
from print_interface import ConstString

np.seterr(all="raise")


def treat_file(
    filename: str,
    dict_test: Optional[Dict[str, Any]] = None,
    dict_default_values: Optional[
        Dict[str, Union[int, float, Tuple[int, int]]]
    ] = None,
) -> None:
    sep = script.SeparatePage()
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    sep.treat_file(filename, dict_test, dict_default_values, True)


def test_0001_png() -> None:
    """first good page"""
    treat_file(
        "0001.png",
        {
            ConstString.separation_double_page_angle(): (
                90.55,
                "range",
                -0.1,
                0.1,
            ),
            ConstString.separation_double_page_y(): (2485, "range", -1, 1),
            ConstString.page_rotation(1): (0.73, "range", -0.1, 0.1),
            ConstString.page_rotation(2): (0.16, "range", -0.1, 0.1),
            ConstString.image_crop(1, "x1"): (331, "range", -1, 1),
            ConstString.image_crop(1, "y1"): (336, "range", -1, 1),
            ConstString.image_crop(1, "x2"): (2342, "range", -1, 1),
            ConstString.image_crop(1, "y2"): (3223, "range", -1, 1),
            ConstString.image_crop(2, "x1"): (170, "range", -1, 1),
            ConstString.image_crop(2, "y1"): (649, "range", -1, 1),
            ConstString.image_crop(2, "x2"): (2184, "range", -1, 1),
            ConstString.image_crop(2, "y2"): (3361, "range", -1, 1),
            ConstString.image_dpi(1): (300, "difference", 0.0000001),
            ConstString.image_border(1, 1): (324, "range", -1, 1),
            ConstString.image_border(1, 2): (276, "range", -1, 1),
            ConstString.image_border(1, 3): (224, "range", -1, 1),
            ConstString.image_border(1, 4): (224, "range", -1, 1),
            ConstString.image_dpi(2): (300, "difference", 0.0000001),
            ConstString.image_border(2, 1): (674, "range", -1, 1),
            ConstString.image_border(2, 2): (101, "range", -1, 1),
            ConstString.image_border(2, 3): (223, "range", -1, 1),
            ConstString.image_border(2, 4): (223, "range", -1, 1),
        },
    )


def test_2_pages_2_contours_png() -> None:
    """There is not one contour for the two pages,
    but one contour for each page.
    """
    treat_file(
        "2-pages-2-contours.png",
        {
            ConstString.separation_double_page_angle(): (
                90.22,
                "range",
                -0.1,
                0.1,
            ),
            ConstString.separation_double_page_y(): (2487, "range", -1, 1),
            ConstString.page_rotation(1): (0.08, "range", -0.1, 0.1),
            ConstString.page_rotation(2): (0.25, "range", -0.1, 0.1),
            ConstString.image_crop(1, "x1"): (1185, "range", -1, 1),
            ConstString.image_crop(1, "y1"): (1720, "range", -1, 1),
            ConstString.image_crop(1, "x2"): (1186, "range", -1, 1),
            ConstString.image_crop(1, "y2"): (1721, "range", -1, 1),
            ConstString.image_crop(2, "x1"): (108, "range", -1, 1),
            ConstString.image_crop(2, "y1"): (241, "range", -1, 1),
            ConstString.image_crop(2, "x2"): (2154, "range", -1, 1),
            ConstString.image_crop(2, "y2"): (3240, "range", -1, 1),
            ConstString.image_dpi(1): (300, "difference", 0.0000001),
            ConstString.image_border(1, 1): (1752, "range", -1, 1),
            ConstString.image_border(1, 2): (1753, "range", -1, 1),
            ConstString.image_border(1, 3): (1239, "range", -1, 1),
            ConstString.image_border(1, 4): (1239, "range", -1, 1),
            ConstString.image_dpi(2): (300, "difference", 0.0000001),
            ConstString.image_border(2, 1): (240, "range", -1, 1),
            ConstString.image_border(2, 2): (248, "range", -1, 1),
            ConstString.image_border(2, 3): (207, "range", -1, 1),
            ConstString.image_border(2, 4): (207, "range", -1, 1),
        },
    )


def test_black_border_not_removed_png() -> None:
    """The border on the right is still there."""
    treat_file(
        "black-border-not-removed.png",
        {
            ConstString.separation_double_page_angle(): (
                89.97,
                "range",
                -0.1,
                0.1,
            ),
            ConstString.separation_double_page_y(): (2454, "range", -1, 1),
            ConstString.page_rotation(1): (0.01, "range", -0.1, 0.1),
            ConstString.page_rotation(2): (-0.1, "range", -0.1, 0.1),
            ConstString.image_crop(1, "x1"): (298, "range", -1, 1),
            ConstString.image_crop(1, "y1"): (143, "range", -1, 1),
            ConstString.image_crop(1, "x2"): (2308, "range", -1, 1),
            ConstString.image_crop(1, "y2"): (3346, "range", -1, 1),
            ConstString.image_crop(2, "x1"): (158, "range", -1, 1),
            ConstString.image_crop(2, "y1"): (144, "range", -1, 1),
            ConstString.image_crop(2, "x2"): (2172, "range", -1, 1),
            ConstString.image_crop(2, "y2"): (3353, "range", -1, 1),
            ConstString.image_dpi(1): (300, "difference", 0.0000001),
            ConstString.image_border(1, 1): (127, "range", -1, 1),
            ConstString.image_border(1, 2): (157, "range", -1, 1),
            ConstString.image_border(1, 3): (225, "range", -1, 1),
            ConstString.image_border(1, 4): (225, "range", -1, 1),
            ConstString.image_dpi(2): (300, "difference", 0.0000001),
            ConstString.image_border(2, 1): (132, "range", -1, 1),
            ConstString.image_border(2, 2): (146, "range", -1, 1),
            ConstString.image_border(2, 3): (223, "range", -1, 1),
            ConstString.image_border(2, 4): (223, "range", -1, 1),
        },
    )


def test_image_failed_to_rotate_png() -> None:
    """If AngleLimitStddev is too small, the angle to rotate the image
    can not be computed.
    """
    treat_file(
        "image_failed_to_rotate.png",
        {
            ConstString.separation_double_page_angle(): (
                90.44,
                "range",
                -0.1,
                0.1,
            ),
            ConstString.separation_double_page_y(): (2495, "range", -1, 1),
            ConstString.page_rotation(1): (0.40, "range", -0.1, 0.1),
            ConstString.page_rotation(2): (0.35, "range", -0.1, 0.1),
            ConstString.image_crop(1, "x1"): (209, "range", -1, 1),
            ConstString.image_crop(1, "y1"): (8, "range", -1, 1),
            ConstString.image_crop(1, "x2"): (2485, "range", -1, 1),
            ConstString.image_crop(1, "y2"): (3487, "range", -1, 1),
            ConstString.image_crop(2, "x1"): (169, "range", -1, 1),
            ConstString.image_crop(2, "y1"): (234, "range", -1, 1),
            ConstString.image_crop(2, "x2"): (2250, "range", -1, 1),
            ConstString.image_crop(2, "y2"): (3356, "range", -1, 1),
            ConstString.image_dpi(1): (300, "difference", 0.0000001),
            ConstString.image_border(1, 1): (14, "range", -1, 1),
            ConstString.image_border(1, 2): (14, "range", -1, 1),
            ConstString.image_border(1, 3): (102, "range", -1, 1),
            ConstString.image_border(1, 4): (102, "range", -1, 1),
            ConstString.image_dpi(2): (300, "difference", 0.0000001),
            ConstString.image_border(2, 1): (205, "range", -1, 1),
            ConstString.image_border(2, 2): (160, "range", -1, 1),
            ConstString.image_border(2, 3): (189, "range", -1, 1),
            ConstString.image_border(2, 4): (189, "range", -1, 1),
        },
    )
