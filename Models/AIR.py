from Models import AIRInfo
import numpy as np

class AIR:
    __data: np.ndarray
    __airInfo: AIRInfo

    def __init__(self, data: np.ndarray, airInfo: AIRInfo) -> None:
        self.__airInfo = airInfo
        self.__data = data

    __init__.__defaults__ = tuple(None for name in __init__.__code__.co_varnames)

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def airInfo(self):
        return self.__airInfo

    @airInfo.setter
    def airInfo(self, airInfo):
        self.__airInfo = airInfo