from math import trunc
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

from wikipedia import exceptions
engine = pyttsx3.init('sapi5') # Speech API
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) # setting David's voice onto the engine
for i in range (len(voices)):   
    print(voices[i].id)
# print(voices[1].id)
# print(voices[2].id)
# print(voices[3].id)
# engine.say("My Name is JARVIS")
# engine.runAndWait()


def speak(audio): 
    """
    Makes the AI speak
    """
    print(audio)
    engine.say(audio)
    engine.runAndWait()
    
def takeCommand():
    """
    It takes microphone input from the user and returns string output
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold =1  # seconds of non-speaking audio before a phrase is considered complete
        r.energy_threshold =450 # minimum audio energy to be considered a command
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source,timeout=4, phrase_time_limit=7) #Records a phrase from user
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language= 'en-in') #Using google for voice; en-in mens 
        print(f"User said: {query}\n")
    except Exception as e:
        print("Exception: " + str(e))
        speak("Couldn't Listen! Please, say that again")
        return "None"
    return query
    
def wishme(): 
    """
    A function that wishes u w.r.t time
    """
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12:
        speak("Good Morning")
    elif hour >= 12 and hour <=6:
        speak("Good After")
    elif hour >= 6 and hour <=9:
        speak("Good Evening")
    elif hour >= 9 and hour <=0:
        speak("Good Night")
    speak("Hello, My name is Jarvis. What can I do for you?")
    
def sendemail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
     #This is the default mail submission port(of starttls). When an email client or outgoing server is submitting an email to be routed by a proper mail server, it should always use SMTP port 587 as
    server.echlo()
    #Extended Simple Mail Transfer Protocol (ESMTP) command sent by an email server(client) to identify itself when connecting to another email server to start the process of sending an email
    server.starttls()
    #Puts the connection to the SMTP server into TLS mode.  # If there has been no previous EHLO or HELO command this session, this method tries ESMTP EHLO first.
    server.login('pwaykos1@gmail.com', "Password")
    #Log in on an SMTP server that requires authentication.
    server.sendmail('pwaykos1@gmail.com', to, content)
    server.close()
    
    
    
if __name__ == "__main__":
    wishme()
    f =1
    while f == 1:
        query = takeCommand().lower()
        #Logic for executing tasks based on Query
        if 'wikipedia' in query :
            # print("Searching Wikipedia....")
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "") #Replacing Wikipedia with blank to replace it
            results = wikipedia.summary(query, sentences=2,auto_suggest=True, redirect=True)
            speak("The Wikipedia says....")
            # print(results)
            speak(results)
            break;
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            
        elif 'quit' in query:
            speak("Thank you, Have a good day")
            exit()
            # f = 0   
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'play music' in query:
            music_dir = 'D:\\audio'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0])) #This will join the path with the first song in the directory
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'open code' in query:
            codePath = "C:\\Users\\pwayk\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'email to prajwal ' in query:
            try:
                speak("What should I say")
                content = takeCommand()
                to = "pwaykos1@gmail.com"
                sendemail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                speak("Sorry sir!, The email couldn't be sent")
        elif 'open gmail' in query:
            webbrowser.open("mail.google.com")
        
                
                
            
            
            
          
            
        
            