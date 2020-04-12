import os

import numpy as np
from scipy.io import loadmat

from Models.AIR import AIR
from Models.AIRInfo import AIRInfo

airLibPath = os.path.normpath(os.getenv("AIR_LIB_PATH"))

def loadAIR(fileName: str) -> AIR:
    
    airFile = loadmat(os.path.join(airLibPath, fileName))
    airFileInfo = airFile.get("air_info")

    infoValues = airFileInfo[0,0]
    infoNames = airFileInfo[0,0].dtype.names

    air = AIR(airFile.get("h_air")[0], generateAIRInfo(infoValues, infoNames))

    return air

def generateAIRInfo(infoValues: np.ndarray, infoNames: tuple) -> AIRInfo:
    
    airInfo = AIRInfo()

    airInfo.description = infoValues[infoNames.index("description")][0]
    airInfo.precision = infoValues[infoNames.index("precision")][0]
    airInfo.room = infoValues[infoNames.index("room")][0]
    airInfo.head = infoValues[infoNames.index("head")][0][0]
    airInfo.distance = infoValues[infoNames.index("distance")][0][0]
    airInfo.fs = infoValues[infoNames.index("fs")][0][0]
    airInfo.channel = infoValues[infoNames.index("channel")][0][0]
    airInfo.filename = infoValues[infoNames.index("filename")][0]
    
    # airInfo.description = infoValues[infoNames.index("description")][0]
    # airInfo.precision = infoValues[infoNames.index("precision")][0]
    # airInfo.room = infoValues[infoNames.index("room")][0]
    # airInfo.head = infoValues[infoNames.index("head")][0][0]
    # airInfo.distance = infoValues[infoNames.index("distance")][0][0]
    # airInfo.fs = infoValues[infoNames.index("fs")][0][0]
    # airInfo.channel = infoValues[infoNames.index("channel")][0][0]
    # airInfo.filename = infoValues[infoNames.index("filename")][0]

    return airInfo
