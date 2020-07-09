import numpy as np

class AIRInfo:
    __angle: int
    __azimuth_angle: int
    __cal_plate: int
    __channel: int
    __contact_pressure: int
    __d_height: float
    __d_mic_mic: float
    __d_speaker_mic: float
    __description: str
    __distance: float
    __erp_dist: float
    __excitation: str
    __filename: str
    __fs: int
    __head: int
    __hhp_xyz: np.ndarray
    __mic_height: float
    __microphone: str
    __misc: str
    __mock_up_type: str
    __mrp_height: float
    __phone_pos: str
    __pinna: float
    __precision: str
    __rir_method: str
    __rir_type: str
    __room: str
    __torso: int
    __version: str

    def __init__(self, angle: int, azimuth_angle: int, cal_plate: int, channel: int, contact_pressure: int, d_height: float, d_mic_mic: float, d_speaker_mic: float, description: str, distance: float, erp_dist: float, excitation: str, filename: str, fs: int, head: int, hhp_xyz: np.ndarray, mic_height: float, microphone: str, misc: str, mock_up_type: str, mrp_height: float, phone_pos: str, pinna: float, precision: str, rir_method: str, rir_type: str, room: str, torso: int, version: str) -> None:
        self.__angle = angle
        self.__azimuth_angle = azimuth_angle
        self.__cal_plate = cal_plate
        self.__channel = channel
        self.__contact_pressure = contact_pressure
        self.__d_height = d_height
        self.__d_mic_mic = d_mic_mic
        self.__d_speaker_mic = d_speaker_mic
        self.__description = description
        self.__distance = distance
        self.__erp_dist = erp_dist
        self.__excitation = excitation
        self.__filename = filename
        self.__fs = fs
        self.__head = head
        self.__hhp_xyz = hhp_xyz
        self.__mic_height = mic_height
        self.__microphone = microphone
        self.__misc = misc
        self.__mock_up_type = mock_up_type
        self.__mrp_height = mrp_height
        self.__phone_pos = phone_pos
        self.__pinna = pinna
        self.__precision = precision
        self.__rir_method = rir_method
        self.__rir_type = rir_type
        self.__room = room
        self.__torso = torso
        self.__version = version

    __init__.__defaults__ = tuple(None for name in __init__.__code__.co_varnames) 

    @property
    def fs(self):
        return self.__fs

    @fs.setter
    def fs(self, fs):
        self.__fs = fs

    @property
    def filename(self):
        return self.__filename

    @filename.setter
    def filename(self, filename):
        self.__filename = filename