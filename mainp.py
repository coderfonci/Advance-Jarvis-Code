from ast import If
from doctest import master
import re
from unicodedata import name
import pyttsx3
#import PySimpleGUI as sg 
import webbrowser
import speech_recognition as sr
import datetime
from platform import release
import keyboard
from keyboard import press
from time import sleep


#========================

                    
                    
                    
                    

name = 'master'
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 178)

#print=sg.Print

def speak(audio): 
    engine.say(audio) 
    engine.runAndWait() 

def takeCommand():
      
    r = sr.Recognizer()
      
    with sr.Microphone() as source:
        print ('\U0001F600')
        print("Listening...") 
        r.energy_threshold = 500
        r.pause_threshold = 0.7
        r.non_speaking_duration = 0.2        
        audio = r.listen(source,timeout=7, phrase_time_limit=7)
        
    
    try: 
        print("Recognizing...")     
        query = r.recognize_google(audio, language ='en-in') 
        print(f"User said: {query}\n")
        
    
    except Exception as e: 
        print(e)
        #print("Unable to Recognizing your voice.")
        #speak("Sorry, I didn't get that.")
        return "None"

    return query 

def close_tab(): 
    key = keyboard.press_and_release('Ctrl + w')

    return key 
def down_tab(): 
    key = keyboard.press_and_release('down arrow')
    return key 
def up_tab(): 
    key = keyboard.press_and_release('up arrow')
    return key 

