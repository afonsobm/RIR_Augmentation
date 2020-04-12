import os

import numpy as np
from scipy.io.matlab import loadmat

from Models.AIR import AIR
from Models.AIRInfo import AIRInfo
from Util.LoadAIR import loadAIR

if __name__ == "__main__" :

    fileName = 'air_binaural_lecture_0_0_1.mat'
    airFile = loadAIR(fileName)
    pass
