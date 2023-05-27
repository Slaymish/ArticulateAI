<h1 align="center">ArticulateAI</h1>
<p align="center">Listen, transcribe, reply - ArticulateAI masters the art of conversation.</p>

<p align="center">
    <a href="https://github.com/Slaymish/ArticulateAI"><img src="http://randojs.com/images/2.3kb-shield.png" height="20"/></a>
    <a href="https://twitter.com/intent/tweet?text=Check%20out%20ArticulateAI,%20an%20exciting%20project%20on%20GitHub.&url=https://github.com/Slaymish/ArticulateAI&hashtags=AI,ArticulateAI,opensource,github,developers"><img src="http://randojs.com/images/tweetShield.svg" alt="Tweet" height="20"/></a>
</p><br/><br/>


ArticulateAI is a powerful tool that utilizes the Whisper API for speech transcription. It leverages the advanced capabilities of OpenAI's GPT-3 or GPT-4 (depending on the size of the transcription) to provide intelligent responses. Additionally, Elevenlabs' text-to-speech technology is employed for high-quality audio output.




## Installation Instructions
To set up the Speech Assistant, follow these steps:

```
git clone https://github.com/Slaymish/ArticulateAI
cd ArticulateAI
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

## 👏 Supporters

[![Stargazers repo roster for @Slaymish/ArticulateAI](https://reporoster.com/stars/dark/Slaymish/ArticulateAI)](https://github.com/Slaymish/ArticulateAI/stargazers)


***
#### 📝 License

Copyright © 2023 [Hamish Burke](https://github.com/Slaymish). <br />
This project is [MIT](https://github.com/Slaymish/SpeechToSpeechAssistant/blob/main/LICENSE) licensed. 
