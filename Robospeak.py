import pyttsx3

print("Welcome to RoboSpeaker")

while True:
    speaker = pyttsx3.init()
    text = input("Enter what you want me to speak: ")
    if text.lower() == "exit":
        speaker.say("Goodbye my friend")
        speaker.runAndWait()
        break
    speaker.say(text)
    speaker.runAndWait()