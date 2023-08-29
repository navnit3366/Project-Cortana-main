"""
Author: @skywalkerSam
Aim: First release of Cortana
Date: 12022.07.19.03:21:00
"""

import pyttsx3 as pt
import speech_recognition as sr
from pyfiglet import figlet_format
import datetime as dt
import os
import webbrowser as wb

name = 'Sam Skywalker'
username = 'starboy'
ai_name = 'Stargirl'
default_ai = "Cortana"


def process_command():
    while True:
        try:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("\nSay Something...")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            print("Recognizing Now...\n")
            command = r.recognize_google(audio, language="en-US")
            print("You Said: " + command + "\n\n")
            break
        except KeyboardInterrupt:
            print("\n\nCancelling Tasks...\n")
            break
        except sr.UnknownValueError:
            print("Sorry, Please say that again...\n")
            continue
        except sr.RequestError as e:
            print(
                f"Could not request results from Google Speech Recognition service; {0}".format(e))
            break
    return command


def speak(words="Hello World"):
    engine = pt.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.getProperty('rate')
    engine.setProperty('rate', 210)
    engine.say(words)
    engine.runAndWait()


def introduction():
    title = figlet_format("Cortana  AI", "doom")
    print(title)
    return title


def greeting(user="User"):
    dt.datetime.now()
    time_hour = int(dt.datetime.now().hour)

    if 0 < time_hour < 12:
        print(f"Hello {user}, Good Morning :)\n")
    elif 12 < time_hour < 16:
        print(f"Hello {user}, Good Afternoon :)\n")
    else:
        print(f"Hello {user}, Good Evening :)\n")


