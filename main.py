import numpy as np
from Models.AIRInfo import AIRInfo
from Models.AIR import AIR

if __name__ == "__main__" :
    
    airInfo = AIRInfo(description="test",frequency=48e3,name="bla")
    print(airInfo.description)
    airInfo.description = "matera"
    print(airInfo.description)

    air = AIR()
    
