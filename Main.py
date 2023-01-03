from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import cv2
from time import sleep, strftime
import keyboard
import pyttsx3
from tkvideo import tkvideo
import bs4 as BeautifulSoup
import requests, json
import subprocess
import sys
import sys
import subprocess
import threading 
import subprocess
import wolframalpha
import pyttsx3
import tkinter
import keyboard
from keyboard import press 
from keyboard import write
from time import sleep
import psutil
import platform
from datetime import datetime
import random
import requests
from bs4 import BeautifulSoup
import bs4
import screen_brightness_control as sbc
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
from os import spawnle, startfile
# import pyautogui
# from pyautogui import click
import keyboard
from keyboard import press 
from keyboard import write
from time import sleep
import winshell
import pyjokes
import smtplib
import ctypes
import time
import requests
import shutil
from bs4 import BeautifulSoup
import cv2
import numpy

######################################### System Information #############################
System_name = "JARVIS"
##########################################################################################
######################################### User Information ###############################
user = "Adnan"
################
try:# location finder in try
    ipAdd = requests.get('https://api.ipify.org').text
    print(ipAdd)
    url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
    geo_requests = requests.get(url)
    geo_data = geo_requests.json()
    city = geo_data['city']
    # print(geo_data)
    country = geo_data['country']
    my_current_location = city,country
except:# location error
    print('     ')
#################
Gender = "Male"
##########################################################################################



def speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.setProperty('rate',220)
    print(f"JARVIS: ",audio)
    engine.say(audio)
    engine.runAndWait()

