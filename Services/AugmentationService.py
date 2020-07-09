import math as m
import numpy as np

from Models.AIR import AIR
from Models.AIRInfo import AIRInfo
from Util.IRUtil import earlyResponseIR, lateResponseIR
from Constants.AIRContants import AIRConstants


def augmentAIR():
    raise NotImplementedError

def calculateDRR(air: AIR):
    earlyIR: np.ndarray
    lateIR: np.ndarray
    drr: float

    # Retrieving early/late responses
    earlyIR = earlyResponseIR(air.data, air.airInfo.fs, AIRConstants.DELAY_THRESHOLD, AIRConstants.TOLERANCE_WINDOW)
    lateIR = lateResponseIR(air.data, air.airInfo.fs, AIRConstants.DELAY_THRESHOLD, AIRConstants.TOLERANCE_WINDOW)

    # Calculating DRR
    drr = 10 * m.log10( np.sum(np.square(earlyIR))[0] / float(np.sum(np.square(lateIR))[0]) )

    return drr



