from typing import Any, Optional, Tuple

import script
from page.split import SplitTwoWavesParameters
from page.unskew import UnskewPageParameters
from page.crop import CropAroundDataInPageParameters


class MockDisableSeparatePage(script.SeparatePage):
    def __init__(self, stop_at: int = 99):
        self.__stop_at = stop_at

    def split_two_waves(
        self,
        image: Any,
        parameters: SplitTwoWavesParameters,
        enable_debug: Optional[str],
    ) -> Tuple[Any, Any]:
        if self.__stop_at > 0:
            return super().split_two_waves(image, parameters, enable_debug)
        return (0, 0)

    def unskew_page(
        self,
        image: Any,
        n_page: int,
        parameters: UnskewPageParameters,
        enable_debug: Optional[str],
    ) -> Any:
        if self.__stop_at > 1:
            return super().unskew_page(image, n_page, parameters, enable_debug)
        return 0

    def crop_around_data_in_page(
        self,
        image: Any,
        n_page: int,
        parameters: CropAroundDataInPageParameters,
        enable_debug: Optional[str],
    ) -> Tuple[Any, Tuple[int, int, int, int], int, int]:
        if self.__stop_at > 2:
            return super().crop_around_data_in_page(
                image, n_page, parameters, enable_debug
            )
        return (0, (0, 0, 0, 0), 0, 0)

    def uncrop_to_fit_size(
        self,
        image: Any,
        n_page: int,
        size_wh: Tuple[int, int],
        crop: Tuple[int, int, int, int],
    ) -> Any:
        if self.__stop_at > 3:
            return super().uncrop_to_fit_size(image, n_page, size_wh, crop)
        return 0

    def save_final_page(self, filename: str, image: Any) -> None:
        if self.__stop_at > 4:
            super().save_final_page(filename, image)

    __stop_at: int
