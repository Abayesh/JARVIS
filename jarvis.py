from subprocess import STARTUPINFO
from typing_extensions import Self
import pyttsx3 #audio assistant voice
import speech_recognition as sr  #getting command from user
import maskpass #password hider
import datetime
import os #to have a control of OS
import cv2 #for camera
import random #for playing music randomly
from requests import get #to access HTTPS
import wikipedia #imports wikipedia page
import webbrowser
import pywhatkit as kit #automation for youtube and Whatsapp
import smtplib
import sys #system+
import wolframalpha #Wolframalpha API
import pyautogui #importing the UI
import time
import PyPDF2  #read and edit PdF
from PyPDF2 import PdfReader, PdfWriter
import img2pdf #to convert a image to pdf
import psutil #battery
import speedtest #netspeed
import math #to convert bytes to mb in netspeed
import pyjokes #python jokes
#PyQt5
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from JarvisGUI import Ui_JarvisUi
import urllib.request
import playsound #for alarm
import platform #sysinfo






engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[0].id)  #David Voice
engine.setProperty('voices',voices[0].id)
engine.setProperty('rate',150)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#additional intializing voice
def startup():
    speak("Initializing system and checking all drivers")
    speak("All drivers are up and running")
    hour=int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("Good Morning Boss")
    elif hour>12 and hour<16:
        speak("Good Afternoon Boss")
    else:
        speak("Good Evening Boss")
    speak("Its "+(datetime.datetime.now().strftime("%I:%M %p"))+" and i'm online")
    speak ("Do you want any favour boss?")

 


    #FUNCTION DEFINITIIONS
    
       #To send an email
def sendEmail(to,content):
    #sender_email="dummymailjarvis@gmail.com"
    #password="jarvis@123"
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("dummymailjarvis@gmail.com","auqpykjylbmncbus")
    server.sendmail("dummymailjarvis@gmail.com",to,content)
    server.close()


     #wolframalpha API
def computational_intelligence(question):
    try:
        client = wolframalpha.Client("JJVYV9-Q7R74WYYYK")
        answer = client.query(question)
        answer = next(answer.results).text
        return answer
    except:
        speak("Sorry boss I couldn't fetch your query's answer. Please try again ")
        return None
        


    #pyPDF2
def pdf_reader():
    book=open("jarvispdf.pdf",'rb')#reads in binary mode
    pdfreader=PyPDF2.PdfReader(book)
    pages=len(pdfreader.pages)
    speak(f"Total number of pages in the book {pages}")
    speak("please enter the page number i have to read")
    pg=int(input("Please Enter the page nuber: "))
    page=pdfreader.pages[pg-1]
    text=page.extract_text()
    speak(text)


   


