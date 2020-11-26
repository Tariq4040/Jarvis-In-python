import pyttsx3
import datetime
import wikipedia
import speech_recognition as sr
import pyaudio
import webbrowser
import os
import random
import smtplib



engine = pyttsx3.init('sapi5') #learn more about sapi5,use google and read more about it.....
voices = engine.getProperty('voices')     #yahan pe voices get ki h or neche set kre ge.
# print(voices)
# hmare system k andr 2 voices hoti,male and female ki,voices[0].id=male voice
#  and voices[1].id=female voice....... 
print(voices[0].id)
voices = engine.setProperty('voice' , voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour > 0 and hour < 12:
        speak("Good Morning Tariq Ahmad")
    elif hour >= 12 and hour < 18:
        speak("Good After Noon Tariq Ahmad")
    else:
        speak("Good Night Tariq Ahmad")

    speak("Hi I'm Your Assistant! how May i Help You Sir.....Tell Me")

def takeCommand():
    #it take command from user by Microphone,and return output as string 
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold  = 1
        r.energy_threshold = 700
        # r.dynamic_energy_threshold = True
        # r.operation_timeout = 5000
        audio = r.listen(source)
    try:
        print("Recognizing......")
        query = r.recognize_google(audio , language='en')
        print(f"User Speak: {query} ")
    except Exception as e:
        print(e)
        print("i Can't Understand Your words So,Please Repeat!!!!")
        speak("i Can't Understand Your words So,Please Repeat!!!!")
        

        return "None"
    return query

def sendEmail(to , content):
#email send krne k lea  hme email ki security me ja kr wahn se Less secure app access ka check off
#  se on krna h.mtlb jis account se send krna h os ka on krna h.testing krne k bad che again
# off kr de....  
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('scholors14409@gmail.com', 'scholors508587')
    server.sendmail('scholors14409@gmail.com', to , content)
    server.close()
    #here is our main Function,in which we are calling all the User Define Functions 
if __name__ == "__main__":
    # speak('Welcome Mr Tariq')
    wishMe()
    # takeCommand()

    #Logics for executing Task based on Query........
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia......')
            query = query .replace('wikipedia' ,'')
            result= wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(result)
            speak(result)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open visual Studio code' in query:
            webbrowser.open("visual Studio code")
        
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")


        elif 'play music' in query:
            music_dir= "D:\\EnterTainment\\SONG+Videos\\Gurman Bhular"
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        

        elif 'the time' in query:
            store_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the Current time is {store_time}")

        #yahan pe hm vs code the path de rhe g esii trha hm or b agr kesi program 
        # ko open krwana chahte h to os ya on ka path de skte h......yahan pe srf ak ka path de
        # rha hn   

        elif 'open visual studio code' in query:
            path = "C:\\Users\\M.Tariq Ahmad\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)

        elif 'send email' in query:
            try:
                speak('what should you Say to Email Receiver??')
                content = takeCommand()
                to = 'developer14409@gmail.com' #ye email os bnde ka h jse hm ne email send krna h
                sendEmail(to , content)     #ye method define kea h,check top
                speak('Your Email has Beeen Sent Successfully')
            except Exception as e:
                print(e)
                speak("Your Email has Not been Sent")

        elif 'exit' in query:
            speak("Thank You for give Me time")
            exit()
            
