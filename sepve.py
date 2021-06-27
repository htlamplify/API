from smbus2 import SMBus
from lookup_tables import *


class SEPVE:
    CURRENT_INPUT: int = 2
    INPUT_GAIN_dB: int = 28
    VOLUME: str = "MUTE"
    BASS_dB: int = 0
    MID_dB: int = 2
    TREBLE_dB: int = 2
    SPEAKER: str = "MUTE"
    i2c_addr = 0x44
    bus = None

    def __init__(self, addr):
        self.i2c_addr = addr
        self.bus = SMBus(1)

    def setInputChannelFunction(self, channel: int):
        self.bus.write_byte_data(self.i2c_addr, INPUT_SELECTOR.get("SUB_ADDR"), INPUT_SELECTOR.get(channel))

    def setInputGainFunction(self, gain: int):
        self.bus.write_byte_data(self.i2c_addr, INPUT_GAIN.get("SUB_ADDR"), INPUT_GAIN.get(gain))

    def setVolumeFunction(self, volume):
        if volume == "MUTE":
            volume = VOLUME.get("MUTE")
        self.bus.write_byte_data(self.i2c_addr, VOLUME.get("SUB_ADDR"), volume)

    def setBassGainFunction(self, gain: int):
        self.bus.write_byte_data(self.i2c_addr, BASS_GAIN.get("SUB_ADDR"), BASS_GAIN.get(gain))

    def setMidGainFunction(self, gain: int):
        self.bus.write_byte_data(self.i2c_addr, TREBLE_GAIN.get("SUB_ADDR"), TREBLE_GAIN.get(gain))

    def setTrebleGainFunction(self, gain: int):
        self.bus.write_byte_data(self.i2c_addr, TREBLE_GAIN.get("SUB_ADDR"), TREBLE_GAIN.get(gain))

    def setSpeakerAttRFunction(self, att):
        if att == "MUTE":
            att = SPEAKER_ATT_R.get("MUTE")
        self.bus.write_byte_data(self.i2c_addr, SPEAKER_ATT_R.get("SUB_ADDR"), att)

    def setSpeakerAttLFunction(self, att):
        if att == "MUTE":
            att = SPEAKER_ATT_L.get("MUTE")
        self.bus.write_byte_data(self.i2c_addr, SPEAKER_ATT_L.get("SUB_ADDR"), att)
