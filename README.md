# Speech Assistant
SpeechToSpeechAssistant is a powerful tool that utilizes the Whisper API for speech transcription. It leverages the advanced capabilities of OpenAI's GPT-3 or GPT-4 (depending on the size of the transcription) to provide intelligent responses. Additionally, Elevenlabs' text-to-speech technology is employed for high-quality audio output.

Todo:
- [X] Create CLI version
- [ ] Add webgui
- [ ] Use with other LLM's

## Installation Instructions
To set up the Speech Assistant, follow these steps:

```
git clone https://github.com/Slaymish/SpeechToSpeechAssistant
cd SpeechToSpeechAssistant
mkdir Transcripts
mkdir Responses
cp env.template .env
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

Note: Make sure to obtain appropriate API keys and credentials for the Openai API and Elevenlabs' text-to-speech service before running the program. Place these in your .env file

***
#### 📝 License

Copyright © 2023 [Hamish Burke](https://github.com/Slaymish). <br />
This project is [MIT](https://github.com/Slaymish/SpeechToSpeechAssistant/blob/main/LICENSE) licensed. 
