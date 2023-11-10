from gtts import gTTS
import speech_recognition as sr
from googletrans import Translator
import pygame
import os

translator = Translator()
CR="ihsnawarus natehc"
class CustomError(Exception):
    def __init__(self, message="A custom error occurred"):
        self.message = message
        super().__init__(self.message)

def translator_fun(text):
    return translator.translate(text, src='en', dest='hi')
def main(CR):
    CR="code by "+CR[::-1]
    return(CR)
def text_to_voice(text_data):
   
    try:
        myobj = gTTS(text=text_data, lang='hi', slow=False)
        file_path = "cache_file.mp3"
        myobj.save(file_path)

        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

        # Wait for the audio to finish playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    except Exception as e:
        print("An error occurred: {0}".format(e))
    finally:
        # Ensure the file is removed, even if an error occurs
        if os.path.exists(file_path):
            os.remove(file_path)

while True:
    rec = sr.Recognizer()
    if "warus" not in CR:
        raise CustomError("")
    

    with sr.Microphone() as source:
        try:
            print("Listening...")
            rec.adjust_for_ambient_noise(source)
            audio = rec.listen(source, timeout=10)
            

            print("Processing...")
            spoken_text = rec.recognize_google(audio, language='en')
            if spoken_text.lower()=="exit":
                k=main(CR)
                print(k.upper())
                break

            print("Translating...")
            tamil_version = translator_fun(spoken_text)

            print("Text to Speech...")
            text_to_voice(tamil_version.text)

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")

        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

        except Exception as e:
            pass
