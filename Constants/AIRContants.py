import sys

class classproperty(object):
    def __init__(self, f):
        self.f = f
    def __get__(self, obj, owner):
        return self.f(owner)

class AIRConstants:

    # defines the intensity of the impulse response which will represent when the audio reached the microfone in the recording
    DELAY_THRESHOLD: float = 0.0001

    # [miliseconds] defines the size of the tolerance window that will be used to retrieve the early/late impulse responses
    TOLERANCE_WINDOW: float = 2.5

    def __init__(self):
        pass

    __init__.__defaults__ = tuple(None for name in __init__.__code__.co_varnames)