
#all modules
import speech_recognition as sr
from datetime import datetime
from datetime import date
import random
from os import *
import webbrowser
import wikipedia
import requests
from bs4 import BeautifulSoup
from wikipedia.wikipedia import search
from pywhatkit import playonyt


#greeting message
hour = int(datetime.now().hour)

if hour>=0 and hour<12:
    system('say good morning sir')
elif hour>=12 and hour<18:
      system('say good after noon sir')
else:
    system('say good evening sir')



#listening
r = sr.Recognizer()
mic = sr.Microphone()
with mic as source:
    print("Listening...")
    r.pause_threshold = 1
    audio = r.listen(source)

#recongnizing
try:
    print("Recognizing...")
    it = r.recognize_google(audio, language="en-in")
    print("user said: ", it)
    it = it.upper()

except Exception as e:
    it = ""
 


while "SLEEP" not in it:
 today = datetime.now()
 to = date.today()



 if ('HI' in it):
    system('say hello sam')
    print("Hello sam")
 elif ('HELLO' in it):
     system('say hi sam')
     print("hi sam")
 elif ('NAMASTE' in it):
     system('say namaste sam')
     print("namaste sam")
 elif ('WHAT IS YOUR NAME' in it or 'WHAT IS YOUR NAME?' == it):
     system('say my name is proton')
     print("my name is proton")
 elif ("WEATHER" in it):
     place = ("ujjian")
     search = f"wheather in {place}"

     url1 = f"https://www.google.com/search?q={search}"
     q2 = requests.get(url1)

     soup = BeautifulSoup(q2.text, "html.parser")
     update = soup.find("div", class_="BNeawe").text
     
     system(f"say {search} now is {update}")
     print(f"{search} now is {update}")

 elif ("ARE YOU HUMAN" in it):
     system('say i am not human i am robot')
     print("i am not human i am robot")
 elif("ARE YOU ROBOT" in it):
     system('say yes')
     print ("yes")
 elif("HOW OLD ARE YOU" in it or "WHATS YOUR AGE" == it):
     system("say what do you think how old am i")
     print("what do you think how old am i?")
 elif("WHAT DAY IS TODAY" == it or "DATE" in it):
     system ('say the date is %02d/%02d/%04d' % (today.day, today.month, today.year))
     print (today.day, today.month, today.year)
 elif("TIME" in it):    
     system ('say the time is %02d:%02d:%02d' % (today.hour, today.minute, today.second))
     print (today.hour, today.minute, today.second)
 elif("WHO ARE YOU" in it or "WHO ARE YOU?" == it):
     system('say i am proton ')
     print("i am proton")   
 elif("SONG" in it):

    song = ["safe and sound", "Cartoon-on and on", "Jim Yosef - Firefly ", "Virtual Riot - Purple Dragons", "Luis Fonsi - Despacito", "Downlink - Absolute Fire"]
    x = random.choice(song)
     
    play = it.replace("SONG", x)
    system('say Playing random song for you')
    print("Playing random song for you")
    playonyt(play)
 elif ("PLAY" in it):
     video = it.replace("PLAY", "")
     system('say playing on youtube' + video)
     print("playing on youtube" + video)
     playonyt(video) 
      
 elif("WHAT IS MY NAME" in it):
     system('say sam. ')
     print("sam")
 elif("WHO MADE YOU" in it):
     system('say python made me')
     print("python made me")
 elif("TELL ME SOMETHING" in it):
     system('say rose are reds... voilents are blue... Proton is here... tell what can i do')
     print("rose are reds voilents are blue Proton is here tell what can i do")
 elif("SAM" == it):
     system('say your name')
     print("your name")
 elif("PROTON" == it):
    system('say my name is proton')
    print("my name is proton")
 elif("TELL ME JOKE" in it):
     system('say my sence of humor in in alpha hopefully soon it will get beta')
     print("my sence of humor in in alpha \nhopefully soon it will get beta")         
 elif("RANDOM NUMBER" in it):
    a = input("enter first number: ")
    b = input("enter second number: ")
    a = int(a)
    b = int(b)
    ran = random.randint(a, b)
    system('say the random number is' + str(ran))
    print(ran)
 elif("I AM SAM HERE" == it):
     system('say hi sam')
     print("hi sam")
 elif("HOW ARE YOU" in it):
     system('say i am fine')
     print("i am fine")
 elif("STOCK" in it):
     stock = it.replace("STOCK", "")
     url = f"https://www.google.com/search?q={stock}"

     Html = requests.get(url)

     soup = BeautifulSoup(Html.text, "html.parser")

     price = soup.find("div", class_="BNeawe").text
   
     system('say ' + str(price))
     print(price)

 elif("YOUTUBE" in it):
         print("opening youtube...")
         webbrowser.open("http://www.youtube.com")
 elif("GOOGLE" in it):
         print("opening google...")
         webbrowser.open("http://www.goole.com")                    
 elif("STACK OVERFLOW" in it):
         print("opening stackoverflow...")
         webbrowser.open("http://www.stackoverflow.com")
 elif("WIKIPEDIA" in it or "WIKI" in it):
      print("searching wikipedia...")
      it = it.replace("WIKIPEDIA", "")
      results = wikipedia.summary(it, sentences=2)
      system("say according to wikipedia")
      system("say " + results)
      print(results)
 else:
     if(it != ""):
      system('say what')
      print("what...") 

 r = sr.Recognizer()
 mic = sr.Microphone()


 with mic as source:
    print("Listening...")
    r.pause_threshold = 1
    audio = r.listen(source)


 try:
    print("Recognizing...")
    it = r.recognize_google(audio, language="en-in")
    print(f"user said: ", it)
    it = it.upper()

 except Exception as e:
    #   print("listening...")
    #   system("say say that again please...")
      it = ""



 if ("SLEEP" in it):
     system('say ok, Going for sleep')
     print("ok, Going for sleep\n")
