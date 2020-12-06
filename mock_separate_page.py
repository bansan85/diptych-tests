from typing import Optional, Tuple

import numpy as np

import script
from page.split import SplitTwoWavesParameters
from page.unskew import UnskewPageParameters
from page.crop import CropAroundDataInPageParameters


class MockDisableSeparatePage(script.SeparatePage):
    def __init__(self, stop_at: int = 99):
        self.__stop_at = stop_at

    def split_two_waves(
        self,
        image: np.ndarray,
        parameters: SplitTwoWavesParameters,
        enable_debug: Optional[str],
    ) -> Tuple[np.ndarray, np.ndarray]:
        if self.__stop_at > 0:
            return super().split_two_waves(image, parameters, enable_debug)
        return (np.empty(0), np.empty(0))

    def unskew_page(
        self,
        image: np.ndarray,
        n_page: int,
        parameters: UnskewPageParameters,
        enable_debug: Optional[str],
    ) -> np.ndarray:
        if self.__stop_at > 1:
            return super().unskew_page(image, n_page, parameters, enable_debug)
        return np.empty(0)

    def crop_around_data_in_page(
        self,
        image: np.ndarray,
        n_page: int,
        parameters: CropAroundDataInPageParameters,
        enable_debug: Optional[str],
    ) -> Tuple[np.ndarray, Tuple[int, int, int, int], int, int]:
        if self.__stop_at > 2:
            return super().crop_around_data_in_page(
                image, n_page, parameters, enable_debug
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

    __stop_at: int
