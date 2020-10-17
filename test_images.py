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
            "separation double page angle": (90.7, "difference", 0.3),
            "separation double page y=0": (2486, "difference", 10),
            "page rotation 1": (0.68, "difference", 0.2),
            "page rotation 2": (0.15, "difference", 0.2),
            "image 1 crop x1": (332, "difference", 10),
            "image 1 crop y1": (336, "difference", 10),
            "image 1 crop x2": (2343, "difference", 10),
            "image 1 crop y2": (3222, "difference", 10),
            "image 2 crop x1": (169, "difference", 10),
            "image 2 crop y1": (649, "difference", 10),
            "image 2 crop x2": (2182, "difference", 10),
            "image 2 crop y2": (3361, "difference", 10),
            "image 1 recadre gauche": (224, "difference", 10),
            "image 1 recadre droite": (224, "difference", 10),
            "image 1 recadre haut": (325, "difference", 10),
            "image 1 recadre bas": (276, "difference", 10),
            "image 2 recadre gauche": (223, "difference", 10),
            "image 2 recadre droite": (223, "difference", 10),
            "image 2 recadre haut": (678, "difference", 10),
            "image 2 recadre bas": (97, "difference", 10),
            "image 1 dpi": (300, "difference", 0.0000001),
            "image 2 dpi": (300, "difference", 0.0000001),
        },
    )


def test_2_pages_2_contours_png() -> None:
    """There is not one contour for the two pages,
    but one contour for each page.
    """
    treat_file(
        "2-pages-2-contours.png",
        {
            "separation double page angle": (90.3, "difference", 0.3),
            "separation double page y=0": (2494, "pourcent", 0.005),
            "page rotation 1": (0.08, "difference", 1),
            "page rotation 2": (0.39, "difference", 0.2),
            "image 1 crop x1": (1188, "difference", 10),
            "image 1 crop y1": (1720, "difference", 10),
            "image 1 crop x2": (1189, "difference", 10),
            "image 1 crop y2": (1721, "difference", 10),
            "image 2 crop x1": (104, "difference", 10),
            "image 2 crop y1": (241, "difference", 10),
            "image 2 crop x2": (2149, "difference", 10),
            "image 2 crop y2": (3239, "difference", 10),
            "image 1 recadre gauche": (1239, "difference", 10),
            "image 1 recadre droite": (1239, "difference", 10),
            "image 1 recadre haut": (1752, "difference", 10),
            "image 1 recadre bas": (1753, "difference", 10),
            "image 2 recadre gauche": (207, "difference", 10),
            "image 2 recadre droite": (207, "difference", 10),
            "image 2 recadre haut": (233, "difference", 10),
            "image 2 recadre bas": (255, "difference", 10),
            "image 1 dpi": (300, "difference", 0.0000001),
            "image 2 dpi": (300, "difference", 0.0000001),
        },
    )


def test_black_border_not_removed_png() -> None:
    """The border on the right is still there."""
    treat_file(
        "black-border-not-removed.png",
        {
            "separation double page angle": (90.17, "difference", 0.3),
            "separation double page y=0": (2465, "pourcent", 0.005),
            "page rotation 1": (-0.02, "difference", 0.2),
            "page rotation 2": (0.03, "difference", 0.2),
            "image 1 crop x1": (297, "difference", 10),
            "image 1 crop y1": (144, "difference", 10),
            "image 1 crop x2": (2309, "difference", 10),
            "image 1 crop y2": (3346, "difference", 10),
            "image 2 crop x1": (157, "difference", 10),
            "image 2 crop y1": (146, "difference", 10),
            "image 2 crop x2": (2167, "difference", 10),
            "image 2 crop y2": (3351, "difference", 10),
            "image 1 recadre gauche": (222, "difference", 10),
            "image 1 recadre droite": (222, "difference", 10),
            "image 1 recadre haut": (128, "difference", 10),
            "image 1 recadre bas": (159, "difference", 10),
            "image 2 recadre gauche": (223, "difference", 10),
            "image 2 recadre droite": (223, "difference", 10),
            "image 2 recadre haut": (132, "difference", 10),
            "image 2 recadre bas": (147, "difference", 10),
            "image 1 dpi": (300, "difference", 0.0000001),
            "image 2 dpi": (300, "difference", 0.0000001),
        },
    )


def test_image_failed_to_rotate_png() -> None:
    """If AngleLimitStddev is too small, the angle to rotate the image
    can not be computed.
    """
    treat_file(
        "image_failed_to_rotate.png",
        {
            "separation double page angle": (90.40, "difference", 0.3),
            "separation double page y=0": (2494, "pourcent", 0.005),
            "page rotation 1": (0.41, "difference", 0.2),
            "page rotation 2": (0.37, "difference", 0.2),
            "image 1 crop x1": (170, "difference", 10),
            "image 1 crop y1": (13, "difference", 10),
            "image 1 crop x2": (2471, "difference", 10),
            "image 1 crop y2": (3498, "difference", 10),
            "image 2 crop x1": (169, "difference", 10),
            "image 2 crop y1": (234, "difference", 10),
            "image 2 crop x2": (2248, "difference", 10),
            "image 2 crop y2": (3355, "difference", 10),
            "image 1 recadre gauche": (91, "difference", 10),
            "image 1 recadre droite": (91, "difference", 10),
            "image 1 recadre haut": (17, "difference", 10),
            "image 1 recadre bas": (17, "difference", 10),
            "image 2 recadre gauche": (190, "difference", 10),
            "image 2 recadre droite": (190, "difference", 10),
            "image 2 recadre haut": (205, "difference", 10),
            "image 2 recadre bas": (161, "difference", 10),
            "image 1 dpi": (300, "difference", 0.0000001),
            "image 2 dpi": (300, "difference", 0.0000001),
        },
    )
