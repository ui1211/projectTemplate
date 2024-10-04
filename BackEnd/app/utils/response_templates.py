# レスポンステンプレートを定義
def success_response_template(data=None):
    return {
        "status": "success",
        "message": "Operation completed successfully",
        "data": data,
    }


def error_response_template(message="An error occurred"):
    return {
        "status": "error",
        "message": message,
        "data": None,
    }
