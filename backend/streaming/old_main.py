import asyncio
import aiofiles
from fastapi import FastAPI, WebSocket

app = FastAPI()


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    mp3_file_path = "source/nature.mp3"

    try:
        async with aiofiles.open(mp3_file_path, "rb") as mp3_file:
            while True:
                data = await mp3_file.read(4096)
                if not data:
                    break
                await websocket.send_bytes(data)
                await asyncio.sleep(0.1)
        print("Finished sending data.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        await websocket.close()
        print("WebSocket connection closed.")