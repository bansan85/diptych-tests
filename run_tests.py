import sys

sys.path.append("..")

import script

script.DEBUG = False

from multiprocessing import Process


def run_cpu_tasks_in_parallel(tasks):
    running_tasks = [Process(target=task) for task in tasks]
    for running_task in running_tasks:
        running_task.start()
    for running_task in running_tasks:
        running_task.join()


run_cpu_tasks_in_parallel(
    [
        # first good page
        lambda: script.SeparatePage().treat_file(
            "0001.png",
            {
                "separation contour double": (0, "ecart", 0),
                "separation double page angle": (90.7, "ecart", 0.2),
                "separation double page y=0": (2486, "pourcent", 0.002),
                "page rotation 1": (0.68, "ecart", 0.2),
                "page rotation 2": (0.15, "ecart", 0.2),
                "image 1 crop x1": (332, "ecart", 5),
                "image 1 crop y1": (336, "ecart", 5),
                "image 1 crop x2": (2343, "ecart", 5),
                "image 1 crop y2": (3222, "ecart", 5),
                "image 2 crop x1": (169, "ecart", 5),
                "image 2 crop y1": (649, "ecart", 5),
                "image 2 crop x2": (2182, "ecart", 5),
                "image 2 crop y2": (3361, "ecart", 5),
                "image 1 dpi": (300, "ecart", 0.0000001),
                "image 2 dpi": (300, "ecart", 0.0000001),
            },
        ),
        lambda: script.SeparatePage().treat_file(
            "2-pages-2-contours.png",
            {
                "separation contour double": (1, "ecart", 0),
                "separation double page angle": (90.3, "ecart", 0.2),
                "separation double page y=0": (2494, "pourcent", 0.002),
                "page rotation 1": (0.08, "ecart", 1),
                "page rotation 2": (0.39, "ecart", 0.2),
                "image 1 crop x1": (1188, "ecart", 5),
                "image 1 crop y1": (1720, "ecart", 5),
                "image 1 crop x2": (1189, "ecart", 5),
                "image 1 crop y2": (1721, "ecart", 5),
                "image 2 crop x1": (104, "ecart", 5),
                "image 2 crop y1": (241, "ecart", 5),
                "image 2 crop x2": (2149, "ecart", 5),
                "image 2 crop y2": (3239, "ecart", 5),
                "image 1 dpi": (300, "ecart", 0.0000001),
                "image 2 dpi": (300, "ecart", 0.0000001),
            },
        ),
    ]
)
