from app.schemas.message import Message
from app.services.message_service import handle_message
from fastapi import APIRouter, WebSocket

router = APIRouter()


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_json()
        message = Message(**data)
        response = await handle_message(message)
        await websocket.send_json(response.dict())
