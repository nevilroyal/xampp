import pyttsx3
import speech_recognition as sr
from gtts import gTTS
import os
import platform

# Function for Text to Speech
def tts():
    text = input("Enter the text: ").strip()
    
    if not text:
        print("No text entered. Please enter some text.")
        return

    lang = "en"
    speech = gTTS(text=text, lang=lang, slow=False)
    speech.save("output.mp3")

    print("Playing the converted text...")

    # Detect OS and use appropriate command to play audio
    if platform.system() == "Windows":
        os.system("start output.mp3")
    elif platform.system() == "Darwin":  # macOS
        os.system("open output.mp3")
    else:  # Linux
        os.system("mpg321 output.mp3")

# Function for Speech to Text from a File (Audio File)
def att():
    file = "output.wav"  # Ensure this file exists in the working directory
    s = sr.Recognizer()

    if not os.path.exists(file):
        print(f"Error: The file '{file}' does not exist.")
        return

    try:
        with sr.AudioFile(file) as source:
            audio_data = s.record(source)
            text = s.recognize_google(audio_data)
            print("Text from audio file:", text)
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main Menu Loop
while True:
    print("\nMENU:")
    print("1 - Text to Speech")
    print("2 - Speech to Text from File")
    print("3 - Exit")

    choice = input("Enter your choice (1, 2, or 3): ").strip()

    if choice == '1':
        tts()
    elif choice == '2':
        att()
    elif choice == '3':
        print("\nExiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

    print("\n" + "_" * 30 + "\n")
