import os

import numpy as np
from scipy.io import loadmat

from Models.AIR import AIR
from Models.AIRInfo import AIRInfo

airLibPath = os.path.normpath(os.getenv("AIR_LIB_PATH"))


def load_air(file_name: str) -> AIR:
    
    air_file = loadmat(os.path.join(airLibPath, file_name))
    air_file_info = air_file.get("air_info")

    info_values = air_file_info[0,0]
    info_names = air_file_info[0,0].dtype.names

    air = AIR(air_file.get("h_air")[0], generate_air_info(info_values, info_names))

    return air


def generate_air_info(info_values: np.ndarray, info_names: tuple) -> AIRInfo:
    
    air_info = AIRInfo()

    if "angle" in info_names:
        air_info.angle = info_values[info_names.index("angle")][0][0]
    if "azimuth_angle" in info_names:
        air_info.azimuth_angle = info_values[info_names.index("azimuth_angle")][0][0]
    if "cal_plate" in info_names:
        air_info.cal_plate = info_values[info_names.index("cal_plate")][0][0]
    if "channel" in info_names:
        air_info.channel = info_values[info_names.index("channel")][0][0]
    if "contact_pressure" in info_names:
        air_info.contact_pressure = info_values[info_names.index("contact_pressure")][0][0]
    if "d_height" in info_names:
        air_info.d_height = info_values[info_names.index("d_height")][0][0]
    if "d_mic_mic" in info_names:
        air_info.d_mic_mic = info_values[info_names.index("d_mic_mic")][0][0]
    if "d_speaker_mic" in info_names:
        air_info.d_speaker_mic = info_values[info_names.index("d_speaker_mic")][0][0]
    if "description" in info_names:
        air_info.description = info_values[info_names.index("description")][0]
    if "distance" in info_names:
        air_info.distance = info_values[info_names.index("distance")][0][0]
    if "erp_dist" in info_names:
        air_info.erp_dist = info_values[info_names.index("erp_dist")][0][0]
    if "excitation" in info_names:
        air_info.excitation = info_values[info_names.index("excitation")][0]
    if "filename" in info_names:
        air_info.filename = info_values[info_names.index("filename")][0]
    if "fs" in info_names:
        air_info.fs = info_values[info_names.index("fs")][0][0]
    if "head" in info_names:
        air_info.head = info_values[info_names.index("head")][0][0]
    if "HHP_xyz" in info_names:
        air_info.HHP_xyz = info_values[info_names.index("HHP_xyz")][0]
    if "mic_height" in info_names:
        air_info.mic_height = info_values[info_names.index("mic_height")][0][0]
    if "microphone" in info_names:
        air_info.microphone = info_values[info_names.index("microphone")][0]
    if "misc" in info_names and info_values[info_names.index("misc")].shape[0] > 1:
        air_info.misc = info_values[info_names.index("misc")][0]
    if "mock_up_type" in info_names:
        air_info.mock_up_type = info_values[info_names.index("mock_up_type")][0]
    if "mrp_height" in info_names:
        air_info.mrp_height = info_values[info_names.index("mrp_height")][0][0]
    if "phone_pos" in info_names:
        air_info.phone_pos = info_values[info_names.index("phone_pos")][0]
    if "pinna" in info_names:
        air_info.pinna = info_values[info_names.index("pinna")][0][0]
    if "precision" in info_names:
        air_info.precision = info_values[info_names.index("precision")][0]
    if "rir_method" in info_names:
        air_info.rir_method = info_values[info_names.index("rir_method")][0]
    if "rir_type" in info_names:
        air_info.rir_type = info_values[info_names.index("rir_type")][0]
    if "room" in info_names:
        air_info.room = info_values[info_names.index("room")][0]
    if "torso" in info_names:
        air_info.torso = info_values[info_names.index("torso")][0][0]
    if "version" in info_names:
        air_info.version = info_values[info_names.index("version")][0]

    return air_info