attempt = 1
if __name__ == '__main__':
    try:
        introduction()
        greeting('Starboy')  # Change the name of the user here
        speak("I'm here...")

        while attempt <= 5:
            command = process_command().lower()
            attempt = attempt + 1

            # Basic Assistant Commands...
            if 'exit' in command:
                print("Exiting Interface...")
                speak('Alright')
                break

            elif "quit" in command:
                print("Okay :) \n")
                speak("Okay")
                break

            elif "done" in command:
                print("Alright ;) \n")
                speak("Alright")
                break

            elif "the date" in command:
                current_date = str(dt.date.today())
                print(f"Today is; {current_date} \n")
                speak(f"Today is, {current_date}")

            elif 'the time' in command:
                time = dt.datetime.now().strftime("%H:%M:%S")
                print(f"Current Time: {time}")
                speak(f"The time is {time}")

            elif "who are you" in command:
                print(
                    f"Hello, I'm {ai_name} & I'm here to help you... \n")
                speak(
                    f"Hello, I am {ai_name}, and I am here to help you")

            elif "tell me about yourself" in command:
                print(
                    f"Hey, I'm {default_ai} & I'm here to help... \n")
                speak(
                    f"Hey, I am {default_ai}, and I am here to help")

            elif "hello cortana" in command:
                print(
                    f"Hello {name}. How may I help you? \n")
                speak(f"Hello {name}. How may I help you?")

            elif "you need to improve" in command:
                print("Sorry for the inconvenience :( \n")
                speak("Sure")
                break

            elif "good morning" in command:
                print(f"Good morning {name}, have a nice day :) \n")
                speak(f"Good morning {name}, have a nice day")

            elif "good afternoon" in command:
                print(
                    f"Good afternoon {name}, hope you doing good :) \n")
                speak(f"Good afternoon {name}, hope you doing good")

            elif "good evening" in command:
                print(
                    f"Good evening {name}, It's time to get refreshed :) \n")
                speak(
                    f"Good evening {name}, It's time to get refreshed")

            elif "good night" in command:
                print(f"Good Night {name}, Have a nice dream :) \n")
                speak(f"Good Night {name}, Have a nice dream")
                break

            # Windows System Based Commands...
            elif 'open explorer' in command:
                os.system("explorer")
                print("Opening Explorer...")
                speak("Opening Explorer...")
                break

            elif "open file explorer" in command:
                os.system("explorer")
                print("Opening File Explorer...")
                speak("Opening File Explorer...")
                break

            elif "open files" in command:
                os.system("explorer")
                print("Opening Files...")
                speak("Opening File Explorer...")
                break

            elif "open terminal" in command:
                print("Opening PowerShell Terminal...")
                speak("Opening PowerShell Terminal...")
                os.system("powershell")
                break

            elif "open windows terminal" in command:
                print("Opening PowerShell In Windows Terminal...")
                speak("Opening PowerShell In Windows Terminal...")
                os.system("powershell")
                break

            elif "open powershell" in command:
                print("Opening PowerShell Terminal...")
                speak("Opening PowerShell Terminal...")
                os.system("powershell")
                break

            elif 'reboot the system' in command:
                print('Rebooting The System In Less Than A Minute...')
                speak('Rebooting The System In Less Than A Minute...')
                os.system('shutdown /r')
                speak('Looking forward to help you...')
                break

            elif "stop reboot" in command:
                print('Stopping System From Reboot...')
                speak('Stopping System From Reboot...')
                os.system('shutdown -a')
                break

            elif 'restart the system' in command:
                print('Restarting The System In Less Than A Minute...')
                speak('Restarting The System In Less Than A Minute...')
                os.system('shutdown /r')
                speak('Looking forward to help you...')
                break

            elif "stop restart" in command:
                print('Stopping System From Restart...')
                speak('Stopping System From Restart...')
                os.system('shutdown -a')
                speak("Welcome Back, I am here to help you... ")

            elif 'poweroff the system' in command:
                print('Shutting Down The System In Less Than A Minute...')
                speak(
                    'Shutting Down The System In Less Than A Minute...')
                os.system('shutdown -s')
                speak('Looking forward to help you!')
                break

            elif 'power of the system' in command:
                print('Shutting Down The System In Less Than A Minute...')
                speak(
                    'Shutting Down The System In Less Than A Minute...')
                os.system('shutdown -s')
                speak('Looking forward to help you...')
                break

            elif "stop poweroff" in command:
                print('Stopping System From Shutdown...')
                speak('Stopping System From Shutdown...')
                os.system('shutdown -a')
                speak("Welcome Back, I am here to help you... ")
                break

            elif "stop power of" in command:
                print('Stopping System From Shutdown...')
                speak('Stopping System From Shutdown...')
                os.system('shutdown -a')
                speak("Welcome Back, I am here to help you... ")
                break

            elif 'shutdown the system' in command:
                print('Shutting Down The System In Less Than A Minute...')
                speak(
                    'Shutting Down The System In Less Than A Minute...')
                os.system('shutdown -s')
                speak('Looking forward to help you!')
                break

            elif 'shut down the system' in command:
                print('Shutting Down The System In Less Than A Minute...')
                speak(
                    'Shutting Down The System In Less Than A Minute...')
                os.system('shutdown -s')
                speak('Looking forward to help you...')
                break

            elif "stop shutdown" in command:
                print('Stopping System From Shutdown...')
                speak('Stopping System From Shutdown...')
                os.system('shutdown -a')
                speak("Welcome Back, I am here to help you... ")
                break

            elif "stop shut down" in command:
                print('Stopping System From Shutdown...')
                speak('Stopping System From Shutdown...')
                os.system('shutdown -a')
                speak("Welcome Back, I am here to help you... ")
                break

            elif "open control panel" in command:
                os.system("control")
                print("Opening Control Panel...")
                speak("Opening Control Panel...")
                break

            elif "open bash shell" in command:
                print("Opening Bash Shell (Linux Terminal, WSL)...")
                speak("Opening Bash Shell...")
                os.system("bash")
                break

            elif "open bash terminal" in command:
                print("Opening Bash Shell (Linux Terminal, WSL)...")
                speak("Opening Bash Shell...")
                os.system("bash")
                break

            elif "open ubuntu" in command:
                print("Opening Ubuntu (Linux Terminal, WSL/WSL2)...")
                speak("Opening Ubuntu...")
                os.system("ubuntu")
                break

            elif "open python" in command:
                print("Opening Python Shell...")
                speak("Opening Python Shell...")
                os.system("python")
                exit()

            elif 'open code' in command:
                os.system("code")
                print('Opening Visual Studio Code...')
                speak('Opening Visual Studio Code...')
                break

            elif 'open code editor' in command:
                os.system("code")
                print('Opening Visual Studio Code...')
                speak('Opening Visual Studio Code...')
                break

            elif "open docker desktop" in command:
                docker_desktop_path = "C:\\Program Files\\Docker\\Docker\\Docker Desktop.exe"
                os.startfile(docker_desktop_path)
                print("Opening Docker Desktop...")
                speak("Opening Docker Desktop...")
                break

            elif "open virtualbox" in command:
                virtualbox_path = "C:\\Program Files\\Oracle\\VirtualBox\\VirtualBox.exe"
                os.startfile(virtualbox_path)
                print("Opening Virtualbox...")
                speak("Opening Virtualbox...")
                break

            elif 'open firefox' in command:
                firefox_path = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
                os.startfile(firefox_path)
                print('Opening Firefox Browser...')
                speak('Opening Firefox...')
                break

            elif "open chrome" in command:
                chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                os.startfile(chrome_path)
                print("Opening Chrome Browser...")
                speak("Opening Chrome...")
                break

            elif "open microsoft browser" in command:
                microsoft_browser_path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
                os.startfile(microsoft_browser_path)
                print('Opening Microsoft Edge Browser...')
                speak("Opening Microsoft Edge...")
                break

            elif "open microsoft edge browser" in command:
                microsoft_browser_path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
                os.startfile(microsoft_browser_path)
                print('Opening Microsoft Edge Browser...')
                speak("Opening Microsoft Edge...")
                break

            elif "open microsoft edge" in command:
                microsoft_browser_path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
                os.startfile(microsoft_browser_path)
                print('Opening Microsoft Edge Browser...')
                speak("Opening Microsoft Edge...")
                break

            elif "open windows browser" in command:
                microsoft_browser_path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
                os.startfile(microsoft_browser_path)
                print('Opening Microsoft Edge Browser...')
                speak("Opening Microsoft Edge...")
                break

            elif "open epic games launcher" in command:
                epic_games_launcher = "C:\\Program Files (x86)\\Epic Games\\Launcher\\Portal\\Binaries\\Win64\\EpicGamesLauncher.exe"
                os.startfile(epic_games_launcher)
                print("Opening Epic Games Launcher...")
                speak("Opening Epic Games Launcher...")
                break

            elif "open fortnite" in command:
                epic_games_launcher = "C:\\Program Files (x86)\\Epic Games\\Launcher\\Portal\\Binaries\\Win64\\EpicGamesLauncher.exe"
                os.startfile(epic_games_launcher)
                print("Opening Epic Games Launcher...")
                speak("Opening Epic Games Launcher...")
                break

            elif "open fortnite game" in command:
                epic_games_launcher = "C:\\Program Files (x86)\\Epic Games\\Launcher\\Portal\\Binaries\\Win64\\EpicGamesLauncher.exe"
                os.startfile(epic_games_launcher)
                print("Opening Epic Games Launcher...")
                speak("Opening Epic Games Launcher...")
                break

            elif "i wanna play fortnite" in command:
                epic_games_launcher = "C:\\Program Files (x86)\\Epic Games\\Launcher\\Portal\\Binaries\\Win64\\EpicGamesLauncher.exe"
                os.startfile(epic_games_launcher)
                print("Opening Epic Games Launcher...")
                speak("Opening Epic Games Launcher...")
                break

            elif "i want to play fortnite" in command:
                epic_games_launcher = "C:\\Program Files (x86)\\Epic Games\\Launcher\\Portal\\Binaries\\Win64\\EpicGamesLauncher.exe"
                os.startfile(epic_games_launcher)
                print("Opening Epic Games Launcher...")
                speak("Opening Epic Games Launcher...")
                break

            elif "i want to play fortnite game" in command:
                epic_games_launcher = "C:\\Program Files (x86)\\Epic Games\\Launcher\\Portal\\Binaries\\Win64\\EpicGamesLauncher.exe"
                os.startfile(epic_games_launcher)
                print("Opening Epic Games Launcher...")
                speak("Opening Epic Games Launcher...")
                break

            elif "open unreal engine" in command:
                epic_games_launcher = "C:\\Program Files (x86)\\Epic Games\\Launcher\\Portal\\Binaries\\Win64\\EpicGamesLauncher.exe"
                os.startfile(epic_games_launcher)
                print("Opening Epic Games Launcher...")
                speak("Opening Epic Games Launcher...")
                break

            elif "open steam play" in command:
                steam_play = "C:\\Program Files (x86)\\Steam\\steam.exe"
                os.startfile(steam_play)
                print("Opening Steam Play...")
                speak("Opening Steam Play...")
                break

            elif "open steam" in command:
                steam_play = "C:\\Program Files (x86)\\Steam\\steam.exe"
                os.startfile(steam_play)
                print("Opening Steam Play...")
                speak("Opening Steam Play...")
                break

            elif "i wanna play halo infinite" in command:
                steam_play = "C:\\Program Files (x86)\\Steam\\steam.exe"
                os.startfile(steam_play)
                print("Opening Steam Play...")
                speak("Opening Steam Play...")
                break

            elif "i want to play halo infinite" in command:
                steam_play = "C:\\Program Files (x86)\\Steam\\steam.exe"
                os.startfile(steam_play)
                print("Opening Steam Play...")
                speak("Opening Steam Play...")
                break

            # Web Browser Commands...
            elif 'open google.com' in command:
                wb.open('https://www.google.com/')
                print('Opening Google.com...')
                speak('Opening Google.com...')
                break

            elif "open duckduckgo" in command:
                wb.open("https://duckduckgo.com/")
                print("Opening DuckDuckGo.com...")
                speak("Opening DuckDuckGo.com...")
                break

            elif "open wikipedia" in command:
                wb.open("https://www.wikipedia.org/")
                print("Opening Wikipedia.org...")
                speak("Opening Wikipedia...")
                break

            elif "open gmail" in command:
                wb.open("https://www.gmail.com/")
                print("Opening Google Mail...")
                speak("Opening Google Mail...")
                break

            elif "open google mail" in command:
                wb.open("https://www.gmail.com/")
                print("Opening Google Mail...")
                speak("Opening Google Mail...")
                break

            elif 'open youtube' in command:
                wb.open('https://www.youtube.com/')
                print("Opening Youtube...")
                speak("Opening Youtube...")
                break

            elif 'open udemy' in command:
                wb.open('https://www.udemy.com/')
                print('Opening Udemy.com...')
                speak('Opening Udemy...')
                break

            elif "open code browser" in command:
                wb.open("https://replit.com/")
                print("Opening Replit.com...")
                speak("Opening Replit.com...")
                break

            elif "open stack overflow" in command:
                wb.open("https://stackoverflow.com/")
                print("Opening StackOverFlow.com...")
                speak("Opening StackOverFlow...")
                break

            elif "open stackoverflow" in command:
                wb.open("https://stackoverflow.com/")
                print("Opening StackOverFlow.com...")
                speak("Opening StackOverFlow.com...")
                break

            elif 'open github' in command:
                wb.open('https://github.com/')
                print('Opening Github.com...')
                speak('Opening Github...')
                break

            elif "open git lab" in command:
                wb.open("https://gitlab.com/")
                print("Opening GitLab.com...")
                speak("Opening GitLab...")
                break

            elif "open apple.com" in command:
                wb.open("https://www.apple.com/")
                print("Opening Apple.com...")
                speak("Opening Apple.com...")
                break

            elif 'open amazon.in' in command:
                wb.open('https://www.amazon.in/')
                print('Opening Amazon.in...')
                speak('Opening Amazon.in...')
                break

            elif 'open amazon.com' in command:
                wb.open('https://www.amazon.com/')
                print('Opening Amazon.com...')
                speak('Opening Amazon.com...')
                break

            elif "open flipkart" in command:
                wb.open("https://www.flipkart.com/")
                print("Opening Flipkart.com...")
                speak("Opening Flipkart.com...")
                break

            elif "open twitter" in command:
                wb.open("https://twitter.com/")
                print("Opening Twitter.com...")
                speak("Opening Twitter.com...")
                break

            elif "open instagaram" in command:
                wb.open("https://www.instagram.com/")
                print("Opening Instagram.com...")
                speak("Opening Instagram.com...")
                break

            elif "open facebook" in command:
                wb.open("https://www.facebook.com/")
                print("Opening Facebook.com...")
                speak("Opening Facebook.com...")
                break

            elif "open discord" in command:
                wb.open("https://discord.com/")
                print("Opening Discord.com...")
                speak("Opening Discord.com...")
                break

            elif "open reddit" in command:
                wb.open("https://www.reddit.com/")
                print("Opening Reddit.com")
                speak("Opening Reddit.com")
                break

            elif "open space x.com" in command:
                wb.open("https://www.spacex.com/")
                print("Opening SpaceX.com...")
                speak("Opening SpaceX.com...")
                break

            elif "open unreal engine dotkom" in command:
                wb.open("https://www.unrealengine.com/")
                print("Opening Unreal Engine.com...")
                speak("Opening Unreal Engine.com...")
                break

            elif "open unreal engine dotcom" in command:
                wb.open("https://www.unrealengine.com/")
                print("Opening Unreal Engine.com...")
                speak("Opening Unreal Engine.com...")
                break

            elif "open unreal engine learning" in command:
                wb.open("https://learn.unrealengine.com/")
                print("Opening Learn.UnrealEngine.com...")
                speak("Opening Learn.UnrealEngine.com...")
                break

            elif "open epic developer community" in command:
                wb.open("https://dev.epicgames.com/community/")
                print("Opening Dev.EpicGames.com/community...")
                speak("Opening Dev.EpicGames.com/community...")
                break

            elif "open metahuman creator" in command:
                wb.open("https://metahuman.unrealengine.com/")
                print("Opening Metahuman Creator...")
                speak("Opening Metahuman Creator...")
                break

            elif "open m h c" in command:
                wb.open("https://metahuman.unrealengine.com/")
                print("Opening Metahuman Creator...")
                speak("Opening Metahuman Creator...")
                break

            elif "open spotify on web" in command:
                wb.open("https://open.spotify.com/")
                print("Opening Spotify on Web, Enjoy listening...")
                speak("Opening Spotify on Web, Enjoy listening...")
                break

            elif "open spotify on the web" in command:
                wb.open("https://open.spotify.com/")
                print("Opening Spotify on Web, Enjoy listening...")
                speak("Opening Spotify on Web, Enjoy listening...")
                break

            else:
                print("Say that again please...\n")
                speak("Say that again")

    except KeyboardInterrupt:
        print("\n\nCancelling Tasks...\n")

    except UnboundLocalError:
        print("\n\nCancelling Tasks...\n")
