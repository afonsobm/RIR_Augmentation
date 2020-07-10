import math as m

import numpy as np
from scipy import signal

from Constants.AIRContants import AIRConstants
from Models.AIR import AIR
from Models.AIRInfo import AIRInfo
from Util.IRUtil import earlyResponseIR, lateResponseIR


def augmentRIR(air: AIR) -> np.ndarray:
    earlyIR: np.ndarray
    lateIR: np.ndarray
    drr: float
    alpha: float

    # Retrieving early/late responses
    earlyIR = earlyResponseIR(air.data, air.airInfo.fs, AIRConstants.DELAY_THRESHOLD, AIRConstants.TOLERANCE_WINDOW)
    lateIR = lateResponseIR(air.data, air.airInfo.fs, AIRConstants.DELAY_THRESHOLD, AIRConstants.TOLERANCE_WINDOW)

    # Calculating DRR
    drr = calculateDRR(air, earlyIR, lateIR)

    # Calculating Alpha Scalar to DRR
    alpha = calculateAlpha(drr, air.airInfo.fs, earlyIR, lateIR)

def calculateAlpha(drr: float, fs: float, earlyIR: np.ndarray, lateIR: np.ndarray) -> float:
    hannWindow: np.ndarray
    earlyIR_NP: np.ndarray
    coefA: float
    coefB: float
    coefC: float
    alphaRoots: np.ndarray

    # Generating Hann Windows and removing zeroes on earlyIR
    hannWindow = signal.hann(m.ceil((fs * AIRConstants.HANN_WINDOW_SIZE)/float(1000)))

    ### TODO: Verify if earlyIR_NP is correct to properly multiply hannWindow
    earlyIR_NP = np.take(earlyIR, np.where(np.abs(earlyIR) > 0))
    ############################################################

    # Prevent uneven sized arrays between hannWindow and earlyIR
    if np.size(earlyIR_NP) > np.size(hannWindow):
        earlyIR_NP = earlyIR_NP[0:np.size(hannWindow)]
    elif np.size(hannWindow) < np.size(hannWindow):
        hannWindow = hannWindow[0:np.size(earlyIR_NP)]
    
    # Calculating the maximum root of the quadratic equation to retrieve alpha
    coefA = np.sum(np.square(hannWindow) * np.square(earlyIR_NP))
    coefB = 2 * np.sum((1 - hannWindow) * hannWindow * np.square(earlyIR_NP))
    coefC = np.sum(np.square(1 - hannWindow) * np.square(earlyIR_NP)) - (np.sum(lateIR) * m.pow(10, drr/float(10)))

    disc = m.pow(coefB, 2) - 4 * coefA * coefC
    alphaRoots = np.array((-coefB + m.sqrt(disc))/(2*coefA), 'float')
    alphaRoots = np.append(alphaRoots, (-coefB - m.sqrt(disc))/(2*coefA))
    
    return np.max(alphaRoots)

def calculateDRR(air: AIR, earlyIR: np.ndarray, lateIR: np.ndarray) -> float:
    
    drr = 10 * m.log10( np.sum(np.square(earlyIR)) / float(np.sum(np.square(lateIR))) )   
    return drr
