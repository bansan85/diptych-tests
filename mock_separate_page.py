import random
from typing import Dict, Optional, Tuple, Union

import numpy as np

from angle import Angle
from debug_image import DebugImage
from page.crop import CropAroundDataInPageParameters
from page.split import SplitTwoWavesParameters
from page.unskew import UnskewPageParameters
import script


class MockDisableSeparatePage(script.SeparatePage):
    def __init__(self, stop_at: int = 99, fuzzing: bool = False) -> None:
        self.__stop_at = stop_at
        self.__fuzzing = fuzzing

    def split_two_waves(
        self,
        image: np.ndarray,
        parameters: SplitTwoWavesParameters,
        debug: DebugImage,
    ) -> Tuple[np.ndarray, np.ndarray]:
        if self.__stop_at > 0:
            return super().split_two_waves(image, parameters, debug)
        return (np.empty(0), np.empty(0))

    def unskew_page(
        self,
        image: np.ndarray,
        n_page: int,
        parameters: UnskewPageParameters,
        debug: DebugImage,
    ) -> np.ndarray:
        if self.__stop_at > 1:
            return super().unskew_page(image, n_page, parameters, debug)
        return np.empty(0)

    def crop_around_data_in_page(
        self,
        image: np.ndarray,
        n_page: int,
        parameters: CropAroundDataInPageParameters,
        debug: DebugImage,
    ) -> Tuple[np.ndarray, Tuple[int, int, int, int], int, int]:
        if self.__stop_at > 2:
            return super().crop_around_data_in_page(
                image, n_page, parameters, debug
            )
        return (np.empty(0), (0, 0, 0, 0), 0, 0)

    def uncrop_to_fit_size(
        self,
        image: np.ndarray,
        n_page: int,
        size_wh: Tuple[int, int],
        crop: Tuple[int, int, int, int],
    ) -> np.ndarray:
        if self.__stop_at > 3:
            return super().uncrop_to_fit_size(image, n_page, size_wh, crop)
        return np.empty(0)

    def save_final_page(self, filename: str, image: np.ndarray) -> None:
        if self.__stop_at > 4:
            super().save_final_page(filename, image)

    def treat_file(
        self,
        filename: str,
        dict_test: Optional[
            Dict[
                str,
                Union[
                    Tuple[str, int, int],
                    Tuple[str, float, float],
                    Tuple[str, Angle, Angle],
                ],
            ]
        ] = None,
        dict_default_values: Optional[
            Dict[str, Union[int, float, Tuple[int, int], Angle]]
        ] = None,
        debug: Optional[DebugImage] = None,
    ) -> None:
        if debug is None:
            debug = DebugImage(DebugImage.Level.OFF)

        if dict_default_values is None:
            dict_default_values = {}

        if self.__fuzzing:
            dict_default_values["UnskewPageHoughLinesScale"] = random.uniform(
                0.30, 1.0
            )
            print(filename, dict_default_values)

        super().treat_file(filename, dict_test, dict_default_values, debug)

    __stop_at: int
    __fuzzing: bool
