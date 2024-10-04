from app.routers import websocket
from app.utils.documentation import custom_openapi
from fastapi import FastAPI

app = FastAPI()

# デフォルトのOpenAPIスキーマ関数を保存
default_openapi = app.openapi

# WebSocketルーターの登録
app.include_router(websocket.router)

# カスタムOpenAPIスキーマ関数を設定
app.openapi = lambda: custom_openapi(app, default_openapi)


# ルートの定義
@app.get("/")
async def root():
    return {"message": "WebSocket API is running"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
