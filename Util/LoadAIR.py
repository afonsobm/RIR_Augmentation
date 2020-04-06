import os
from scipy.io import loadmat

airLibPath = os.path.normpath(os.getenv("AIR_LIB_PATH"))

def loadAIR(fileName: str):
    
    airFile = loadmat(os.path.join(airLibPath, fileName))
    return airFile