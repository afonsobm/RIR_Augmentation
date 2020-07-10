# =======================================================
# GRADUATION PROJECT - ROOM IMPULSE RESPONSE AUGMENTATION
# =======================================================

# ================
# AUTHOR - VERSION
# ================

#   Author: Bruno Machado Afonso
#   Version: 1.0
#   Institution: Escola Politecnica - Universidade Federal do Rio de Janeiro (UFRJ), Rio de Janeiro, Brazil

# ===========
# DESCRIPTION
# ===========

#   This project is based on the implementation of the work presented on the following articles
        
        # 1) IMPULSE RESPONSE DATA AUGMENTATION AND DEEP NEURAL NETWORKS FOR BLIND ROOM ACOUSTIC PARAMETER ESTIMATION - Nicholas J. Bryan - Adobe Research, San Francisco, CA, USA
        # 2) A STUDY ON DATA AUGMENTATION OF REVERBERANT SPEECH FOR ROBUST SPEECH RECOGNITION - Tom Ko et al. - Huawei Noah’s Ark Research Lab, Hong Kong, China

#   The main objective is to create a method which generates artificial Room Impulse Response (RIR) by modifying the
#   Direct-to-Reverberant Ratio (DRR) and Reverberation Time (T60) parameters extracted from the RIR
#   Later, these can be aplied to speech signals to generate far-field speechs (using augmented RIR and artificial noises)


import os

import numpy as np
from scipy.io.matlab import loadmat

from Models.AIR import AIR
from Models.AIRInfo import AIRInfo
from Services.AugmentationService import augmentRIR, calculateDRR
from Util.LoadAIR import load_air

if __name__ == "__main__" :

    for fileName in open('load_air_files.txt', 'r'):
        
        fileName = fileName.rstrip()
        airFile = load_air(fileName)
        augmentRIR(airFile)
        pass
