# All Imports Required For Python:
import os
import pyttsx3
import speech_recognition as sr
import webbrowser
import pywhatkit
import pyautogui
import wikipedia
import time
import keyboard
import pyjokes
import PyPDF2
import datetime
from PyDictionary import PyDictionary as Dictionary
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import Tk
from tkinter import StringVar
from pytube import YouTube
from googletrans import Translator
from gtts import gTTS
from playsound import playsound




def Speak(Audio):

    Assistant = pyttsx3.init('sapi5')
    voices = Assistant.getProperty('voices')
    Assistant.setProperty('voice', voices[0].id)
    Assistant.setProperty('rate',200)
    print("   ")
    print(f"Jarvis: {Audio}")
    Assistant.say(Audio)
    Assistant.runAndWait()

def Speak1(Audio):

    Assistant = pyttsx3.init('sapi5')
    voices = Assistant.getProperty('voices')
    Assistant.setProperty('voice', voices[1].id)
    Assistant.setProperty('rate',200)

    print("   ")
    print(f"Jarvis: {Audio}")
    Assistant.say(Audio)
    Assistant.runAndWait()

def takecommand(): 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("          ")
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"Your Command :  {query}\n")

    except:   
        return "None"
        
    return query.lower()


Speak('Booting Jarvis')


def dictionary():
    Speak('Activated Dictionary!')
    Speak1('Tell Me The Problem!')
    Problem = takecommand()

    if 'meaning' in Problem:
        Problem = Problem.replace("jarvis","")
        Problem = Problem.replace("what","")
        Problem = Problem.replace("is","")
        Problem = Problem.replace("the","")
        Problem = Problem.replace("meaning","")
        Problem = Problem.replace("of","")

        resurlt = Dictionary.meaning(Problem)
        Speak1(f"The Meaning For {Problem} is {resurlt}")

    elif 'synonym' in Problem:
        Problem = Problem.replace("jarvis","")
        Problem = Problem.replace("what","")
        Problem = Problem.replace("is","")
        Problem = Problem.replace("the","")
        Problem = Problem.replace("synonym","")
        Problem = Problem.replace("of","")

        resurlt = Dictionary.synonym(Problem)
        Speak1(f"The Synonym For {Problem} is {resurlt}")

    elif 'antonym' in Problem:
        Problem = Problem.replace("jarvis","")
        Problem = Problem.replace("what","")
        Problem = Problem.replace("is","")
        Problem = Problem.replace("the","")
        Problem = Problem.replace("anonym","")
        Problem = Problem.replace("of","")

        resurlt = Dictionary.antonym(Problem)
        Speak1(f"The Anonym For {Problem} is {resurlt}")

    Speak('Exited Dictionary')
        
def screenshot():
    Speak('Ok Sir!')
    keyboard.press_and_release("windows + prt sc")
    
def Reader():
    Speak("Tell Me The Name Of The Book!")

    name = takecommand()

    if 'english' in name:

        os.startfile('C:\\Users\\WINDOWS 8.1 PRO\\Downloads\\gehc1dd\\gehc101.pdf')
        book = open('C:\\Users\\WINDOWS 8.1 PRO\\Downloads\\gehc1dd\\gehc101.pdf','rb')
        pdfreader = PyPDF2.PdfFileReader(book)
        pages = pdfreader.getNumPages()

        Speak(f"Number Of Pages In This Books Are {pages}")
        Speak("From Which Page I Have To Start Reading ?")
        numPage = int(input("Enter The Page Number :"))
        page = pdfreader.getPage(numPage)
        text = page.extractText()
        Speak("In Which Language , I Have To Read ?")
        lang = takecommand()

        if 'hindi' in lang:
            transl = Translator()
            textHin = transl.translate(text,'hi')
            textm = textHin.text
            speech = gTTS(text = textm )
            try:
                speech.save('book.mp3')
                playsound('book.mp3')

            except:
                playsound('book.mp3')

        else:
            Speak(text)

    elif 'english chapter 2' in name:
        os.startfile('C:\\Users\\WINDOWS 8.1 PRO\\Downloads\\gehc1dd\\gehc102')
        book = open('C:\\Users\\WINDOWS 8.1 PRO\\Downloads\\gehc1dd\\gehc102','rb')
        pdfreader = PyPDF2.PdfFileReader(book)
        pages = pdfreader.getNumPages()
        Speak(f"Number Of Pages In This Books Are {pages}")
        Speak("From Which Page I Have To Start Reading ?")
        numPage = int(input())
        page = pdfreader.getPage(numPage)
        text = page.extractText()
        Speak("In Which Language , I Have To Read ?")
        lang = takecommand()

        if 'hindi' in lang:
            transl = Translator()
            textHin = transl.translate(text,'hi')
            textm = textHin.text
            speech = gTTS(text = textm )
            try:

                speech.save('book.mp3')
                playsound('book.mp3')

            except:
                playsound('book.mp3')

        else:
            Speak(text)




