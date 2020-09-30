import sys

sys.path.append("..")

import script

script.DEBUG = False

from multiprocessing import Process

PARALLEL = False

def run_cpu_tasks_in_parallel(tasks):
    if PARALLEL:
        running_tasks = [Process(target=task) for task in tasks]
        for running_task in running_tasks:
            running_task.start()
        for running_task in running_tasks:
            running_task.join()
    else:
        for task in tasks:
            task()


run_cpu_tasks_in_parallel(
    [
        # first good page
        lambda: script.SeparatePage().treat_file(
            "0001.png",
            {
                "separation double page angle": (90.7, "ecart", 0.3),
                "separation double page y=0": (2486, "pourcent", 0.005),
                "page rotation 1": (0.68, "ecart", 0.2),
                "page rotation 2": (0.15, "ecart", 0.2),
                "image 1 crop x1": (332, "ecart", 10),
                "image 1 crop y1": (336, "ecart", 10),
                "image 1 crop x2": (2343, "ecart", 10),
                "image 1 crop y2": (3222, "ecart", 10),
                "image 2 crop x1": (169, "ecart", 10),
                "image 2 crop y1": (649, "ecart", 10),
                "image 2 crop x2": (2182, "ecart", 10),
                "image 2 crop y2": (3361, "ecart", 10),
                "image 1 recadre gauche": (224, "ecart", 10),
                "image 1 recadre droite": (224, "ecart", 10),
                "image 1 recadre haut": (325, "ecart", 10),
                "image 1 recadre bas": (276, "ecart", 10),
                "image 2 recadre gauche": (223, "ecart", 10),
                "image 2 recadre droite": (223, "ecart", 10),
                "image 2 recadre haut": (678, "ecart", 10),
                "image 2 recadre bas": (97, "ecart", 10),
                "image 1 dpi": (300, "ecart", 0.0000001),
                "image 2 dpi": (300, "ecart", 0.0000001),
            },
        ),
        # There is not one contour for the two pages,
        # but one contour for each page.
        lambda: script.SeparatePage().treat_file(
            "2-pages-2-contours.png",
            {
                "separation double page angle": (90.3, "ecart", 0.3),
                "separation double page y=0": (2494, "pourcent", 0.005),
                "page rotation 1": (0.08, "ecart", 1),
                "page rotation 2": (0.39, "ecart", 0.2),
                "image 1 crop x1": (1188, "ecart", 10),
                "image 1 crop y1": (1720, "ecart", 10),
                "image 1 crop x2": (1189, "ecart", 10),
                "image 1 crop y2": (1721, "ecart", 10),
                "image 2 crop x1": (104, "ecart", 10),
                "image 2 crop y1": (241, "ecart", 10),
                "image 2 crop x2": (2149, "ecart", 10),
                "image 2 crop y2": (3239, "ecart", 10),
                "image 1 recadre gauche": (1239, "ecart", 10),
                "image 1 recadre droite": (1239, "ecart", 10),
                "image 1 recadre haut": (1752, "ecart", 10),
                "image 1 recadre bas": (1753, "ecart", 10),
                "image 2 recadre gauche": (207, "ecart", 10),
                "image 2 recadre droite": (207, "ecart", 10),
                "image 2 recadre haut": (228, "ecart", 10),
                "image 2 recadre bas": (261, "ecart", 10),
                "image 1 dpi": (300, "ecart", 0.0000001),
                "image 2 dpi": (300, "ecart", 0.0000001),
            },
        ),
        # The border on the right is still there.
        lambda: script.SeparatePage().treat_file(
            "black-border-not-removed.png",
            {
                "separation double page angle": (90.17, "ecart", 0.3),
                "separation double page y=0": (2465, "pourcent", 0.005),
                "page rotation 1": (-0.02, "ecart", 0.2),
                "page rotation 2": (0.03, "ecart", 0.2),
                "image 1 crop x1": (297, "ecart", 10),
                "image 1 crop y1": (144, "ecart", 10),
                "image 1 crop x2": (2309, "ecart", 10),
                "image 1 crop y2": (3346, "ecart", 10),
                "image 2 crop x1": (157, "ecart", 10),
                "image 2 crop y1": (146, "ecart", 10),
                "image 2 crop x2": (2167, "ecart", 10),
                "image 2 crop y2": (3351, "ecart", 10),
                "image 1 recadre gauche": (222, "ecart", 10),
                "image 1 recadre droite": (222, "ecart", 10),
                "image 1 recadre haut": (128, "ecart", 10),
                "image 1 recadre bas": (159, "ecart", 10),
                "image 2 recadre gauche": (223, "ecart", 10),
                "image 2 recadre droite": (223, "ecart", 10),
                "image 2 recadre haut": (132, "ecart", 10),
                "image 2 recadre bas": (147, "ecart", 10),
                "image 1 dpi": (300, "ecart", 0.0000001),
                "image 2 dpi": (300, "ecart", 0.0000001),
            },
        ),
        # If AngleLimitStddev is too small, the angle to rotate the image
        # can not be computed.
        lambda: script.SeparatePage().treat_file(
            "image_failed_to_rotate.png",
            {
                "separation double page angle": (90.40, "ecart", 0.3),
                "separation double page y=0": (2494, "pourcent", 0.005),
                "page rotation 1": (0.41, "ecart", 0.2),
                "page rotation 2": (0.37, "ecart", 0.2),
                "image 1 crop x1": (91, "ecart", 10),
                "image 1 crop y1": (13, "ecart", 10),
                "image 1 crop x2": (2449, "ecart", 10),
                "image 1 crop y2": (3486, "ecart", 10),
                "image 2 crop x1": (169, "ecart", 10),
                "image 2 crop y1": (234, "ecart", 10),
                "image 2 crop x2": (2248, "ecart", 10),
                "image 2 crop y2": (3355, "ecart", 10),
                "image 1 recadre gauche": (61, "ecart", 10),
                "image 1 recadre droite": (61, "ecart", 10),
                "image 1 recadre haut": (17, "ecart", 10),
                "image 1 recadre bas": (17, "ecart", 10),
                "image 2 recadre gauche": (190, "ecart", 10),
                "image 2 recadre droite": (190, "ecart", 10),
                "image 2 recadre haut": (205, "ecart", 10),
                "image 2 recadre bas": (161, "ecart", 10),
                "image 1 dpi": (300, "ecart", 0.0000001),
                "image 2 dpi": (300, "ecart", 0.0000001),
            },
        ),
    ]
)
