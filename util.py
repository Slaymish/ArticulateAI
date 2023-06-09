import openai
import pyaudio
import wave
from elevenlabs import generate, stream, set_api_key
import datetime
import dotenv
from _thread import start_new_thread
import time


# Load environment variables from .env file
dotenv.load_dotenv()

# Define constants and config variables
WAVE_OUTPUT_FILENAME = "tempaudio.wav"
RECORD_SECONDS = 20

eleven_api = dotenv.get_key(dotenv_path=".env", key_to_get="ELEVEN_API_KEY")
openai_api_key = dotenv.get_key(dotenv_path=".env", key_to_get="OPENAI_API_KEY")

# Set API keys
openai.api_key = openai_api_key # openai api key
if eleven_api:
    set_api_key(eleven_api) # elevenlabs api key

def printcount(secs, recordLength):
    """Countdown timer for recording."""
    i = recordLength
    while i != 0:
        print("-- " + str(i) + " --", end='\r')
        i -= 1
        time.sleep(secs)

def text_to_speak(txt):
    """Converts text to speech using elevenlabs API."""
    if eleven_api:
        audio = generate(
            text=txt,
            voice="Antoni",
            model="eleven_monolingual_v1",
            stream=True
        )
        stream(audio)

def record_audio(RECORD_SECONDS):
    """Records audio for the specified duration and saves it as a WAV file."""
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    CHUNK = 1024

    audio = pyaudio.PyAudio()
    
    # Start recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
    print("recording...")
    frames = []
    
    start_new_thread(printcount, (1, RECORD_SECONDS))
    for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print("finished recording")
    
    # Stop recording
    stream.stop_stream()
    stream.close()
    audio.terminate()
    
    # Save audio data to WAV file
    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()
    print("Finished writing audio")

def get_custom_timestamp():
    """Returns a custom timestamp in the format: Hour-MinuteAM/PM-Day-MonthName"""
    now = datetime.datetime.now()
    timestamp = now.strftime("%I-%M%p-%-d-%B")
    return timestamp

def transribe_audio():
    """Transcribes the recorded audio using OpenAI's Whisper ASR system."""
    audio_file= open(WAVE_OUTPUT_FILENAME, "rb")
    return openai.Audio.transcribe("whisper-1", audio_file)

def chat_complete(starting_prompt, transcript):
    """Generates a chat completion using GPT-3.5-turbo or GPT-4 based on the length of the transcript."""
    model = "gpt-3.5-turbo"

    if transcript == "":
        transcript += "The user said nothing.\n\n"
    elif len(transcript) > 60:
        model = "gpt-4"
        print("---- Using SMART Mode (GPT-4) ----)")
    else: 
        print("---- Using FAST Mode (GPT-3.5-turbo) ----)")

    # Send transcript to GPT-3
    chat_completion = openai.ChatCompletion.create(
        model=model, 
        messages=[
            {"role": "system", "content": starting_prompt},
            {"role": "user", "content": transcript}
        ]
    )

    # Save response to file
    with open("Responses/" + get_custom_timestamp() + ".txt", "w") as file:
        file.write(chat_completion.choices[0].message.content)

    return chat_completion.choices[0].message.content
