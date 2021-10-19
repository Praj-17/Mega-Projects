import pyttsx3
import PyPDF2
import speech_recognition as sr



# 0:alex , 17:stacey , other
vno=0

book = open("oops_final.pdf","rb")
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
voices=speaker.getProperty('voices')
speaker.setProperty('voice',voices[vno].id)
print("ACTIVATED",voices[vno].id)
rate=speaker.getProperty('rate')
speaker.setProperty('rate',250)

def speak(talk):
    speaker.say(talk)
    speaker.runAndWait()


def takeCommand():
    '''
    Recognize speech input from the microphone and returns it in form of string in console
    '''

    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.energy_threshold = 300
        r.adjust_for_ambient_noise(source)
        print("Listening,Speak Now......")
        talk = r.listen(source) #use speech recognizer(sr.Recognizer()) to listen to the audio source
        # said = ""

        try:
            print("Recognizing....")
            said = r.recognize_google(talk) # Performs speech recognition on audio_data,using the Google Speech Recognition API
            print("You said : ", said.lower())
        except Exception as e:
            print("Exception: " + str(e))
            print("Say that again Please...")
            speak("Say that again Please")
            said=takeCommand()

    return said

# print("From which page do you want me to start reading from ?")
# speak("From which page do you want me to start reading from ?")
page_number = 7
page = pdfReader.getPage(page_number)

# page = pdfReader.getPage(1)
text = page.extractText()
speaker.say(text)
speaker.runAndWait()
# book = open("oops_final.pdf","rb")
            # pdfReader = PyPDF2.PdfFileReader(book)
            # pages = pdfReader.numPages
            # print(pages)
            #
            # print("From which page do you want me to start reading from ?")
            # speak("From which page do you want me to start reading from ?")
            # page_number = takeCommand()
            # page = pdfReader.getPage(page_number)
            # texts = page.extractText()
            # speak(texts)