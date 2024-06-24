from os import name

from pydub import AudioSegment
from pydub.playback import play
import io
import asyncio
import websockets
import imageio_ffmpeg as ffmpeg

AudioSegment.converter = ffmpeg.get_ffmpeg_exe()
print(ffmpeg.get_ffmpeg_exe())


async def stream_audio():
    uri = "ws://localhost:8000/ws"
    async with websockets.connect(uri) as websocket:
        audio_data = io.BytesIO()

        try:
            while True:
                data = await websocket.recv()
                audio_data.write(data)

                # Проверяем, если данные закончились
                if len(data) == 0:
                    break

            audio_data.seek(0)
            song = AudioSegment.from_file(audio_data, format="mp3")
            play(song)
        except Exception as e:
            print(f"Error: {e}")


if name == "client":
    asyncio.run(stream_audio())