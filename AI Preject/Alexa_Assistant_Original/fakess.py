import pyjokes
import speech_recognition as sr
import datetime
import datefinder
import pyttsx3
import wikipedia
import pywhatkit
import webbrowser
import os
import subprocess
from subprocess import call
import sys
import smtplib
import time
import random
from selenium import webdriver
import wolframalpha
import urllib.request     #urllib. request for opening and reading URLs
import ssl
import PyPDF2
try:
    app=wolframalpha.Client("WJEH8E-A35T37Y6X8")
except Exception as p:
    print("Exception: " + str(p))


# 0:alex , 17:stacey , other
# 0:David, 1,2: Hazel, Zira
vno=1
var_pass = "iit1istheaim"
engine=pyttsx3.init() #sapi5 can be used
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[vno].id)
print("ACTIVATED",voices[vno].id)
rate=engine.getProperty('rate')
engine.setProperty('rate',250)


def speak(talk):
    """
    Makes the AI speak
    """
    engine.say(talk)
    engine.runAndWait()

def  wishMe():
    subprocess.call(["afplay", "sound.mp3"])
    hour=int(datetime.datetime.now().hour)   #will get hour in int(0-24)
    if hour>=0 and hour<=12:
        print("Good Morning,sir...")
        speak("Good Morning,SIR")
    elif hour>=12 and hour<=18:
        print("Good Afternooon,sir...")
        speak("Good Afternooon SIR")
    else:
        print("Good Evening,sir...")
        speak("Good Evening SIR")

def voicename():
    if vno==0:
        print("I am Alex, your personal assistant, how may i help you today?")
        speak("I am Alex, your personal assistant, how may i help you today?")

    elif vno==17:
        print("I am Stacey, your personal assistant, how may i help you today?")
        speak("I am Stacey, your personal assistant, how may i help you today?")

    else:
        print("I am MR.X,your personal assistant, how may i help you today?")
        speak("I am MR.X,your personal assistant, how may i help you today?")





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
        talk = r.listen(source, timeout=4, phrase_time_limit=7) #use speech recognizer(sr.Recognizer()) to listen to the audio source
        # said = ""

        try:
            print("Recognizing....")
            said = r.recognize_google(talk, language="en-in") # Performs speech recognition on audio_data,using the Google Speech Recognition API
            print("You said : ", said.lower())
        except Exception as e:
            print("Exception: " + str(e))
            print("Say that again Please...")
            speak("Say that again Please")
            said=takeCommand()

    return said



def sendEmail(to,content):

    # A port number is a way to identify a specific process to which  an Internet or other network  message is to be forwarded when it arrives  at  a  server
    #Modern email servers use port 587 for the secure submission of email for delivery.

     server=smtplib.SMTP('smtp.gmail.com',587)  #This is the default mail submission port(of starttls). When an email client or outgoing server is submitting an email to be routed by a proper mail server, it should always use SMTP port 587 as the default port.
     server.ehlo()  #Extended Simple Mail Transfer Protocol (ESMTP) command sent by an email server(client) to identify itself when connecting to another email server to start the process of sending an email
     server.starttls() #Puts the connection to the SMTP server into TLS mode.  # If there has been no previous EHLO or HELO command this session, this method tries ESMTP EHLO first.

     server.login("sharaanofficial2001@gmail.com",var_pass) #Log in on an SMTP server that requires authentication.
     server.sendmail("sharaanofficial2001@gmail.com",to,content) #from,to,msg
     server.close()

def wolfram_ssl():
    ssl._create_default_https_context = ssl._create_unverified_context
    response = urllib.request.urlopen('https://www.wolframalpha.com/')
    # print(response.read().decode('utf-8'))


class CallPy(object):
    def __init__(self, path='/Users/sharaan/PycharmProjects/pythonProject4/Alexa_Assistant_Original/sound.py'):
        self.path = path

    def call_python_file(self):
        call(["Python3", "{}".format(self.path)])



