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
            "separation double page angle": (90.55, "difference", 0.1),
            "separation double page y=0": (2485, "difference", 1),
            "page rotation 1": (0.73, "difference", 0.1),
            "page rotation 2": (0.16, "difference", 0.1),
            "image 1 crop x1": (331, "difference", 1),
            "image 1 crop y1": (336, "difference", 1),
            "image 1 crop x2": (2342, "difference", 1),
            "image 1 crop y2": (3223, "difference", 1),
            "image 2 crop x1": (170, "difference", 1),
            "image 2 crop y1": (649, "difference", 1),
            "image 2 crop x2": (2184, "difference", 1),
            "image 2 crop y2": (3361, "difference", 1),
            "image 1 dpi": (300, "difference", 0.0000001),
            "image 1 recadre haut": (324, "difference", 1),
            "image 1 recadre bas": (276, "difference", 1),
            "image 1 recadre gauche": (224, "difference", 1),
            "image 1 recadre droite": (224, "difference", 1),
            "image 2 dpi": (300, "difference", 0.0000001),
            "image 2 recadre haut": (674, "difference", 1),
            "image 2 recadre bas": (101, "difference", 1),
            "image 2 recadre gauche": (223, "difference", 1),
            "image 2 recadre droite": (223, "difference", 1),
        },
    )


def test_2_pages_2_contours_png() -> None:
    """There is not one contour for the two pages,
    but one contour for each page.
    """
    treat_file(
        "2-pages-2-contours.png",
        {
            "separation double page angle": (90.22, "difference", 0.1),
            "separation double page y=0": (2487, "difference", 1),
            "page rotation 1": (0.08, "difference", 0.1),
            "page rotation 2": (0.25, "difference", 0.1),
            "image 1 crop x1": (1185, "difference", 1),
            "image 1 crop y1": (1720, "difference", 1),
            "image 1 crop x2": (1186, "difference", 1),
            "image 1 crop y2": (1721, "difference", 1),
            "image 2 crop x1": (108, "difference", 1),
            "image 2 crop y1": (241, "difference", 1),
            "image 2 crop x2": (2154, "difference", 1),
            "image 2 crop y2": (3240, "difference", 1),
            "image 1 dpi": (300, "difference", 0.0000001),
            "image 1 recadre haut": (1752, "difference", 1),
            "image 1 recadre bas": (1753, "difference", 1),
            "image 1 recadre gauche": (1239, "difference", 1),
            "image 1 recadre droite": (1239, "difference", 1),
            "image 2 dpi": (300, "difference", 0.0000001),
            "image 2 recadre haut": (240, "difference", 1),
            "image 2 recadre bas": (248, "difference", 1),
            "image 2 recadre gauche": (207, "difference", 1),
            "image 2 recadre droite": (207, "difference", 1),
        },
    )


def test_black_border_not_removed_png() -> None:
    """The border on the right is still there."""
    treat_file(
        "black-border-not-removed.png",
        {
            "separation double page angle": (89.97, "difference", 0.1),
            "separation double page y=0": (2454, "difference", 1),
            "page rotation 1": (0.01, "difference", 0.1),
            "page rotation 2": (-0.1, "difference", 0.1),
            "image 1 crop x1": (298, "difference", 1),
            "image 1 crop y1": (143, "difference", 1),
            "image 1 crop x2": (2308, "difference", 1),
            "image 1 crop y2": (3346, "difference", 1),
            "image 2 crop x1": (158, "difference", 1),
            "image 2 crop y1": (144, "difference", 1),
            "image 2 crop x2": (2172, "difference", 1),
            "image 2 crop y2": (3353, "difference", 1),
            "image 1 dpi": (300, "difference", 0.0000001),
            "image 1 recadre haut": (127, "difference", 1),
            "image 1 recadre bas": (157, "difference", 1),
            "image 1 recadre gauche": (225, "difference", 1),
            "image 1 recadre droite": (225, "difference", 1),
            "image 2 dpi": (300, "difference", 0.0000001),
            "image 2 recadre haut": (132, "difference", 1),
            "image 2 recadre bas": (146, "difference", 1),
            "image 2 recadre gauche": (223, "difference", 1),
            "image 2 recadre droite": (223, "difference", 1),
        },
    )


def test_image_failed_to_rotate_png() -> None:
    """If AngleLimitStddev is too small, the angle to rotate the image
    can not be computed.
    """
    treat_file(
        "image_failed_to_rotate.png",
        {
            "separation double page angle": (90.44, "difference", 0.1),
            "separation double page y=0": (2495, "difference", 1),
            "page rotation 1": (0.40, "difference", 0.1),
            "page rotation 2": (0.35, "difference", 0.1),
            "image 1 crop x1": (194, "difference", 1),
            "image 1 crop y1": (9, "difference", 1),
            "image 1 crop x2": (2439, "difference", 1),
            "image 1 crop y2": (3453, "difference", 1),
            "image 2 crop x1": (169, "difference", 1),
            "image 2 crop y1": (234, "difference", 1),
            "image 2 crop x2": (2250, "difference", 1),
            "image 2 crop y2": (3356, "difference", 1),
            "image 1 dpi": (300, "difference", 0.0000001),
            "image 1 recadre haut": (32, "difference", 1),
            "image 1 recadre bas": (32, "difference", 1),
            "image 1 recadre gauche": (118, "difference", 1),
            "image 1 recadre droite": (118, "difference", 1),
            "image 2 dpi": (300, "difference", 0.0000001),
            "image 2 recadre haut": (205, "difference", 1),
            "image 2 recadre bas": (160, "difference", 1),
            "image 2 recadre gauche": (189, "difference", 1),
            "image 2 recadre droite": (189, "difference", 1),
        },
    )
