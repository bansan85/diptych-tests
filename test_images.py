from typing import Optional, Any, Dict, Union, Tuple
import os
import numpy as np

import script

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
            "separation double page angle": (90.55, "range", -0.1, 0.1),
            "separation double page y=0": (2485, "range", -1, 1),
            "page rotation 1": (0.73, "range", -0.1, 0.1),
            "page rotation 2": (0.16, "range", -0.1, 0.1),
            "image 1 crop x1": (331, "range", -1, 1),
            "image 1 crop y1": (336, "range", -1, 1),
            "image 1 crop x2": (2342, "range", -1, 1),
            "image 1 crop y2": (3223, "range", -1, 1),
            "image 2 crop x1": (170, "range", -1, 1),
            "image 2 crop y1": (649, "range", -1, 1),
            "image 2 crop x2": (2184, "range", -1, 1),
            "image 2 crop y2": (3361, "range", -1, 1),
            "image 1 dpi": (300, "difference", 0.0000001),
            "image 1 recadre haut": (324, "range", -1, 1),
            "image 1 recadre bas": (276, "range", -1, 1),
            "image 1 recadre gauche": (224, "range", -1, 1),
            "image 1 recadre droite": (224, "range", -1, 1),
            "image 2 dpi": (300, "difference", 0.0000001),
            "image 2 recadre haut": (674, "range", -1, 1),
            "image 2 recadre bas": (101, "range", -1, 1),
            "image 2 recadre gauche": (223, "range", -1, 1),
            "image 2 recadre droite": (223, "range", -1, 1),
        },
    )


def test_2_pages_2_contours_png() -> None:
    """There is not one contour for the two pages,
    but one contour for each page.
    """
    treat_file(
        "2-pages-2-contours.png",
        {
            "separation double page angle": (90.22, "range", -0.1, 0.1),
            "separation double page y=0": (2487, "range", -1, 1),
            "page rotation 1": (0.08, "range", -0.1, 0.1),
            "page rotation 2": (0.25, "range", -0.1, 0.1),
            "image 1 crop x1": (1185, "range", -1, 1),
            "image 1 crop y1": (1720, "range", -1, 1),
            "image 1 crop x2": (1186, "range", -1, 1),
            "image 1 crop y2": (1721, "range", -1, 1),
            "image 2 crop x1": (108, "range", -1, 1),
            "image 2 crop y1": (241, "range", -1, 1),
            "image 2 crop x2": (2154, "range", -1, 1),
            "image 2 crop y2": (3240, "range", -1, 1),
            "image 1 dpi": (300, "difference", 0.0000001),
            "image 1 recadre haut": (1752, "range", -1, 1),
            "image 1 recadre bas": (1753, "range", -1, 1),
            "image 1 recadre gauche": (1239, "range", -1, 1),
            "image 1 recadre droite": (1239, "range", -1, 1),
            "image 2 dpi": (300, "difference", 0.0000001),
            "image 2 recadre haut": (240, "range", -1, 1),
            "image 2 recadre bas": (248, "range", -1, 1),
            "image 2 recadre gauche": (207, "range", -1, 1),
            "image 2 recadre droite": (207, "range", -1, 1),
        },
    )


def test_black_border_not_removed_png() -> None:
    """The border on the right is still there."""
    treat_file(
        "black-border-not-removed.png",
        {
            "separation double page angle": (89.97, "range", -0.1, 0.1),
            "separation double page y=0": (2454, "range", -1, 1),
            "page rotation 1": (0.01, "range", -0.1, 0.1),
            "page rotation 2": (-0.1, "range", -0.1, 0.1),
            "image 1 crop x1": (298, "range", -1, 1),
            "image 1 crop y1": (143, "range", -1, 1),
            "image 1 crop x2": (2308, "range", -1, 1),
            "image 1 crop y2": (3346, "range", -1, 1),
            "image 2 crop x1": (158, "range", -1, 1),
            "image 2 crop y1": (144, "range", -1, 1),
            "image 2 crop x2": (2172, "range", -1, 1),
            "image 2 crop y2": (3353, "range", -1, 1),
            "image 1 dpi": (300, "difference", 0.0000001),
            "image 1 recadre haut": (127, "range", -1, 1),
            "image 1 recadre bas": (157, "range", -1, 1),
            "image 1 recadre gauche": (225, "range", -1, 1),
            "image 1 recadre droite": (225, "range", -1, 1),
            "image 2 dpi": (300, "difference", 0.0000001),
            "image 2 recadre haut": (132, "range", -1, 1),
            "image 2 recadre bas": (146, "range", -1, 1),
            "image 2 recadre gauche": (223, "range", -1, 1),
            "image 2 recadre droite": (223, "range", -1, 1),
        },
    )


def test_image_failed_to_rotate_png() -> None:
    """If AngleLimitStddev is too small, the angle to rotate the image
    can not be computed.
    """
    treat_file(
        "image_failed_to_rotate.png",
        {
            "separation double page angle": (90.44, "range", -0.1, 0.1),
            "separation double page y=0": (2495, "range", -1, 1),
            "page rotation 1": (0.40, "range", -0.1, 0.1),
            "page rotation 2": (0.35, "range", -0.1, 0.1),
            "image 1 crop x1": (194, "range", -1, 1),
            "image 1 crop y1": (9, "range", -1, 1),
            "image 1 crop x2": (2439, "range", -1, 1),
            "image 1 crop y2": (3453, "range", -1, 1),
            "image 2 crop x1": (169, "range", -1, 1),
            "image 2 crop y1": (234, "range", -1, 1),
            "image 2 crop x2": (2250, "range", -1, 1),
            "image 2 crop y2": (3356, "range", -1, 1),
            "image 1 dpi": (300, "difference", 0.0000001),
            "image 1 recadre haut": (32, "range", -1, 1),
            "image 1 recadre bas": (32, "range", -1, 1),
            "image 1 recadre gauche": (118, "range", -1, 1),
            "image 1 recadre droite": (118, "range", -1, 1),
            "image 2 dpi": (300, "difference", 0.0000001),
            "image 2 recadre haut": (205, "range", -1, 1),
            "image 2 recadre bas": (160, "range", -1, 1),
            "image 2 recadre gauche": (189, "range", -1, 1),
            "image 2 recadre droite": (189, "range", -1, 1),
        },
    )
