import util

# List of prompt options to begin the process
starting_prompts = [
    "The transcript below is of someone discussing how to make a type of food. Format the information as a recipe.",
    "The transcript below is of someone talking about a random subject. Summarize what they were talking about.",
    "The transcript below is of someone trying to get help with a math problem. Concisely explain how to solve the problem. Go step by step.",
    "The transcript below is of a debate on a particular subject. Identify the main points of each side.",
    "The transcript below is of a lecture on a scientific topic. Provide a clear and simplified explanation of the topic.",
    "The transcript below is of a person describing a series of events. Create a timeline based on the information provided.",
    "The transcript below is of someone describing a complex process. Break down the steps of the process in an easy-to-understand way.",
    "The transcript below is a story. Summarize the story and identify its main themes.",
    "The transcript below is a description of a problem someone is facing. Propose a solution to the problem.",
    "The transcript below is a review of a book or movie. Provide a brief overview based on the reviewer's opinion.",
    "The transcript below is a conversation in a foreign language. Translate the conversation to English.",
    "Answer the following question."
]


# Main loop continues until user decides to stop
while True:
    # Display the prompt options
    print("----------------------------------------------------------------")
    print("Starting prompts:")
    for i, prompt in enumerate(starting_prompts):
        print(f"{i}. {prompt}")
    print("----------------------------------------------------------------")
    
    # Request user to select a prompt
    prompt_index = int(input("Which starting prompt would you like to use? "))
    selected_prompt = starting_prompts[prompt_index]
    print("----------------------------------------------------------------")
    
    # Prepend context to the selected prompt
    starting_prompt = f"You are a helpful bot. {selected_prompt}\n\n"

    # Request user to specify the audio length for recording
    RECORD_SECONDS = int(input("How many seconds of audio would you like to record? "))

    # Record audio using the specified duration
    util.record_audio(RECORD_SECONDS=RECORD_SECONDS)

    # Transcribe the recorded audio
    transcript = util.transribe_audio().text

    # Save the transcript to a text file, using a custom timestamp for the filename
    timestamp = util.get_custom_timestamp()
    with open(f"Transcripts/{timestamp}.txt", "w") as file:
        file.write(transcript)
    
    # Generate the chat completion
    chat_completion = util.chat_complete(starting_prompt=starting_prompt, transcript=transcript)

    # Print the chat completion
    print("----------------------------------------------------------------")
    print(".")
    print(".")
    print(".")
    print(chat_completion)
    print(".")
    print(".")
    print(".")
    print("----------------------------------------------------------------")

    # Check the length of the chat completion. If it's short enough, use text-to-speech to vocalize it.
    if len(chat_completion) < 100:
        print("Starting TTS")
        util.text_to_speak(chat_completion)
    else:
        print("Response too long for tts")
