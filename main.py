import os

import numpy as np
from scipy.io.matlab import loadmat

from Models.AIR import AIR
from Models.AIRInfo import AIRInfo
from Util.LoadAIR import loadAIR

airLibPath = os.path.normpath(os.getenv("AIR_LIB_PATH"))

if __name__ == "__main__" :

    # fileName = 'air_binaural_lecture_0_0_1.mat'
    # airFile = loadAIR(fileName)

    fileNames = os.listdir(airLibPath)
    allInfo = ["JOGAR_FORA"]

    for fileName in fileNames:
        if (str.startswith(fileName, "air")):
            
            airFile = loadmat(os.path.join(airLibPath, fileName))
            airFileInfo = airFile.get("air_info")
            infoValues = airFileInfo[0,0]
            infoNames = airFileInfo[0,0].dtype.names

    allInfo = list(set(allInfo))
    cacilds = 2
    pass
