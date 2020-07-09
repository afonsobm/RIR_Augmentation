import numpy as np
import math as m

def earlyResponseIR(ir_data: np.ndarray, fs: int, threshold: float, tolerance: float) -> np.ndarray:

    earlyResponseData = ir_data.copy()
    sampleWindowSize = m.ceil((fs * tolerance)/float(1000))
    delaySize = np.argmax(ir_data > threshold)

    earlyResponseData[0:(delaySize - sampleWindowSize)] = 0
    earlyResponseData[(delaySize + sampleWindowSize):] = 0
    
    return earlyResponseData

    
def lateResponseIR(ir_data: np.ndarray, fs: int, threshold: float, tolerance: float) -> np.ndarray:

    lateResponseData = ir_data.copy()
    sampleWindowSize = m.ceil((fs * tolerance)/float(1000))
    delaySize = np.argmax(ir_data > threshold)

    lateResponseData[(delaySize - sampleWindowSize):(delaySize + sampleWindowSize)] = 0

    return lateResponseData