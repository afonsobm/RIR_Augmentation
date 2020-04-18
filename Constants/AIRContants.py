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