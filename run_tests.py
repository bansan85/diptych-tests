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
                "page rotation 1": (0.8, "ecart", 0.2),
                "page rotation 2": (0.0, "ecart", 0.2),
                "image 1 crop x1": (331, "pourcent", 0.01),
                "image 1 crop y1": (337, "pourcent", 0.01),
                "image 1 crop x2": (2343, "pourcent", 0.002),
                "image 1 crop y2": (3223, "pourcent", 0.002),
                "image 2 crop x1": (168, "pourcent", 0.01),
                "image 2 crop y1": (648, "pourcent", 0.01),
                "image 2 crop x2": (2181, "pourcent", 0.002),
                "image 2 crop y2": (3362, "pourcent", 0.002),
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
                "page rotation 1": (0.0, "ecart", 0.2),
                "page rotation 2": (0.0, "ecart", 0.2),
                "image 1 crop x1": (2474, "pourcent", 0.01),
                "image 1 crop y1": (3466, "pourcent", 0.01),
                "image 1 crop x2": (98, "pourcent", 0.002),
                "image 1 crop y2": (23, "pourcent", 0.002),
                "image 2 crop x1": (96, "pourcent", 0.01),
                "image 2 crop y1": (241, "pourcent", 0.01),
                "image 2 crop x2": (2148, "pourcent", 0.002),
                "image 2 crop y2": (3242, "pourcent", 0.002),
                "image 1 dpi": (300, "ecart", 0.0000001),
                "image 2 dpi": (300, "ecart", 0.0000001),
            },
        ),
    ]
)
