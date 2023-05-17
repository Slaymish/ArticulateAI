# Speech Assistant
The Speech Assistant is a powerful tool that utilizes the Whisper API for speech transcription. It leverages the advanced capabilities of OpenAI's GPT-3 or GPT-4 (depending on the size of the transcription) to provide intelligent responses. Additionally, Elevenlabs' text-to-speech technology is employed for high-quality audio output.

## Installation Instructions
To set up the Speech Assistant, follow these steps:

```
git clone https://github.com/Slaymish/SpeachAssistant
cd SpeachAssistant
mkdir Transcripts
mkdir Responses
touch .env
```

Install the required dependencies by running the following command:

```
pip install -r requirements.txt
```

Execute the script using:
```
python3 run.py
```

By following these instructions, you'll have the Speech Assistant up and running, ready to transcribe your speech and provide insightful responses.

Note: Make sure to obtain appropriate API keys and credentials for the Whisper API and Elevenlabs' text-to-speech service before running the program. **and save them to a .env file** in the pwd
