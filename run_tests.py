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
                "image 1 dpi": (300, "ecart", 0.0000001),
                "image 2 dpi": (300, "ecart", 0.0000001),
            },
        ),
        # The right border is still there.
        lambda: script.SeparatePage().treat_file(
            "black-border-not-removed.png",
            {
                "separation double page angle": (90.17, "ecart", 0.3),
                "separation double page y=0": (2465, "pourcent", 0.005),
                "page rotation 1": (-0.02, "ecart", 1),
                "page rotation 2": (0.03, "ecart", 0.2),
                "image 1 crop x1": (297, "ecart", 10),
                "image 1 crop y1": (144, "ecart", 10),
                "image 1 crop x2": (2309, "ecart", 10),
                "image 1 crop y2": (3346, "ecart", 10),
                "image 2 crop x1": (157, "ecart", 10),
                "image 2 crop y1": (146, "ecart", 10),
                "image 2 crop x2": (2167, "ecart", 10),
                "image 2 crop y2": (3351, "ecart", 10),
                "image 1 dpi": (300, "ecart", 0.0000001),
                "image 2 dpi": (300, "ecart", 0.0000001),
            },
        ),
    ]
)
