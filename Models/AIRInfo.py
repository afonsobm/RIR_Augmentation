class AIRInfo:
    angle: str
    azimuth_angle: str
    cal_plate: str
    channel: int
    contact: str
    contact_pressure: str
    d_height: str
    d_mic_mic: str
    d_speaker_mic: str
    description: str
    distance: int
    erp_dist: str
    excitation: str
    filename: str
    fs: int
    head: int
    hhp_xyz: str
    mic_height: str
    microphone: str
    misc: str
    mock_up_type: str
    mrp_height: str
    phone_pos: str
    pinna: str
    precision: str
    rir_method: str
    rir_type: str
    room: str
    torso: str
    version: str

    def __init__(self, angle: str, azimuth_angle: str, cal_plate: str, channel: int, contact: str, contact_pressure: str, copyright: str, d_height: str, d_mic_mic: str, d_speaker_mic: str, description: str, distance: int, erp_dist: str, excitation: str, filename: str, fs: int, head: int, hhp_xyz: str, mic_height: str, microphone: str, misc: str, mock_up_type: str, mrp_height: str, phone_pos: str, pinna: str, precision: str, rir_method: str, rir_type: str, room: str, torso: str, version: str) -> None:
        self.angle = angle
        self.azimuth_angle = azimuth_angle
        self.cal_plate = cal_plate
        self.channel = channel
        self.contact = contact
        self.contact_pressure = contact_pressure
        self.d_height = d_height
        self.d_mic_mic = d_mic_mic
        self.d_speaker_mic = d_speaker_mic
        self.description = description
        self.distance = distance
        self.erp_dist = erp_dist
        self.excitation = excitation
        self.filename = filename
        self.fs = fs
        self.head = head
        self.hhp_xyz = hhp_xyz
        self.mic_height = mic_height
        self.microphone = microphone
        self.misc = misc
        self.mock_up_type = mock_up_type
        self.mrp_height = mrp_height
        self.phone_pos = phone_pos
        self.pinna = pinna
        self.precision = precision
        self.rir_method = rir_method
        self.rir_type = rir_type
        self.room = room
        self.torso = torso
        self.version = version

        __init__.__defaults__ = tuple(None for name in __init__.__code__.co_varnames)