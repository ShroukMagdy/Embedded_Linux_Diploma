from gtts import gTTS
from playsound import *
from speech_recognition import Recognizer, Microphone
import os 
import webbrowser
from time import *
from playsound import *

recognizer = Recognizer()

word_browser = {
    "google" : "https://www.google.com/",
    "جوجل" : "https://www.google.com/",
    "youtube" : "https://www.youtube.com/",
    "يوتيوب" : "https://www.youtube.com/"
}
word_time = ['time','ساعة','الوقت','الساعة']
word_date = ['يوم','النهارده','التاريخ','اليوم','date']
# Function to get speech
def listen():
    text_en = ""
    text_ar = ""
    with Microphone() as src:
        # recognizer.adjust_for_ambient_noise(src)
        print("Listening...")
        speech = recognizer.listen(src,timeout=5, phrase_time_limit=10)
    try:
        text_en = recognizer.recognize_google(speech, language='en-US')
        print("Recognized in English: " + text_en)
    except Exception as e:
        print(f"Error recognizing English: {e}")

    try:
        text_ar = recognizer.recognize_google(speech, language='ar-EG')
        print("Recognized in Arabic: " + text_ar)
    except Exception as e:
        print(f"Error recognizing Arabic: {e}")

    return text_en, text_ar

# Function to respond
def speak(text, lang):
    response_file = None
    try:
        response = gTTS(text=text, lang=lang, slow=False)
        response_file = os.path.join(os.getcwd(), "a.mp3")
        response.save(response_file)

        # Check if the file exists
        if os.path.exists(response_file):
            print(f"File created: {response_file}")

            # Create a VLC media player object
            player = playsound(response_file)

        else:
            print(f"File not found: {response_file}")
    except Exception as e:
        print(f"Error opening sound: {e}")
    finally:
        # Ensure the file is removed
        if response_file and os.path.exists(response_file):
            try:
                os.remove(response_file)
                print(f"File removed: {response_file}")
            except Exception as e:
                print(f"Error removing file: {e}")

# Function to do command
def search_execute(text):
    #browsers
    for key in word_browser.keys():
        if key in text:
            webbrowser.open(word_browser[key])
            return
    #time
    for word in word_time:
        if word in text:
            time=ctime().split(" ")[-2]
            speak(time,'en')
            return
    #date
    for word in word_date:
        if word in text:
            time=ctime().split(" ")
            speak(time,'en')
            return
    speak("Sorry, what you want is not available",'en')
    

def main():
    text_en = ""
    text_ar = ""
    speak("Hello , What do you want",'en')
    try:
        text_en, text_ar = listen()
    except Exception as e:
        print(f"Error opening sound: {e}")

    if not(text_ar == "") or not(text_en == ""):
        search_execute(text_ar+text_en.lower())

    sth_else =True
    while sth_else:
        speak("do you want something else",'en')
        try:
            text_en, text_ar = listen()
        except Exception as e:
            print(f"Error opening sound: {e}")

        if ("yes" in text_ar+text_en.lower()) or ("نعم" in text_ar+text_en.lower()):
            speak("What do you want",'en')
            try:
                text_en, text_ar = listen()
            except Exception as e:
                print(f"Error opening sound: {e}")
            if not(text_ar == "") or not(text_en == ""):
                search_execute(text_ar+text_en.lower())
        elif ("no" in text_ar+text_en.lower()) or ("لا" in text_ar+text_en.lower()):
            speak("Goodbye till next time",'en')
            sleep(3)
            sth_else = False
        else:
            speak("I do not get it please say yes or no",'en')  
            sleep(3)


if __name__ == "__main__":
    main()