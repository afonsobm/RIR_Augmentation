from Models import AIRInfo
import numpy as np

class AIR:
    _data: np.ndarray
    _airInfo: AIRInfo

    def __init__(self, data: np.ndarray, airInfo: AIRInfo) -> None:
        self._airInfo = airInfo
        self._data = data

    __init__.__defaults__ = tuple(None for name in __init__.__code__.co_varnames)

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    @property
    def airInfo(self):
        return self._airInfo

    @airInfo.setter
    def airInfo(self, airInfo):
        self._airInfo = airInfo