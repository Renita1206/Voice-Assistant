import speech_recognition as sr
import pyttsx3
import os
from datetime import datetime
import pyjokes


ginny=pyttsx3.init()
r=sr.Recognizer()

terminateCommands=["bye","exit","stop","goodbye"]
check=True

voices = ginny.getProperty("voices")
ginny.setProperty('voice', voices[1].id)

def executeCommand(command):
    print("Command is being processed")
    global check
    if "joke" in command:
        a=pyjokes.get_joke()
        print(a)
        ginny.say(a)
        ginny.runAndWait()
    elif "search" in command:
        search=command.replace("search"," ").strip().replace(" ","+")
        url="start https://www.google.com/search?q="+search
        os.system(url)
    elif "email" in command:
        url="start https://mail.google.com/mail/u/0/#inbox"
        os.system(url)
    elif "time" in command:
        now = datetime.now()
        h=now.hour
        m=now.minute
        time= str(h)+" "+str(m)
        ginny.say("The time is "+time)
        ginny.runAndWait()
    elif "music" in command:
        os.system("spotify")            #can use spotify api later
        check=False
    elif "help" in command:
        helpStatements = ["You can ask me to tell the time, search something in the internet, open your email, tell a joke or play music",
                            "For each of the above use the keywords time, search, email, joke and music respectively"]
        ginny.say(helpStatements[0])
        ginny.say(helpStatements[1])
        ginny.runAndWait()

    else:
        ginny.say("Sorry I'm unable to do that at present moment")
        ginny.runAndWait()



ginny.say("Hello, I'm Ginny")
ginny.runAndWait()

while(check):
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.5)
            print("Listening")
            audio = r.listen(source)
            print("Recognizing")
            command = r.recognize_google(audio)
            command = command.lower()
            print("Recognized text: ",command)
            if command in terminateCommands:
                ginny.say("Okay, goodbye")
                ginny.runAndWait()
                break
            executeCommand(command)
              
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        ginny.say("Sorry, something went wrong")
        ginny.runAndWait()
          
    except sr.UnknownValueError:
        print("unknown error occured")

    except Exception as e:
        print("Error \n", e)

