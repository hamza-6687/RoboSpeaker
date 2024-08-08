import pyttsx3
if __name__ == '__main__':
    print("Welcome to Robo Speaker 1.1 created by Hamza")
    while True:
        x = input("What you want to hear, write please...")
        if x == "Hello":
            text_to_speech.say("Bye Bye")
            text_to_speech.runAndWait()
            break
        text_to_speech = pyttsx3.init()
        text_to_speech.say(x)
        text_to_speech.runAndWait()