class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        speak("please enter the password to start")
        passcode= maskpass.askpass(prompt="Password:", mask="*")
        pwd = "nethraa"
        if passcode==pwd:
            speak("Welcome Abayesh")
            self.TaskExecution()
        else:
            speak("wrong password")
            speak("please say the secret passcode")
            result=self.takecommand().lower()
            if result=="alpha one":
                speak("Welcome Abayesh")
                self.TaskExecution()
            else:
                speak("Unauthenticated person")
                sys.exit()

       #Take Command
    def takecommand(self):
        r= sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            r.pause_threshold=1
            audio=r.listen(source,timeout=10,phrase_time_limit=6) #this will listen the command in microphone as source

        try:
            print("Recognizing...")
            command=r.recognize_google(audio,language='en-in')
            print(f"You said: {command}") #recognize we said in command with help of google indian Eng

        except Exception as e:
            speak("Boss, Please say it again...")
            return "none"
        return command


     #taskexecution
    def TaskExecution(self):
        startup()
        while True:
            self.command=self.takecommand().lower()

                    #General conversation with Jarvis

            if "how are you" in self.command or "how're you" in self.command:
                speak("I'm Fantastic. How about you ?")
               
            elif "i am good" in self.command or "i am fine" in self.command:
                speak("Nice to hear that..")

            elif "what is your name" in self.command or "what's your name" in self.command or "who are you" in self.command:
                speak("I'm Jarvis, your virtual Assistant")

            elif "who created you" in self.command:
                speak("I'm created by a genius named Abayesh")

            elif "what is the time now" in self.command or "tell me the time" in self.command:
                current=datetime.datetime.now()
                speak("The time is")
                speak(current.strftime("%H:%M:%S"))

            elif "what is the date today" in self.command or "what's the date today " in self.command:
                speak("today is")
                speak(datetime.date.today())

            elif "do you have a nickname" in self.command or "do you have a name" in self.command:
                speak("My nickname is JARVIS, but you can call me anytime")

            elif "what can you do" in self.command or "what are your functions" in self.command:
                speak("i can open applications, search your query in web, Entertain you, send messages for you and a lot more.")

            elif "thank you" in self.command or "thankyou jarvis"  in self.command:
                speak("my pleasure boss, Always at your service")

            
            elif 'wait' in self.command or "sleep now" in self.command or "please wait" in self.command or "delay" in self.command:
                waittime=20
                speak("It's Nap time")
                time.sleep(waittime)


            elif 'repeat after me' in self.command or 'repeat' in self.command:
                speak("yes tell me")
                repeat=self.takecommand()
                speak(repeat)

            elif "nothing" in self.command:
                speak("ok boss. But you can call me anytime for assist")

            elif "exit" in self.command or "quit" in self.command:
                speak("Thank you for your time..")
                break

            elif "other voice assistant" in self.command:
                speak("Siri is great, Alexa is perfect, Google assistant is good But i'm the Best")

            elif  "siri" in self.command or "alexa" in self.command:
                speak("I think you misinterpreted me. I'm Jarvis")

            elif "hello" in self.command:
                speak("Hai. I'm Jarvis. Nice to Meet you")

            elif "where are you" in self.command:
                speak("Now i'm inside your PC but always inside your heart")
                
            elif "i love you" in self.command:
                speak("i love you too but i'm just a artificial program")



            



                        #Logic Building for jarvis tasks.....

                #open system applications
                #to open Notepad
            elif "open notepad" in self.command or "notepad" in self.command:
                notepath= "C:\\Windows\\System32\\notepad.exe"
                speak("Opening notepad...")
                os.startfile(notepath)
                
                #to open MS Word
            elif "open word" in self.command or "open MS word" in self.command:
                    wordpath= "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
                    speak("Opening MS Word...")
                    os.startfile(wordpath)

                #to Open MS Excel
            elif "open excel" in self.command or "open MS excel" in self.command:
                    excelpath="C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
                    speak("Opening MS Excel...")
                    os.startfile(excelpath)

                #to open powerpoint
            elif "open powerpoint" in self.command or "open MS powerpoint" in self.command:
                powerpath="C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
                speak("Opening MS Powerpoint... ")
                os.startfile(powerpath)

                #to open file explorer
            elif "open files" in self.command or "open file" in self.command or "open file explorer" in self.command:
                filespath="C:\\"
                speak("Opening file explorer... ")
                os.startfile(filespath)

                #to open CMD
            elif "open command prompt" in self.command or "open CMD" in self.command:
                speak("Opening Command prompt...")
                os.system("start cmd")

                #to open camera
            elif "open camera" in self.command or "camera" in self.command:
                cap= cv2.VideoCapture(0)
                speak("opening camera")
                while True:
                    ret, img=cap.read()
                    cv2.imshow('webcam',img)
                    if cv2.waitKey(10) & 0xFF==ord('c'):
                        break;
                cap.release()
                cv2.destroyAllWindows()

                #to play music
            elif "play music" in self.command or "play some music" in self.command or "music" in self.command:
                    speak("Enjoy your music..")
                    musicpath="C:\music"
                    songs=os.listdir(musicpath) #convert everything in file to a list
                    rd=random.choice(songs)
                    os.startfile(os.path.join(musicpath,rd))

            
                #volume controls
            elif "volume up" in self.command or "increase the volume" in self.command:
                pyautogui.press("volumeup")
            elif "volume down" in self.command or "decrease the system volume" in self.command:
                pyautogui.press("volumedown")
            elif "volume mute" in self.command or "mute" in self.command:
                pyautogui.press("volumemute")

                
                #capture screenshot
            elif "take screenshot" in self.command or "take a screenshot" in self.command or "capture the screen" in self.command:
                    speak("By what name do you want to save the screenshot?")
                    name = self.takecommand()
                    speak("Alright sir, taking the screenshot")
                    time.sleep(4)
                    img = pyautogui.screenshot()
                    name = f"{name}.png"
                    img.save(name)
                    speak("The screenshot has been succesfully captured")

                    
                #to write a note
            elif "write a note" in self.command or "take a note" in self.command or "note it" in self.command:
                speak("What should i write, boss")
                note = self.takecommand()
                speak("at what name you want me to save this note")
                notesave=self.takecommand()
                file = open(f'{notesave}.txt','w')
                file.write(note)
                speak("your note has been saved")

                
            #PYPDF Functions with PDF
            elif "read pdf" in self.command:
                pdf_reader()

            elif "merge pdf" in self.command:
                pdfpath=["jarvispdf2.pdf","jarvispdf3.pdf"]
                pdfwriter=PdfWriter()
                speak('merging PDF files boss')
                for i in pdfpath:
                    pdf=PdfReader(i,'rb')
                    for page in range(len(pdf.pages)):
                        pdfwriter.add_page(pdf.pages[page])
                speak("at which name you want me to save the merged pdf ?")
                merged=self.takecommand()
                with open(f'{merged}.pdf','wb') as out:
                    pdfwriter.write(out)

                speak ("done boss. Merged the pdf files")

                
            #PYPDF Functions with PDF
            elif "read pdf" in self.command:
                pdf_reader()

            elif "merge pdf" in self.command:
                pdfpath=["jarvispdf2.pdf","jarvispdf3.pdf"]
                pdfwriter=PdfWriter()
                speak('merging PDF files boss')
                for i in pdfpath:
                    pdf=PdfReader(i,'rb')
                    for page in range(len(pdf.pages)):
                        pdfwriter.add_page(pdf.pages[page])
                speak("at which name you want me to save the merged pdf ?")
                merged=self.takecommand()
                with open(f'{merged}.pdf','wb') as out:
                    pdfwriter.write(out)

                speak ("done boss. Merged the pdf files")

                

            #battery percentage
            elif "how much power do we have" in self.command or "battery percentage" in self.command or "power" in self.command:
                battery=psutil.sensors_battery()
                percentage=battery.percent
                speak(f"our system have {percentage} percentage battery")
                if percentage>75:
                    speak("our system have enough power to continue our work")
                elif percentage<=75 and percentage>60:
                    speak("we have moderate amount of battery")
                elif percentage<=60 and percentage>30:
                    speak("battery is getting a little low consider plugging in")
                elif percentage<30:
                    speak("please plug in charger")


                #Image to PDF
            elif "convert image to pdf"in self.command or "image to pdf" in self.command:
                img="myimage.jpeg"
                f=open("myimage.pdf",'wb')
                f.write(img2pdf.convert(img))
                f.close()
                speak("done. converted image to pdf")


                 #alarm
            elif "set an alrm" in self.command or "keep an alarm" in self.command or "alarm" in self.command:
                def alarm():
                    alarmtime = input("Enter the time in format HH:MM \t")
                    speak("The Alarm has been set")
                    while True:
                        current_time = time.strftime("%H:%M")
                        if current_time == alarmtime:
                            print("Time's up!")
                            playsound.playsound('C:\\music\\ARIYASANAM.mp3')  # replace 'alarm_sound.mp3' with the path to your alarm sound file
                            break
                alarm()

                #Shutdown the PC
            elif  "shutdown" in self.command:
                speak ("Are you sure want to shutdown the PC?")
                confirm=self.takecommand().lower()
                if confirm=="yes":
                    os.system("shutdown /s /t 1")
                elif confirm=="no":
                    break
                            

             #to display system info
            elif "system information" in self.command or "system info" in self.command:
                system_info = platform.uname()
                speak("System Information:")
                speak(f"System: {system_info.system}")
                speak(f"Node Name: {system_info.node}")
                speak(f"Release: {system_info.release}")
                speak(f"Version: {system_info.version}")
                speak(f"Machine: {system_info.machine}")
                speak(f"Processor: {system_info.processor}")
             
             

              

                    #jarvis online functionalities
                #to find IP Address
            elif "find my ip" in self.command  or "what is my ip address" in self.command or "what's my ip address" in self.command:
                ip=get("https://api.ipify.org").text
                speak(f"your IP address is {ip}")


                #to use wikipedia
            elif "wikipedia" in self.command:
                speak ("searching wikipedia...")
                self.command=self.command.replace("wikipedia","")
                results=wikipedia.summary(self.command,sentences=2)
                speak ("According to Wikipedia..")
                speak(results)
                print(results)

            elif "tell me a joke" in self.command or "joke" in self.command or "jokes" in self.command:
                speak(pyjokes.get_joke())

                #to open youtube
            elif "open youtube" in self.command:
                speak("Opening Youtube...")
                webbrowser.open("https://www.youtube.com")

                #to open Gmail
            elif "open gmail" in self.command or "gmail" in self.command:
                speak("Opening Gmail...")
                webbrowser.open("https://mail.google.com/mail/u/1/")
                
                #to open whatsapp web
            elif "open whatsapp" in self.command or "whatsapp" in self.command:
                speak("opening whatsapp web....")
                webbrowser.open("https://web.whatsapp.com/")

                #to open Social Media Platforms (Facebook,Instagram,Twitter)
            elif "open facebook" in self.command or "facebook" in self.command:
                speak("Opening Facebook...")
                webbrowser.open("https://www.facebook.com/")

            elif "open instagram" in self.command or "instagram" in self.command:
                speak("Opening instagram...")
                webbrowser.open("https://www.instagram.com")

            elif "open twitter" in self.command or "twitter" in self.command:
                speak("Opening twitter...")
                webbrowser.open("https://twitter.com/")

                #to open OTT Platforms (Netflix,AmazonPrime,Hotstar)
            elif "open hotstar" in self.command or "hotstar" in self.command:
                speak("Opening Disney + Hotstar...")
                webbrowser.open("https://www.hotstar.com/in")

            elif "open netflix" in self.command or "netflix" in self.command:
                speak("Opening Netflix...")
                webbrowser.open("https://www.netflix.com/in/")

            elif "open prime" in self.command or "open amazon prime" in self.command or "amazon prime" in self.command:
                speak("Opening Amazon Prime...")
                webbrowser.open("https://www.primevideo.com/")

                #to search something on google
            elif "open google" in self.command:
                speak("What should I search on google")
                search=self.takecommand().lower()
                webbrowser.open(f"{search}")

            #whatsapp auto message
            elif "send message" in self.command:
                wcurrent=datetime.datetime.now()
                wtime=wcurrent.hour
                wmins=wcurrent.minute+2
                speak("Enter The phone number")
                phno=int(input("Enter The phone number:"))
                speak("what is the message you want me to send")
                msgwapp=self.takecommand()
                kit.sendwhatmsg("+91"+f"{phno}",msgwapp,wtime,wmins)#specify time and it only opens in WAweb

                #play song on youtube
            elif "play youtube song" in self.command or "play video on youtube" in self.command:
                speak("What song you want me to play")
                song=self.takecommand().lower()
                kit.playonyt(f"{song}")

                #to send an email automation
            elif "send an email" in self.command or "email" in self.command:
                try:
                    speak("please enter the email address")
                    to=input("Enter Address here:")
                    speak("what  should i say")
                    content =self.takecommand().lower()
                    sendEmail(to,content)
                    speak(f"Email has been successfully sent to {to}")

                except Exception as e:
                    print(e)
                    speak(f"Sorry Boss,I am not able to send this email to {to}")
                    

                #to find the location of a place in maps
            elif "where is" in self.command:
                self.command = self.command.replace("where is","")
                location = self.command
                speak("User asked to Locate")
                speak(location)
                webbrowser.open("https://www.google.co.in/maps/place/" + location + "")

       
            #wolframalpha Api
            elif "calculate" in self.command or "find" in self.command or "what" in self.command or "how" in self.command or "who" in self.command:
                    question = self.command
                    answer = computational_intelligence(question)
                    speak("it is "+answer)
            

        
                #internet speed
            elif "internet speed" in self.command or "net speed" in self.command: 
                def bytes_to_mb(size_bytes):
                    i=int(math.floor(math.log(size_bytes,1024)))
                    power=math.pow(1024,i)
                    size=round(size_bytes/power,2)
                    return f"{size} Mbps"
                speed=speedtest.Speedtest()
                down=speed.download()
                up=speed.upload()
                speak(f"we have "+bytes_to_mb(down)+" download speed")
                speak(f"and we have "+bytes_to_mb(up)+" upload speed")

                #spotify automation
            elif "play" in self.command:
                self.command=self.command.replace("play","")
                song=self.command
                os.system("spotify")
                time.sleep(10)
                pyautogui.hotkey('ctrl','l')
                pyautogui.write(song,interval=0.1)
                for key in ['enter','pagedown','tab','enter','enter']:
                    time.sleep(3)
                    pyautogui.press(key)

              





            
               
              
                  


 

startExecution=MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_JarvisUi()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)
    
    def startTask(self):
        self.ui.movie=QtGui.QMovie("D:/jarvis/jarvis/blackbackground.jpg")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie=QtGui.QMovie("D:/jarvis/jarvis/jarvisload.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie=QtGui.QMovie("D:/jarvis/jarvis/initalizing.gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie=QtGui.QMovie("D:/jarvis/jarvis/loading.gif")
        self.ui.label_4.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer=QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time=QTime.currentTime()
        current_date=QDate.currentDate()
        label_time=current_time.toString('hh:mm:ss')
        label_date=current_date.toString(Qt.ISODate)
        self.ui.textBrowser_2.setText(label_date)
        self.ui.textBrowser_3.setText(label_time)


app=QApplication(sys.argv)
jarvis=Main()
jarvis.show()
exit(app.exec_()) 





