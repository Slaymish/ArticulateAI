import util

# Starting prompts optins
starting_prompts = [
        "The transcript below is of someone discussing how to make a type of food. Format the information as a recipe.",
        "The transcript below is of someone talking about a random subject. Summarize what they were talking about.",
        "The transcript below is of someone trying to get help with a math problem. Concisely explain how to solve the problem. Go step by step.",
        "Answer the following question.",
    ]


while(1):
    # Get the starting prompt
    print("----------------------------------------------------------------")
    print("Starting prompts:")
    for i in range(len(starting_prompts)):
        print(str(i) + ". " + starting_prompts[i])
    print("----------------------------------------------------------------")
    starting_prompt = starting_prompts[int(input("Which starting prompt would you like to use? "))]
    print("----------------------------------------------------------------")
    starting_prompt = "You are a helpful bot. " + starting_prompt + "\n\n"

    # Get the audio length    
    RECORD_SECONDS = int(input("How many seconds of audio would you like to record? "))

    # Record audio
    util.record_audio(RECORD_SECONDS=RECORD_SECONDS)

    transcript = util.transribe_audio().text

    # save transcript to file
    with open("Transcripts/" + util.get_custom_timestamp() + ".txt", "w") as file:
        file.write(transcript)
            

    starting_prompt = "You are a helpful bot. You read the transcript below and reply with what would fit best from the context in the transcript. For example, if the subject is how to make food, you could format the information as a rescipe. If it was jsut two friends talking, just summarize what they were talking and if you had any additional points add them. If no request is said, just summarize what is happening in the transcription.\n\n"

    chat_completion = util.chat_complete(starting_prompt=starting_prompt, transcript=transcript)

    # print the chat completion
    print("----------------------------------------------------------------")
    print(".")
    print(".")
    print(".")
    print(chat_completion)
    print(".")
    print(".")
    print(".")
    print("----------------------------------------------------------------")

    if len(chat_completion) < 100:
        print("Starting TTS")
        # evelenlabs tts
        util.text_to_speak(chat_completion)

    else:
        print("Response too long for tts")

