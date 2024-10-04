import pytest
from app.main import app
from starlette.testclient import TestClient

client = TestClient(app)


@pytest.mark.asyncio
async def test_websocket():
    with client.websocket_connect("/ws") as websocket:
        # テストメッセージ送信
        websocket.send_json({"event": "greet", "content": "World"})
        # レスポンスを受信
        data = websocket.receive_json()
        assert data["status"] == 200
        assert data["content"] == "Hello, World!"
