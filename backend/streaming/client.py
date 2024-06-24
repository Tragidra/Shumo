import asyncio
import websockets


async def stream_audio():
    uri = "ws://localhost:8000/ws"
    filename = "received_audio.mp3"

    async with websockets.connect(uri) as websocket:
        try:
            print("WebSocket connection opened.")
            with open(filename, "wb") as f:
                while True:
                    data = await websocket.recv()
                    if not data:
                        break
                    print(f"Received {len(data)} bytes.")
                    f.write(data)

            print("Finished receiving data.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            await websocket.close()
            print("WebSocket connection closed.")



asyncio.run(stream_audio())