def main_tkinter_gui():
   

    class MyLabel(Label):
        def __init__(self, master, filename):
            im = Image.open(filename)
            seq =  []
            try:
                while 1:
                    seq.append(im.copy())
                    im.seek(len(seq)) # skip to next frame
            except EOFError:
                pass # we're done

            try:
                self.delay = im.info['duration']
            except KeyError:
                self.delay = 100

            first = seq[0].convert('RGBA')
            self.frames = [ImageTk.PhotoImage(first)]

            Label.__init__(self, master, image=self.frames[0])

            temp = seq[0]
            for image in seq[1:]:
                temp.paste(image)
                frame = temp.convert('RGBA')
                self.frames.append(ImageTk.PhotoImage(frame))

            self.idx = 0

            self.cancel = self.after(self.delay, self.play)

        def play(self):
            self.config(image=self.frames[self.idx])
            self.idx += 1
            if self.idx == len(self.frames):
                self.idx = 0
            self.cancel = self.after(self.delay, self.play)   


    
        
    class Redirect():

        def __init__(self, widget, autoscroll=True):
            self.widget = widget
            self.autoscroll = autoscroll

        def write(self, text):
            self.widget.insert('end', text)
            if self.autoscroll:
                self.widget.see("end")  # autoscroll
            

    
    def run():
        threading.Thread(target=task).start()
        def flush(self):
           pass

    def guide_task():
        speak("verification successful")
        print(" ")
        print("Hey! there I am Jarvis")
        print("Please press Initiate system , to start.")
        print("Then I can help you with variety of tasks.")
        print(" ")

    def guide_run():
        threading.Thread(target=guide_task).start()

    def task():
        
        print(f"Hello {user} Please")
        print("Press Initiate system button , to start.")
        print("Then I can help you with variety of tasks.")

        def speak(audio):
            engine = pyttsx3.init('sapi5')
            voices = engine.getProperty('voices')
            engine.setProperty('voice',voices[1].id)
            engine.setProperty('rate',220)
            print(f"JARVIS: ",audio)
            engine.say(audio)
            engine.runAndWait()


        def Listen():
            
            r = sr.Recognizer()
            
            with sr.Microphone() as source:
                
                print("\nListening...")
                r.pause_threshold = 0.7
                audio = r.listen(source)
        
            try:
                print("\nRecognizing...")   
                query = r.recognize_google(audio, language ='en-in')
                print(f"User said: {query}\n")
                
        
            except Exception as e:
                print(e)   
                print("Unable to Recognize your voice.") 
                return "None"
            
            return query


        def wolfram(query):
            api_key = "4Y594Q-5TAGRTVW86"
            requester = wolframalpha.Client(api_key)
            requested = requester.query(query)

            try:
                answer = next(requested.results).text
                return answer

            except:
                speak("no data found")

        def calculator(query):

            term = str(query)
            term = term.replace("jarvis","")
            term = term.replace("plus","+")
            term = term.replace("minus","-") 
            term = term.replace("multiply","*")
            term = term.replace("divide","/")
            term = term.replace("into","*")

            final = str(term)

            try:    
                result1 = wolfram(final)
                print(F"{result1}")
                speak(F"{result1}")
            except:
                speak("sorry, i don't have the answer for that .....")


        def temp(query):

            term = str(query)
            term = term.replace("jarvis","")
            term = term.replace("temperature","")
            term = term.replace("in","")
            term = term.replace("what is the","")

            temp_query = str(term)

            if 'outside' in query:
                var1 = 'temperature in' + my_current_location

                answer = wolfram(var1)
                print(f"{var1} Is {answer}")
                speak(f"{var1} Is {answer}")

            else : 
                var2 = 'temperature in' + temp_query

                answ = wolfram(var2)
                print(f"{var2} Is{answ}")
                speak(f"{var2} Is{answ}")


        def get_size(bytes, suffix="B"):
            factor = 1024
            for unit in ["", "K", "M", "G", "T", "P"]:
                if bytes < factor:
                    return f"{bytes:.2f}{unit}{suffix}"
                bytes /= factor



        def wishMe():
            hour = int(datetime.datetime.now().hour)
            if hour>= 0 and hour<12:
                morning = "Good Morning" , user, Gender
                speak(morning)
        
            elif hour>= 12 and hour<16:
                afternoon = "Good Afternoon", user,Gender
                speak(afternoon)  
        
            else:
                evening = "Good Evening", user ,Gender
                speak(evening) 



        





        first_Command = 1
        while True:
            if first_Command == 1 : 
                store_1 = "Welcome",user," I am here to help you!"
                store_2 = System_name,"in your service", user
                store_3 = user, "How may i help you"
                command_reply = [store_1,store_2,store_3]
                speak(random.choice(command_reply))
            else:
                if 'none' in query:
                    print(' ')
                else:
                    store_4 = "What's the next command for me", user
                    store_5 = "What's your next command", user,"?"
                    next_command_reply = ["What would you like me to help you next with?","How can i help you next?",store_4,"Ready to take next command, Your commands at priority",store_5 ]
                    speak(random.choice(next_command_reply))

            query = Listen().lower()
            
            if 'hello'  in query:
                var_reply_1 = "hello" ," ",user,", how may i help you?"
                var_reply_2 = "hello",user
                var_reply_3 = "hi",user , "What is the command for me ?"
                var_reply_hello = [var_reply_1,var_reply_2,var_reply_3]
                speak(random.choice(var_reply_hello))

            elif 'open youtube' in query:
                speak("Here you go to Youtube")
                try:
                    webbrowser.open("https://www.youtube.com/")
                except:
                    speak("sorry , but i am unable to do so.")
            
            elif 'open google' in query:
                speak("Here you go to Google\n")
                try:
                    webbrowser.open("https://www.google.com/")
                except:speak("sorry , but i am unable to do so.")

            elif 'wikipedia' in query:
                speak('Searching Wikipedia...')
                try:
                    query = query.replace("wikipedia", "")
                    query = query.replace("according to wikipedia", "")
                    query = query.replace(System_name, "")
                    results = wikipedia.summary(query, sentences = 3)
                    speak("According to Wikipedia")
                    speak(results)
                except:
                    speak("sorry , no results found.")
            
            elif 'open vedantu' in query:
                speak("opening vedantu")
                try:
                    webbrowser.open("https://www.vedantu.com/")
                except:
                    speak("sorry , but i am unable to do so.")

            elif 'time' in query:
                try:
                    now = datetime.datetime.now()
                    current_time = now.strftime("%H:%M:%S")
                    speak("the time is now" )
                    speak(current_time)
                except:
                    speak("unable to get time")

            elif 'how are you' in query:
                try:
                    health_type_how_are_you = ['i am fine how about you sir?','i am great how about you sir?','My A I mood levels are always positive sir , how about you sir?']
                    speak(random.choice(health_type_how_are_you))
                    fine_reply_back = Listen()
                    if 'fine' in fine_reply_back:
                        try:
                            health_type_fine = ["it's good to know that you are fine sir",'I am impressed.']
                            speak(random.choice(health_type_fine))
                        except:
                            speak("it's good to know that you are fine sir")
                except:
                    speak('i am fine how about you sir?')
                    if 'fine' in fine_reply_back:
                        try:
                            health_type_fine = ["it's good to know that you are fine sir",'I am impressed.']
                            speak(random.choice(health_type_fine))
                        except:
                            speak("it's good to know that you are fine sir")

            elif 'none' in query:
                speak("unable to recognise your voice ..")

            elif 'exit' in query:
                speak("Thanks for giving me your time")
                screen_main.destroy()
                exit()

            elif 'joke' in query:
                try:
                    speak(pyjokes.get_joke())
                except:
                    speak("unable to get joke , but still you can smile")

            elif 'search'  in query:
                try:
                    query = query.replace("search", "")
                    query = query.replace("jarvis","")
                    search_query = "Ok",Gender,"Searching" ,query,"in google"
                    speak(search_query)
                    webbrowser.open("https://www.google.com/search?q=" + query)
                except:
                    speak("unable to search in google ")

            
            elif 'change background' in query:
                try:
                    ctypes.windll.user32.SystemParametersInfoW(20,
                                                            0,
                                                            "Location of wallpaper",
                                                            0)
                    speak("background changed successfully")
                except:
                    speak("unable to change desktop background")

            elif 'lock window' in query:
                try:
                    speak("locking the device")
                    ctypes.windll.user32.LockWorkStation()
                except:
                    speak("unable to lock the device.")

            
            elif 'shutdown system' in query:
                try:
                    speak("Hold On a Sec ! Your system is on its way to shut down")
                    speak("are you sure you want to shutdown this Pc")
                    subprocess.call('shutdown / p /f')
                    condition = Listen().lower()
                    if "yes" in condition:
                        speak("shutting down the system")
                        subprocess.call('shutdown / p /f')
                    else:
                        speak("ok sir system shutdown command rejected..")
                except:
                    speak("unable to shutdown system")

            elif 'empty recycle bin' in query:
                try:
                    winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
                    speak("Recycle Bin Recycled")
                except:
                    speak("unable to empty recycle bin.")
            
            elif "stop listening" in query:
                speak("for how much time you want to stop jarvis from listening commands")
                a = int(Listen())
                try:
                    sleep(a)
                    speak("i am back sir ! ")
                except:
                    speak("i am not going to sleep because of some system error")

            elif 'sleep' in query:
                try:       
                    speak("ok sir .")            
                    var = IntVar()
                    def sleep_var():
                        var.set(1)
                    def destroy_button():
                        button_sleep.pack_forget()
                    button_sleep = Button(screen_main, text="Backup",font=('space age',13), command=lambda:[sleep_var(),destroy_button()])
                    button_sleep.place(x=700,y=400)

                    print("\nSleeping...😴😴😴")
                    button_sleep.wait_variable(var)
                    speak("I am back in your service sir")
                except:
                    speak("i am not going to sleep because of some system error")

            elif "where is" in query:
                try:
                    query = query.replace("jarvis","")
                    query = query.replace("where is","")
                    location = query
                    reply_location = "Locating",location, " in google maps"
                    speak(reply_location)
                    webbrowser.open("http://www.google.com/maps/place/"+location)
                except:
                    speak("unable to locate this place")

            elif 'restart' in query:
                try:
                    speak("Hold On a Sec ! Your system is on its way to restart")
                    speak("are you sure you want to restart this Pc")
                    condition_1 = Listen().lower()
                    if "yes" in condition_1:
                        speak("shutting down the system")
                        subprocess.call(["shutdown", "/r"])
                    else:
                        speak("ok sir system restart command rejected..")
                except:
                    speak("unable to restart system")

            elif "write a note" in query:
                speak("What should i write, sir")
                try:
                    note = Listen()
                    file = open('jarvis.txt', 'w')
                    time_reply = Gender," Should i include date and time"
                    speak(time_reply)
                    snfm = Listen()
                    if 'yes' in snfm or 'sure' in snfm:
                        try:
                            strTime = datetime.datetime.now().strftime("% H:% M:% S")
                            file.write(strTime)
                            file.write(" :- ")
                            file.write(note)
                        except:
                            speak("unable to write time in note, Sorry but note has been written without time")
                            file.write(note)
                    else:
                        file.write(note)
                except:
                    speak("unable to write note")

            elif "show note" in query:
                speak("Showing Notes")
                file = open("jarvis.txt", "r")
                speak(file.read())


            elif 'date' in query:
                try:
                    from datetime import date
                    today = date.today()
                    dati = today.strftime("%B %d, %Y")
                    DATE_to_be_said = "Today's date is ",dati
                except:
                    speak("I don't know today's date , Apologizes for that")

            elif 'system information' in query:
                try:
                    print("="*15, "System Information", "="*15)
                    speak("System Information")
                    uname = platform.uname()
                    speak(f"System: {uname.system}")
                    speak(f"Node Name: {uname.node}")
                    speak(f"Release: {uname.release}")
                    speak(f"Version: {uname.version}")
                    speak(f"Machine: {uname.machine}")
                    speak(f"Processor: {uname.processor}")
                except:
                    speak("unable to get system information")

            elif 'cpu information' in query:
                try:
                    print("="*15, "CPU Info", "="*15)
                    cpu_physical_core = "this cpu has",  psutil.cpu_count(logical=False),"physical cores"
                    speak(cpu_physical_core)
                    Total_core_cpu = "Total cores:", psutil.cpu_count(logical=True)
                    speak(Total_core_cpu)
                except:
                    speak("unable to get CPU information")

            
            elif 'frequency of cpu' in query:
                try:
                    cpufreq = psutil.cpu_freq()
                    speak(f"Max Frequency: {cpufreq.max:.2f}Mhz")
                    speak(f"Min Frequency: {cpufreq.min:.2f}Mhz")
                    speak(f"Current Frequency: {cpufreq.current:.2f}Mhz")
                except:
                    speak("unable to get Frequency of CPU")


            elif 'usage of cpu' in query:
                try:
                    speak("the cpu usage per core is displayed here ")
                    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
                        print(f"Core {i}: {percentage}%")
                    speak(f"And Total CPU Usage: {psutil.cpu_percent()}%")
                except:
                    speak("unable to get CPU usage")

            elif 'memory information' in query:
                try:
                    print("="*15, "Memory Information", "="*15)
                    speak("the memory information of this computer is")
                    svmem = psutil.virtual_memory()
                    speak(f"Total: {get_size(svmem.total)}")
                    speak(f"Available: {get_size(svmem.available)}")
                    speak(f"Used: {get_size(svmem.used)}")
                    speak(f"Percentage: {svmem.percent}%")
                    print("="*20, "SWAP", "="*20)
                    speak('the swap memory details are')
                    swap = psutil.swap_memory()
                    speak(f"Total: {get_size(swap.total)}")
                    speak(f"Free: {get_size(swap.free)}")
                    speak(f"Used: {get_size(swap.used)}")
                    speak(f"Percentage: {swap.percent}%")
                except:
                    speak("unable to get memory information")


            elif  'launch powerpoint' in query:
                try:
                    speak("launching microsoft powerpoint")
                    os.system("powerpnt")
                except:
                    speak("unable to launch microsoft powerpoint")

            elif "weather"  in query:
                try:
                    temperature_reply = "the temperature in " , city, "is" , temperature 
                    speak(temperature_reply)
                    press_reply = "pressure is ",pressure
                    speak(press_reply)
                    speak("humidity is ")
                    speak(humidity)
                    sky_data_reply = "Sky Description is  ", description
                    speak(sky_data_reply)

                except:
                    speak("unable to get weather reports..")


            elif 'calculate' in query:
                try:
                    calculator(query)
                except:
                    speak("unable to calculate ,please try again")

            elif 'temperature' in query:
                try:
                    temp(query)
                except:
                    speak("unable to get temperature.")

            elif "what is"  in query:
                try:
                    client = wolframalpha.Client("4Y594Q-5TAGRTVW86")
                    res = client.query(query)
                    speak(next(res.results).text)
                except StopIteration:
                    speak("sorry , i don't have the answer for that ..")

            elif 'where i am' in query:
                speak("wait sir, let me check")
                try:
                    LOcation_parser_reply = "sir i think we are in",city,"city of ", country
                    speak(LOcation_parser_reply)
                except:
                    speak("sorry sir but i don't know where we are")

            else:
                not_var = user, "I am having problem in listening you"
                not_understood = ["sorry sir I didn't get that",not_var]
                speak(random.choice(not_understood))
                continue
            

            first_Command +=1

    screen_main = Tk()
    screen_main.attributes("-fullscreen", True)
    screen_main.configure(background="black")
    screen_main.iconbitmap("D:\\3D Objects\\CHANNEL\\HOBBY MASTER\\channel_logo.png")
    def color_changer():
        colors = ["green", "red" , "white" , "gold"]
        # choose and configure random color to the label text
        fg = random.choice(colors)
        label_creation.config(fg = fg)
        
        # call the color_changer() method after 200 micro seconds
        label_creation.after(1000, color_changer)
        
    label_creation = Label(screen_main, font=('space age', 30,'bold'))
    color_changer()
    label_creation.configure(text="Created By Adnan.")
    label_creation.configure(background="black")
    label_creation.place(x=960,y=5)
    
    
    def time():
        string = strftime('%H:%M:%S %p')
        label.config(text=string)
        label.after(1000,time)
        minute = strftime('%M')

    label = Label(screen_main,font=('futura bold',35),background="black",border="0",foreground="cyan")
    label.place(x=10,y=20)
    time()


    try:
        api_key = "fa5aab4feceb62541bf13bfa84259779"

        base_url = "http://api.openweathermap.org/data/2.5/weather?"

        city_name = city

        complete_url = base_url + "appid=" + api_key + "&q=" + city_name

        response = requests.get(complete_url)

        x = response.json()

        if x["cod"] != "404":

            y = x["main"]

            current_temperature = y["temp"]

            current_pressure = y["pressure"]

            current_humidity = y["humidity"]

            z = x["weather"]

            weather_description = z[0]["description"]
            temperature = round(float(float(current_temperature)-273.15)),"°C"
            pressure = round(float(current_pressure*0.000987)),"atm","(",current_pressure,"hpa )"
            humidity = current_humidity,"%"
            weather_description = z[0]["description"]
            description = weather_description

    except:
        print("Getting errors")

    else:
        print(" ")




    anim1_main = MyLabel(screen_main,"D:\\3D Objects\\python Projects\\Face-Recognition-main\\Project JARVIS Advanced\\Center main image.gif")
    anim1_main.configure(width=780,border="0",height=530)
    anim1_main.place(x=390,y=150)

    anim2_main = MyLabel(screen_main,"D:\\3D Objects\\python Projects\\Face-Recognition-main\\Project JARVIS Advanced\\Jarvis_intro.gif")
    anim2_main.configure(width=280,border="0",height=290)
    anim2_main.place(x=5,y=610)

    anim2_main = MyLabel(screen_main,"D:\\3D Objects\\python Projects\\Face-Recognition-main\\Project JARVIS Advanced\\suit.gif")
    anim2_main.configure(width=260,border="0",height=490)
    anim2_main.place(x=1200,y=200)



    geo_weather_data = temperature ,pressure , humidity,description
    Label(screen_main,text="Temperature in",
        font=('arial',20),foreground="cyan",border="0",background="black").place(x=870,y=190)
    Label(screen_main,text=city_name,
        font=('arial',20),foreground="cyan",border="0",background="black").place(x=1070,y=190)
    Label(screen_main,text="is",
        font=('arial',20),foreground="cyan",border="0",background="black").place(x=930,y=230)
    Label(screen_main,text=temperature,
        font=('arial',20),foreground="cyan",border="0",background="black").place(x=960,y=230)

    Label(screen_main,text="humidity:",
        font=('arial',20),foreground="cyan",border="0",background="black").place(x=955,y=265)
    Label(screen_main,text=humidity,
        font=('arial',20),foreground="cyan",border="0",background="black").place(x=1070,y=265)

    Label(screen_main,text="pressure is",
        font=('arial',20),foreground="cyan",border="0",background="black").place(x=970,y=300)
    Label(screen_main,text=pressure,
        font=('arial',20),foreground="cyan",border="0",background="black").place(x=975,y=340)

    Label(screen_main,text="sky description is",
        font=('arial',20),foreground="cyan",border="0",background="black").place(x=985,y=375)
    Label(screen_main,text=description,
        font=('arial',20),foreground="cyan",border="0",background="black").place(x=990,y=410)

    def battey_percentage():
        Label1 = Label(screen_main,text="Current Power Level at",
            font=('arial',20),foreground="cyan",border="0",background="black")
        Label1.place(x=560,y=650)

        battery = psutil.sensors_battery()
        plugged = battery.power_plugged
        percent = str(battery.percent)
        plugged = "Plugged In" if plugged else "Not Plugged In"

        string_battery = battery # 
        string_percent = percent,"%"
        Label2 = Label(screen_main,
            font=('arial',20),border="0",foreground="cyan",background="black")
        Label2.config(text=string_percent)
        Label2.place(x=850,y=650)
        Label2.after(10000,battey_percentage)

    
    battey_percentage()

    def YT_Channel():
        webbrowser.open("https://www.youtube.com/channel/UC9wt9ih0-acWfeWXLI5oDIQ")
    def Yt_studio():
        webbrowser.open("https://studio.youtube.com/channel/UC9wt9ih0-acWfeWXLI5oDIQ")
    def youtube():
        webbrowser.open("www.youtube.com")
    def whatsappweb():
        webbrowser.open("www.whatsappweb.com")
    def Vedantu():
        webbrowser.open("www.vedantu.com")
    def news():
        webbrowser.open("https://www.ndtv.com/")
    def google():
        webbrowser.open("www.google.com")
    def maps():
        webbrowser.open("https://maps.google.com/")
    def advertise():
        webbrowser.open("https://www.youtube.com/channel/UC9wt9ih0-acWfeWXLI5oDIQ?sub_confirmation=1")

        





    myyoutube = Button(screen_main,border="0",background="black",foreground="cyan", text="YOUTUBE", command=youtube,font="LUCIDA 15 bold")
    myyoutube.place(x=520,y=190)

    my_news = Button(screen_main,border="0",background="black",foreground="cyan", text="News", command=news,font="LUCIDA 15 bold")
    my_news.place(x=530,y=230)
    
    my_maps = Button(screen_main,border="0",background="black",foreground="cyan", text="maps", command=maps,font="LUCIDA 15 bold")
    my_maps.place(x=500,y=260)

    my_Google = Button(screen_main,border="0",background="black",foreground="cyan", text="google", command=google,font="LUCIDA 15 bold")
    my_Google.place(x=470,y=300)

    my_vedantu = Button(screen_main,border="0",background="black",foreground="cyan", text="Vedantu", command=Vedantu,font="LUCIDA 15 bold")
    my_vedantu.place(x=440,y=340)

    my_Hobby = Button(screen_main,border="0",background="black",foreground="cyan", text="Hobby master", command=YT_Channel,font="LUCIDA 10 bold")
    my_Hobby.place(x=430,y=380)

    my_YT_Studio = Button(screen_main,border="0",background="black",foreground="cyan", font="LUCIDA 13 bold",text='Yt-studio', 
        command=Yt_studio)
    my_YT_Studio.place(x=440,y=407)

    my_Advertise = Button(screen_main,border="0",background="black",foreground="cyan", font="LUCIDA 14 bold",text='Visit: youtube.com/hobbymaster_real', 
        command=advertise)
    my_Advertise.place(x=1060,y=45)




    def Face_detector():
        


        recognizer = cv2.face.LBPHFaceRecognizer_create() # Local Binary Patterns Histograms
        recognizer.read('D:\\3D Objects\\python Projects\\Face-Recognition-main\\Face-Recognition-main\\trainer\\trainer.yml')   #load trained model
        cascadePath = "haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(cascadePath) #initializing haar cascade for object detection approach

        font = cv2.FONT_HERSHEY_SIMPLEX #denotes the font type


        id = 2 #number of persons you want to Recognize


        names = ['','Adnan']  #names, leave first empty bcz counter starts from 0


        cam = cv2.VideoCapture(0, cv2.CAP_DSHOW) #cv2.CAP_DSHOW to remove warning
        cam.set(3, 640) # set video FrameWidht
        cam.set(4, 480) # set video FrameHeight

        # Define min window size to be recognized as a face
        minW = 0.1*cam.get(3)
        minH = 0.1*cam.get(4)

        # flag = True

        while True:

            ret, img =cam.read() #read the frames using the above created object

            converted_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #The function converts an input image from one color space to another

            faces = faceCascade.detectMultiScale( 
                converted_image,
                scaleFactor = 1.2,
                minNeighbors = 5,
                minSize = (int(minW), int(minH)),
            )

            for(x,y,w,h) in faces:

                cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2) #used to draw a rectangle on any image

                id, accuracy = recognizer.predict(converted_image[y:y+h,x:x+w]) #to predict on every single image

                # Check if accuracy is less them 100 ==> "0" is perfect match 
                if (accuracy < 100):
                    id = names[id]
                    accuracy = "  {0}%".format(round(100 - accuracy))
                    guide_run()
                    button = Button(screen_main,background="black",foreground="Magenta", font=('space age',35),text='Initiate system', command=run)
                    button.place(x=950,y=780)

                else:
                    id = "unknown"
                    accuracy = "  {0}%".format(round(100 - accuracy))
                    speak("verification unvalid")
                    button2 = Button(screen_main,background="black",foreground="Magenta", font=('space age',35),text='Exit system', command=run)
                    button2.place(x=950,y=780)
                
                cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
                cv2.putText(img, str(accuracy), (x+5,y+h-5), font, 1, (255,255,0), 1)  
            
            cv2.imshow('camera',img) 

            k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
            if k == 27:
                break

        # Do a bit of cleanup
        cam.release()
        cv2.destroyAllWindows()

    Face_detector()
    terminal = Text(screen_main)
    terminal.configure(background="Black",foreground="white")
    terminal.configure(width=60,height=30)
    terminal.configure(font=('arial',10))
    terminal.place(x=5,y=100)


    

    old_stdout = sys.stdout    
    sys.stdout = Redirect(terminal)

        
    img = "D:\\3D Objects\\python Projects\\Face-Recognition-main\\Project JARVIS Advanced\\start button.png"
    click_btn= PhotoImage(file=img)
    img_label= Label(image=click_btn)

    

    old_stdout = sys.stdout    
    sys.stdout = Redirect(terminal)



    screen_main.mainloop()
    sys.stdout = old_stdout





main_tkinter_gui()



