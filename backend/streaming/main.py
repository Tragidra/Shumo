import asyncio
import aiofiles
from fastapi import FastAPI, WebSocket
from starlette.responses import StreamingResponse

app = FastAPI()

@app.websocket("/audio_ws")
async def audio_ws_endpoint(websocket: WebSocket):
    await websocket.accept()

    try:
        mp3_file_path = "source/long_stra.mp3"
        async with aiofiles.open(mp3_file_path, "rb") as mp3_file:
            chunk = await mp3_file.read()
            while chunk:
                await websocket.send_bytes(chunk)
                chunk = await mp3_file.read(4096)
                await asyncio.sleep(0.1)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        await websocket.close()