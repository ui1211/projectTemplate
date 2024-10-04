
# WebSocket API

このプロジェクトは、FastAPIを使って構築されたシンプルなWebSocket APIです。

## インストール

必要なPythonパッケージをインストールします:

```bash
pip install fastapi uvicorn pydantic pytest pytest-asyncio
pip install -r requirements.txt
```

## サーバの起動
```bash
uvicorn app.main:app --reload
```

## ディレクトリ構造
```bash
project_root/
├── app/
│   ├── main.py                # 実行用スクリプト
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── websocket.py       # WebSocketエンドポイント定義
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── message.py         # JSON定義スクリプト（Pydanticモデル）
│   ├── services/
│   │   ├── __init__.py
│   │   ├── message_service.py # 各種処理スクリプト
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── documentation.py   # OpenAPI拡張用スクリプト
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── test_websocket.py  # シナリオ実行スクリプト（テスト）
├── requirements.txt           # 依存関係リスト
├── README.md                  # プロジェクトの説明

```