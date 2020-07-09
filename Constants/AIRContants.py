import sys

class AIRConstants:
    class ConstError(TypeError): pass
    def __setattr__(self,name,value):
        if self.__dict__.has_key(name):
            raise "Can't rebind constant(%s)"%name
        self.__dict__[name]=value

sys.modules[__name__] = AIRConstants()

RIR_TYPE = dict([
    (1, "binaural"),
    (2, "dual-channel")
])

# defines the intensity of the impulse response which will represent when the audio reached the microfone in the recording
DELAY_THRESHOLD = 0.001

# [miliseconds] defines the size of the tolerance window that will be used to retrieve the early/late impulse responses
TOLERANCE_WINDOW = 2.5