def TaskExecution():
    wishMe()
    voicename()
    while True:
        said = takeCommand()
        # Logics for executing tasks based on user speech
        if "hello" in said:
            speak("Please Wake Up sir !!!")
            speak("hello sir, how are you?")
            speak("Hello sir, How are you...?")

        elif "alarm" in said:

            print("what hour you want to set the Alarm..?")
            speak("ok,what hour you want to set the alarm..?")
            alarmH=int(takeCommand())
            print("what minute you want to set the Alarm")
            speak("ok,what minute you want to set the alarm..?")
            alarmM = int(takeCommand())

            print("Should I set it for Am or Pm...?")
            speak("Should I set it for eh em or Pm ?")
            ampm = str(takeCommand())
            print("Setting your alarm for",alarmH,":",alarmM,ampm.upper())
            speak(f"Ok sir,Setting your alarm for,{alarmH},{alarmM},{ampm}")
            # speak("ok ,setting alarm")
            print("Alarm set...")
            speak("Alarm set...")

            if(ampm=='pm'):
                alarmH=alarmH+12
                while 1==1:
                    if (alarmH== datetime.datetime.now().hour and alarmM==datetime.datetime.now().minute):
                        speak("Please Wake up sir")
                        speak("Please Wake up sir")
                        print("Time to wake up sir...")
                        subprocess.call(["afplay", "beep_sound.mp3"])


        elif "what is your name" in said:
            if vno == 0:
                speak("I am Alex,your personal assistant")
            elif vno == 17:
                speak("I am Stacy,your personal assistant")
            else:
                speak("I am MR.X,your personal assistant")
            said = takeCommand()

        elif "are you doing well" in said or "how are you" in said:
            stMsgs = ['Just doing my thing!', 'Nice!', 'I am doing great','yah!,going on pretty decent']
            speak(random.choice(stMsgs))
            print(random.choice(stMsgs))

        elif 'search' in said or "wikipedia" in said:
            person = said.replace('search', "")
            speak("ok,Searching Wikipedia for "+person)
            print("How many sentences do you want me to extract")
            speak("How many sentences do you want me to extract")
            no_sent = takeCommand()
            info = wikipedia.summary(person, sentences=no_sent)
            print(info)
            speak("According to Wikipedia...")
            speak(info)

        elif 'play' in said:
            song = said.replace('play', '')
            speak("ok,playing" + song)
            pywhatkit.playonyt(song) #plays the particular song on yt

        elif 'programming joke' in said:
            print(pyjokes.get_joke())
            speak(pyjokes.get_joke())
            said = takeCommand() #takes the answer of a joke question

        elif 'read' in said:
            speak('ok, reading the pdf you have attached')
            c=CallPy()
            c.call_python_file()


        elif 'current time' in said or "time now" in said:
            time = datetime.datetime.now().strftime('%H:%M %p')
            print(time)
            speak('The time is' + time)
            said = takeCommand()


        elif 'competitors' in said:
            speak('I dont know anyone named SIRI,BIKSY AND GOOGLE ASSISTANT,Thats it!!, Got your answer!!,Now dont talk to me henceforth')

        elif 'youtube.com' in said:
            speak("ok,opening Youtube")
            print("Opening Youtube...")
            webbrowser.open('https://www.youtube.com/')

        elif 'google' in said or "google.com" in said:
            speak("ok,opening Google")
            print("Opening Google...")
            webbrowser.open('https://www.google.co.in/')

        elif 'amazon.com' in said:
            speak("ok,opening Amazon Website")
            print("Opening Amazon...")
            webbrowser.open('https://www.amazon.in/')

        elif 'flipkart.com' in said:
            speak("ok,opening flipkart Website")
            print("Opening Flipkart...")
            webbrowser.open('https://www.flipkart.com/?gclid=CjwKCAiAirb_BRBNEiwALHlnDwKe4d566q0IvvOYlBpTISQWNC257Mjc1cCY0rKSVmg8ilSjWdBRTRoC1WAQAvD_BwE&ef_id=CjwKCAiAirb_BRBNEiwALHlnDwKe4d566q0IvvOYlBpTISQWNC257Mjc1cCY0rKSVmg8ilSjWdBRTRoC1WAQAvD_BwE:G:s&s_kwcid=AL!739!3!461496258709!e!!g!!flipkart&gclsrc=aw.ds&&semcmpid=sem_8024046704_brand_city_nc_goog')

        elif 'gmail' in said or "gmail.com" in said:
            speak("ok,opening your Gmail")
            print("Opening Gmail...")
            webbrowser.open('https://mail.google.com/mail/u/0/#inbox')

        elif 'excel' in said or 'ms excel' in said:
            speak("ok,opening MS EXCel on your system")
            print("Opening MS Excel")
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, '/Applications/Microsoft Office 2011/Microsoft Excel.app'])

        elif 'screen recorder' in said or 'quicktime player' in said:
            speak("ok,opening the Screen Recorder application,that is Qicktime player,on your system")
            print("Opening QuickTime player")
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, '/Applications/QuickTime Player.app'])

        elif 'vs code' in said:
            speak("ok,opening VEE ESS CODE EDITOR on your system")
            print("Opening VS Code...")
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, '/Users/sharaan/Downloads/Visual Studio Code 3.app'])

        elif 'zoom' in said:
            speak("ok,opening Zoom application on your system")
            print("Opening Zoom...")
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, '/Applications/zoom.us.app'])

        elif 'data set' in said:
            speak("ok,opening dataset folder from the system memory")
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, '/Users/sharaan/Desktop/sound'])

        elif 'sound' in said:
            speak("ok,opening your sound folder from the system memory")
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, '/Users/sharaan/Desktop/sound'])


        elif 'email' in said or 'mail' in said:
            try:
                speak("ok,What should i write")
                print("What should i write ?")
                content=takeCommand()
                to="sharaanofficial2001@gmail.com"
                print("Sending...")
                speak("Sending...")
                sendEmail(to,content)
                speak("Email sent successfully")
                print("Your Email sent successfully....!!")
                speak("Please check your  Mailbox")

            except Exception as e:
                print("Exception: " + str(e))
                speak("Sorry,not able to send Email")

        elif "location of" in said:
            said = said.split(" ")
            location = said[1] #obtain place name
            speak("Hold on, I will show you where" + location +  "is")
            os.system("google-chrome https://www.google.nl/maps/place/" + location)

        if "weather" in said:
            #We have downloaded the chrome driver for Google Chrome version 87 for MAC
            #The main purpose of the ChromeDriver is to launch Google Chrome & run test cases on Google Chrome browser.
            # Without that, it is not possible to execute Selenium test scripts in Google Chrome as well as automate any web application.

            said = said.split(" ")
            city_name = said[len(said) - 1]
            speak("ok,i am showing you weather forecast of " + city_name + "from weather forecast.com")
            driverLocation = "/Users/sharaan/Downloads/chromedriver 3"
            driver = webdriver.Chrome(driverLocation)  # Creates a new instance of the chrome driver.

            driver.get("https://www.weather-forecast.com/locations/" + city_name + "/forecasts/latest")
            print(driver.find_element_by_class_name("b-forecast__table-description-content")[0].text)

            speak(driver.find_element_by_class_name("b-forecast__table-description-content")[0].text)


        elif "nothing" in said or "stop" in said or "bye" in said or "quit" in said or "close" in said or "exit" in said or "done" in said or "leave" in said or "goodbye" in said:

            speak("okay,Quitting")
            print("Bye Sir, I am going to sleep, you can call me anytime. Have a good day...!!")
            print("Bye Sir, I am going to sleep, you can call me anytime. Have a good day...!!")

            break


        elif "shutdown" in said or "shut down" in  said:
            speak("Shutting down your pc,sir")
            print("Shutting down your pc,sir....")
            speak("Thank You")
            os.system("shutdown /s /t 1")

        elif "temperature" in said:
            try:
                wolfram_ssl()
                response=app.query(said)
                print("The Tempetature is : ",next(response.results).text)
                song = said.replace('C', 'Celcius')
                speak("the Tempetature  is"+next(response.results).text)

            except Exception as z:
                print("Exception"+str(z))
                print("Sorry,no Internet Connection....")

        else:
            try:
                wolfram_ssl()
                response=app.query(said)    #Allows for arbitrary parameters to be passed in the query
                print(next(response.results).text)
                speak(next(response.results).text)
            except:
                print("Say that again,Please...")
                # speak("Say that again,Please...")

if __name__ == '__main__':
    while True:
        try:
            permission = takeCommand()
            if "wake up" in permission:
                TaskExecution()
            elif "sleep" in permission:
                speak("Bye Sir, I am going to sleep, you can call me anytime. Have a good day...!!")
                sys.exit()

        except Exception as e:
            print("Exception: " + str(e))
            print("Say that again Please...")
            speak("Say that again bai")
            said = takeCommand()



