def TaskExe():

    while True:

        query = takecommand()

        if 'youtube search' in query:
            Speak("Ok Sir, This Is What I Found For Your Search!")
            query = query.replace("jarvis","")
            query = query.replace("youtube search","")
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            Speak('Done, Sir')

        elif 'google search' in query:
            Speak("Ok Sir, This Is What I Found For Your Search!")
            query = query.replace("jarvis","")
            query = query.replace("google search","")
            pywhatkit.search(query)
            Speak('Done, Sir')

        elif 'open google' in query:
            Speak('Ok Sir, Launching...')
            webbrowser.open('https://www.google.com/')
            Speak('Done, Sir')

        elif 'open youtube' in query:
            Speak('Ok Sir, Launching...')
            webbrowser.open('https://www.youtube.com/')
            Speak('Done, Sir')

        elif 'open stack overflow' in query:
            Speak('Ok Sir, Launching...')
            webbrowser.open('https://stackoverflow.com/')
            Speak('Done, Sir')

        elif 'open gmail' in query:
            Speak('Ok Sir, Launching...')
            webbrowser.open('https://mail.google.com/mail/u/0/')
            Speak('Done, Sir')

        elif 'open firebase' in query:
            Speak('Ok Sir, Launching...')
            webbrowser.open('https://firebase.google.com/')
            Speak('Done, Sir')

        elif 'open white hat junior' in query:
            Speak('Ok Sir, Launching...')
            webbrowser.open('https://code.whitehatjr.com/s/dashboard')
            Speak('Done, Sir')

        elif 'open whitehat junior' in query:
            Speak('Ok Sir, Launching...')
            webbrowser.open('https://code.whitehatjr.com/s/dashboard')
            Speak('Done, Sir')

        elif 'open github' in query:
            Speak('Ok Sir, Launching...')
            webbrowser.open('https://github.com/')
            Speak('Done, Sir')

        elif 'wikipedia' in query:
            Speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            query = query.replace("Jarvis","")
            query = query.replace("search","")
            query = query.replace("in","")
            wiki = wikipedia.summary(query,3)
            Speak("According to wikipedia")
            Speak1(wiki)

        elif 'whatsapp message to dad' in query:
            Speak('Who Whom Should I Send Message?')
            Person = takecommand()
            Speak('Ok Sir, What Message Should I Send?')
            messageTXT = takecommand()
            Speak(f"Ok Sir, Sending Message{Person}")
            Ddaidu = "+919469210970"
            openChat = "https://web.whatsapp.com/send?phone=" + Ddaidu + "&text=" + messageTXT
            webbrowser.open(openChat)
            time.sleep(30)
            keyboard.press('enter')

        elif 'hello' in query:
            Speak("Hello Sir , How Are You ?")

        elif 'who are you' in query:
            Speak("I Am Jarvis, Sir")
            Speak("Your Personal A.I. Assistant")

        elif 'open visual studio code' in query:
            Speak('Ok Sir, Opening Visual Studio Code')
            os.startfile("G:\\Arnav\\visual studio code\\Microsoft VS Code\\Code.exe")

        elif 'open excel' in query:
            Speak('Ok Sir, Opening Microsoft Excel')
            os.startfile("C:\\ProgramData\\Microsoft\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Excel 2007")

        elif 'open word' in query:
            Speak('Ok Sir, Opening Microsoft Word')
            os.startfile("C:\\ProgramData\\Microsoft\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Word 2007")

        elif 'open powerpoint' in query:
            Speak('Ok Sir, Opening Microsoft Powerpoint Presentation')
            os.startfile("C:\\ProgramData\\Microsoft\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office PowerPoint 2007")

        elif 'open publisher' in query:
            Speak('Ok Sir, Opening Microsoft Office Publisher 2007')
            os.startfile("C:\\ProgramData\\Microsoft\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Publisher 2007")

        elif 'open infopath' in query:
            Speak('Ok Sir, Opening Microsoft Office InfoPath 2007')
            os.startfile("C:\\ProgramData\\Microsoft\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office InfoPath 2007")

        elif 'open chrome' in query:
            Speak('Ok Sir, Opening Google Crome')
            os.startfile("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")

        elif 'open file' in query:
            Speak('Ok Sir, Opening File Explorer')
            os.startfile("C:\\Users\\WINDOWS 8.1 PRO\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\Programs\\System Tools\\File Explorer")

        elif 'open zoom' in query:
            Speak('Ok Sir, Opening Zoom Meeting')
            os.startfile("C:\\Users\WINDOWS 8.1 PRO\\AppData\Roaming\\Zoom\\bin\\Zoom.exe")

        elif 'open cisco' in query:
            Speak('Ok Sir, Opening Cisco Webex Meet')
            os.startfile("C:\\Users\\WINDOWS 8.1 PRO\AppData\\Local\\WebEx\\WebEx\\Applications\\ptoneclk.exe")

        elif 'thank you' in query:
            Speak('No Problem, Sir')
            Speak("Your Command Is My Order")

        elif 'hai' in query:
            Speak('Hi Sir')

        elif 'hi' in query:
            Speak('Hi Sir')     

        elif 'close visual studio code' in query:
            Speak('Ok Sir, Closing Visual Studio Code')
            os.system("TASKKILL /F /im Code.exe")

        elif 'full screen' in query:
            keyboard.press("k")

        elif 'open homepage' in query:
            keyboard.press_and_release("alt + home")

        elif 'back' in query:
            keyboard.press_and_release("alt + left arrow")

        elif 'forward' in query:
            keyboard.press_and_release("alt + right arrow")

        elif 'joke' in query:
            Speak('Ok Sir')
            joke = pyjokes.get_joke()
            Speak1(joke)

        elif 'repete my words' in query:
            myWords = takecommand()
            Speak1(myWords)

        elif 'my location' in query:
            Speak('Ok Sir, Your Location Is')
            webbrowser.open("https://www.google.com/maps/place/Varanasi,+Uttar+Pradesh/@25.3723553,82.6495571,86234m/data=!3m2!1e3!4b1!4m5!3m4!1s0x398e32675987939f:0xb7a2216aae9cc02a!8m2!3d25.3520828!4d82.9501558")

        elif 'dictionary' in query:
            dictionary()

        elif 'remember that ' in query:
            rememberMessage = query.replace("remeber","")
            rememberMessage = rememberMessage.replace("jarvis","")
            rememberMessage = rememberMessage.replace("hello","")
            rememberMessage = rememberMessage.replace("that","")
            Speak(f"Ok Sir I Will Remember That {rememberMessage}")
            remember = open('data.txt','w')
            remember.write(rememberMessage)
            remember.close

        elif 'do you remember' in query:
            remember = open('data.txt','r')
            Speak("You told me to remember that " + remember.read())

        elif 'book' in query:
            Reader()

        elif 'screenshot' in query:
            screenshot()


Speak('Jarvis Booted')
TaskExe()
