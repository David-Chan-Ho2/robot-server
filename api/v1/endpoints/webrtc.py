from fastapi import APIRouter, Request
from aiortc import RTCPeerConnection, RTCSessionDescription
from fastapi.responses import JSONResponse
from config.webrtc import WebcamTrack

pcs = set()

router = APIRouter()

@router.post("/offer")
async def offer(request: Request):
    params = await request.json()
    pc = RTCPeerConnection()
    pcs.add(pc)

    pc.addTrack(WebcamTrack())

    await pc.setRemoteDescription(RTCSessionDescription(
        sdp=params["sdp"], type=params["type"]
    ))
    answer = await pc.createAnswer()
    await pc.setLocalDescription(answer)

    return JSONResponse({
        "sdp": pc.localDescription.sdp,
        "type": pc.localDescription.type
    })
