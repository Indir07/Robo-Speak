#   pip install pyttsx3

import pyttsx3

if __name__ == '__main__':
    print("Welcome to RoboSpeaker Created by Indir Solanki")

    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    while True:
        x = input("What do you want me to speak: ")

        # Speak the input text
        engine.say(x)
        engine.runAndWait()

        y = input("Do you want to continue (y/n): ")

        if y == "n":
            # Speak a farewell message and exit the loop
            farewell_message = "Thank you for using RoboSpeaker. Goodbye!"
            engine.say(farewell_message)
            engine.runAndWait()
            break
