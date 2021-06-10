import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from sepve import SEPVE

addr = 0x88

app = FastAPI(title='SEPVE-WebControl', version='1.0.0')

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

sepve = SEPVE(addr)


@app.post('/select_input/{input_id}')
def selectInput(input_id: int):
    sepve.setInputChannelFunction(channel=input_id)


@app.post('/intput_gain/{gain}')
def setInputGain(gain: int):
    sepve.setInputGainFunction(gain=gain)


@app.post('/volume/{volume}')
def setVolume(volume: int):
    sepve.setVolumeFunction(volume=volume)


@app.post('/bass_gain/{gain}')
def setBassGain(gain: int):
    sepve.setBassGainFunction(gain=gain)


@app.post('/mid_gain/{gain}')
def setMidGain(gain: int):
    sepve.setMidGainFunction(gain=gain)


@app.post('/treble_gain/{gain}')
def setTrebleGain(gain: int):
    sepve.setTrebleGainFunction(gain=gain)


@app.post('/speaker_att_r/{att}')
def setSpeakerAttR(att):
    sepve.setSpeakerAttRFunction(att=att)


@app.post('/speaker_att_l/{att}')
def setSpeakerAttL(att):
    sepve.setSpeakerAttLFunction(att=att)


if __name__ == "__main__":
    uvicorn.run(app, host="10.0.0.40", port=9000)
