from app.schemas.message import Message, ResponseMessage


async def handle_message(message: Message) -> ResponseMessage:
    # 簡易的なメッセージ処理例
    if message.event == "greet":
        response_content = f"Hello, {message.content}!"
    else:
        response_content = "Unknown event."

    return ResponseMessage(status=200, content=response_content)
