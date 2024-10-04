from app.utils.response_templates import (
    error_response_template,
    success_response_template,
)


def custom_openapi(app, default_openapi):
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = default_openapi()

    # WebSocketのエンドポイントに関するOpenAPIドキュメントを追加
    websocket_paths = {
        "/ws": {
            "post": {
                "summary": "WebSocket connection",
                "description": "Handle WebSocket connections and messages",
                "responses": {
                    "101": {"description": "Switching Protocols: WebSocket connection established"},
                    "200": {
                        "description": "Successful connection",
                        "content": {
                            "application/json": {"example": success_response_template({"info": "WebSocket connected"})}
                        },
                    },
                    "400": {
                        "description": "Connection error",
                        "content": {"application/json": {"example": error_response_template("Invalid room code")}},
                    },
                },
            }
        }
    }

    # WebSocketエンドポイントのドキュメントをスキーマに追加
    openapi_schema["paths"].update(websocket_paths)
    app.openapi_schema = openapi_schema
    return app.openapi_schema
