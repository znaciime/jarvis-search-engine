from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyttsx3 as ps
import PySimpleGUI as pgui
import time
#install libraries
#install web driver in this case Google Chrome version 89
#add web driver to path 
pgui.theme("DarkAmber")

speak_voice=ps.init()
search_input=[[pgui.Text("Type in question"),
pgui.Input(size=(30,2), enable_events=True, key="-SEARCH-"),
pgui.Button("OK"),
pgui.Button("Exit")]]


programwindow = pgui.Window(title="Jarvis Help Engine", layout=search_input, margins=(200,200))

speak_voice.say("Hello i am Jarvis help engine, type in question")
speak_voice.runAndWait()
while True:
    event, values = programwindow.read()
    if event =="OK":
        search_input = values["-SEARCH-"]
        driver = webdriver.Chrome('C:/bin/chromedriver.exe')
    try:
        driver.get('http://wikipedia.org/wiki/'+search_input)
        time.sleep(4)
        elem=driver.find_element_by_id("mw-content-text")
        print(elem.text)
        time.sleep(5)
        search_result=elem.text
        print(speak_voice.isBusy())
        speak_voice.say(search_result)
        speak_voice.runAndWait()
        driver.close()
    except:
        print("No search results")
    if event == "Exit" or event == pgui.WIN_CLOSED:
        break
programwindow.close()
speak_voice.stop()