if __name__ == '__main__': 
    query=takeCommand().lower()
    while True : 
        query=takeCommand().lower()
        if 'program' in query : 
            print('in')
            speak('i am online')
            while True:
                query=takeCommand().lower()
                n = query
                c = 'close'
                d = 'down'
                u = 'up'
                if n=='close':
                    speak('This tab going to close..')
                    close_tab()
                elif n=='down':
                    down_tab()
                elif n=='up':
                    up_tab()
                    
                elif'start' in query: 
                    sleep(1)
                    keyboard.press_and_release('spacebar')
                elif'pause' in query: 
                    sleep(1)
                    keyboard.press_and_release('spacebar')

                elif 'help'in query : 
                    speak('ok what a question.')
                    print ('\U0001F607')
                    while True:
                        r = sr.Recognizer()
                        with sr.Microphone() as source:
                            print ('\U0001F600')
                            print("Listening...") 
                            r.energy_threshold = 500
                            r.pause_threshold = 0.7
                            r.non_speaking_duration = 0.2        
                            audio = r.listen(source,timeout=7, phrase_time_limit=7)
                        try:      
                            print("Recognizing...")     
                            find1 = r.recognize_google(audio, language ='en-in') 
                            #print(f"User said: {query}\n") 
                            n = find1
                            s = 'back'
                            c = 'close'
                            d = 'down'
                            u = 'up'
                            if n==s: 
                                speak('i got it lets go back')
                                break
                            elif n=='music please':
                                speak('ok sir. ')
                                webbrowser.open(f'https://soundcloud.com/user-693938217/sets/gangsta?utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing')
                                speak('3.. 2. 1.')
                            elif n=='close':
                                speak('This tab going to close..')
                                close_tab()
                            elif n=='down':
                                down_tab()
                            elif n=='up':
                                up_tab()
                                
                            else:
                                webbrowser.open(f'https://www.google.com/search?q={find1}')
                                speak(f'i got it {find1}')  
                        except Exception as e: 
                            print(e)         

                elif 'open youtube'in query : 
                    speak('you are in youtube ')
                    print ('\U0001F607')
                    while True:
                        r = sr.Recognizer()
                        with sr.Microphone() as source:
                            print ('\U0001F600')
                            print("Listening...") 
                            r.energy_threshold = 500
                            r.pause_threshold = 0.7
                            r.non_speaking_duration = 0.2        
                            audio = r.listen(source,timeout=7, phrase_time_limit=7)
    
                        try: 
                            
                            print("Recognizing...")     
                            find1 = r.recognize_google(audio, language ='en-in') 
                            #print(f"User said: {query}\n") 
                            n = find1
                            s = 'back'
                            c = 'close'
                            d = 'down'
                            u = 'up'
                            if n==s: 
                                speak('i got it lets go back')
                                break
                            elif n=='feel free':
                                speak('ok sir. ')
                                webbrowser.open(f'https://www.youtube.com/watch?v=QOjmvL3e7Lc')
                                speak('open windows 3. 2.. 1.')
                            elif n=='close':
                                speak('This tab going to close..')
                                close_tab()
                            elif n=='down':
                                down_tab()
                            elif n=='up':
                                up_tab()
                            else:
                                webbrowser.open(f'https://www.youtube.com/results?search_query={find1}')
                                speak(f'i got it {find1}')   
                        except Exception as e: 
                            print(e)  
                elif 'movies'in query : 
                    speak('you are in movies area ')
                    print ('\U0001F607')
                    while True:
                        r = sr.Recognizer()
                        with sr.Microphone() as source:
                            print ('\U0001F600')
                            print("Listening...") 
                            r.energy_threshold = 500
                            r.pause_threshold = 0.7
                            r.non_speaking_duration = 0.2        
                            audio = r.listen(source,timeout=7, phrase_time_limit=7)
    
                        try: 
                            
                            print("Recognizing...")     
                            find1 = r.recognize_google(audio, language ='en-in') 
                            #print(f"User said: {query}\n") 
                            n = find1
                            s = 'back'
                            c = 'close'
                            d = 'down'
                            u = 'up'
                            if n==s: 
                                speak('i got it lets go back')
                                break
                            elif n=='Netflix':
                                speak('ok sir. ')
                                webbrowser.open(f'https://www.netflix.com/browse')
                                speak('open netfilx 3. 2.. 1.')
                            elif n=='close':
                                speak('This tab going to close..')
                                close_tab()
                            elif n=='down':
                                down_tab()
                            elif n=='up':
                                up_tab()
                            else:
                                webbrowser.open(f'https://moviezverse.net/?s={find1}')
                                speak(f'i got it {find1}')
                        except Exception as e: 
                            print(e)  
                
                elif 'clean' in query: 
                    speak("Please don't touch mouse and keyboard sir")
                    speak("3, 2, 1,  start ")
                    sleep(1)
                    keyboard.press("Windows")
                    keyboard.release("Windows")
                    sleep(1)
                    keyboard.write("cmd")
                    sleep(1)
                    press('enter')
                    keyboard.release('enter')
                    sleep(1)
                    keyboard.write("tree")
                    press('enter')
                    keyboard.release('enter')
                    speak("System scaning start")

                    sleep(25)
                    keyboard.write("exit")
                    press('enter')
                    keyboard.release('enter')
                    speak("System scaning start")
                
                elif 'full scan' in query: 
                
                    speak("Please don't touch mouse and keyboard sir")
                    speak("3, 2, 1,  start ")
                    sleep(1)
                    keyboard.press_and_release('Windows')
                    sleep(1)
                    keyboard.write("Virus & threat protection")
                    sleep(1)
                    keyboard.press_and_release('enter')
                    sleep(3)
                    keyboard.press_and_release('TAB')
                    sleep(1)
                    keyboard.press_and_release('enter')
                    sleep(1)
                    keyboard.press_and_release('TAB')
                    keyboard.press_and_release('TAB')
                    sleep(1)
                    keyboard.press_and_release('down arrow')
                    sleep(1)
                    keyboard.press_and_release('spacebar')
                    sleep(1)
                    keyboard.press_and_release('TAB')
                    keyboard.press_and_release('TAB')
                    keyboard.press_and_release('TAB')
                    sleep(1)
                    keyboard.press_and_release('enter')
                    sleep(1)
                    keyboard.press_and_release('up arrow')
                    keyboard.press_and_release('up arrow')
                    speak("System scaning start")

                elif 'make new python project' in query: 
                    #Alt + Spacebar + C
                    speak("Please don't touch mouse and keyboard sir")
                    speak("3, 2, 1,  start ")
                    sleep(6)
                    sleep(1)
                    keyboard.press_and_release('Windows')
                    sleep(1)
                    keyboard.write("cmd")
                    sleep(1)
                    keyboard.press_and_release('enter')
                    sleep(1)
                    keyboard.write("cd OneDrive")
                    keyboard.press_and_release('enter')
                    sleep(1)
                    keyboard.write("cd desktop")
                    keyboard.press_and_release('enter')
                    keyboard.write("mkdir MUSIKKU")
                    sleep(1)
                    keyboard.press_and_release('enter')
                    sleep(1)
                    keyboard.write("cd MUSIKKU")
                    sleep(1)
                    keyboard.press_and_release('enter')
                    sleep(1)
                    sleep(1)
                    keyboard.write("notepad test.py")
                    sleep(1)
                    keyboard.press_and_release('enter')
                    sleep(2)
                    keyboard.press_and_release('enter')
                    sleep(2)
                    keyboard.press_and_release('Alt + F4')
                    sleep(1)
                    keyboard.write("code .")
                    keyboard.press_and_release('enter')
                    sleep(6)
                    keyboard.press_and_release('Ctrl + q')
                    sleep(1)
                    keyboard.press_and_release('down arrow')
                    sleep(2)
                    keyboard.press_and_release('enter')
                    sleep(2)
                    keyboard.write("# New Projece ")
                    sleep(1)
                    keyboard.write("\nprint('hello world')")
                    sleep(1)
                    """keyboard.write("(")
                    sleep(1)
                    keyboard.write("'hello'")
                    sleep(1)
                    keyboard.write(")")"""
                    sleep(1)
                    keyboard.write("\n#ready to code..")
                    speak("your new project ready to run sir")

                elif 'sleep' in query : 
                    speak('i got it\n ok i am going to sleep')
                    break
        elif 'bye' in query: 
            print(f'ok bye {name}')
            speak(f'ok bye {name}')
            break
            
                #if '' in query:
                 #   speak(f'ok i to close.')
                  #  query = query.replace("youtube", "")
                   # results =webbrowser.open(f'https://www.youtube.com/results?search_query={query}')
                    #speak('i got it.')

        
        
      
                