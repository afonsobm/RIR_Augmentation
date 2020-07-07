import os

import numpy as np
from scipy.io.matlab import loadmat

from Models.AIR import AIR
from Models.AIRInfo import AIRInfo
from Util.LoadAIR import load_air

if __name__ == "__main__" :

    for fileName in open('load_air_files.txt', 'r'):
        
        fileName = fileName.rstrip()
        print(fileName)
        airFile = load_air(fileName)
        pass
