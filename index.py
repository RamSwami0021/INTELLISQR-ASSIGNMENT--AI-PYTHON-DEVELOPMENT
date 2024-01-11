import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()

def record_text():
    while True:
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                audio2 = r.listen(source2)
                my_text = r.recognize_google(audio2)
                return my_text
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        except sr.UnknownValueError:
            print("Unknown error occurred")

def output_text(text):
    with open("output.txt", "a") as f:
        f.write(text + "\n")

while True:
    text = record_text()
    output_text(text)
    engine.say(text)
    engine.runAndWait()

    print("Text recorded and written to file")
