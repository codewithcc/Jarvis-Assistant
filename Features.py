# ALL PROGRAM INCLOSED IN TRY-EXCEPT BLOCK FOR ANY UNKNOWN ERROR HANDEALING
try:
    from Configure import EMAIL_ID,APP_PASSWORD,WEATHER_API_KEY,NEWS_API_KEY
    try:
        import json
        with open('Jarvis Assistant\Data.json') as j: # LOADING THE DATA FROM JSON FILE
            data = json.load(j)

    except Exception as e: print(f"{e}\n")

    pictures = {
        'ai' : 'C:\\Users\\USER\\OneDrive\\Pictures\\Saved Pictures\\AI 600 x 400.jpg'
    }

    class JarvisAssistant(): # MAKING OF A CLASS WHERE ALL JARVIS FEATURE PATENTS
        def __init__(self):
            pass

        def about_spc(self, sub:str):
            """Tells the Summary of a specified topic using Wikipedia.
            
            Parameter
            =========
            ``Sub`` = The topic you want to get the summary.
            
            Return
            ======
            It Returns ``Summary`` of the topic if the function runs else ``None``."""
            try:
                from wikipedia import summary
                return summary(sub, sentences = 3)
            
            except Exception as e:
                print(f'{e}\n')
                return None

        def suggetion_spc(self, sub:str):
            """Gives Suggestions of a specified topic using Wikipedia.
            
            Parameter
            =========
            ``Sub`` = The topic you want to get the summary.
            
            Return
            ======
            It Returns ``Suggestion`` of the topic if the function runs else ``None``."""
            try:
                from wikipedia import search
                from random import randint
                x = search(sub)
                leng = len(x)
                index = randint(0,leng)
                return x[index]

            except Exception as e:
                print(f'{e}\n')
                return None

        def suggetion_any(self):
            """Gives any random Suggestions using Wikipedia.
            
            Parameter
            =========
            It has no Parameter.
            
            Return
            ======
            It Returns ``Suggestion`` of the topic if the function runs else ``None``."""
            try:
                from wikipedia import random
                return random()

            except Exception as e:
                print(f'{e}\n')
                return None

        def home_lights(self, command: bool):
            """Turns ``ON`` and ``OFF`` the room lights.

            Parameter
            =========
            ``command`` = A boolean value states wheather turn on or off the light.\n
            
            Return
            ======
            Returns ``True`` if function executes else ``False``."""
            try:
                import serial

                if command == True:
                    return True

                else: return False

            except Exception as e:
                print(f'{e}\n')
                return False

        def home_fans(self, command: bool):
            """Turns ``ON`` and ``OFF`` the room fans.

            Parameter
            =========
            ``command`` = A boolean value states wheather turn on or off the fan.\n
            
            Return
            ======
            Returns ``True`` if function executes else ``False``."""
            try:
                import serial

                if command == True:
                    return True

                else: return False

            except Exception as e:
                print(f'{e}\n')
                return False

        def outdoor_lights(self, command: bool):
            """Turns ``ON`` and ``OFF`` the outdoor lights.

            Parameter
            =========
            ``command`` = A boolean value states wheather turn on or off the light.\n
            
            Return
            ======
            Returns ``True`` if function executes else ``False``."""
            try:
                import serial

                if command == True:
                    return True

                else: return False

            except Exception as e:
                print(f'{e}\n')
                return False

        def faceId(self):
            """It finds a particular face using your Webcam.
            
            Parameter
            =========
            It has no Parameter.
            
            Return
            ======
            It returns ``True`` if the face detected else ``False``."""
            try:
                from cv2 import VideoCapture,VideoWriter_fourcc,CAP_DSHOW,CAP_PROP_FPS,CAP_PROP_FOURCC
                from face_recognition import load_image_file,face_encodings,face_locations,compare_faces
                
                cam = VideoCapture(0,CAP_DSHOW)
                cam.set(CAP_PROP_FPS,30)
                cam.set(CAP_PROP_FOURCC,VideoWriter_fourcc(*'MJPG'))

                ccFace=load_image_file('Jarvis Assistant\Images\chanchal.jpg')
                ccFaceEncode=face_encodings(ccFace)[0]

                knownEncodings=[ccFaceEncode]

                ignore,frame = cam.read()
                unknownFace = frame
                faceLocations = face_locations(unknownFace)
                unknownEncodings = face_encodings(unknownFace,faceLocations)

                for faceLocation,unknownEncoding in zip(faceLocations,unknownEncodings):
                    val = False
                    matches=compare_faces(knownEncodings,unknownEncoding)

                    if True in matches:
                        val = True
                        return val
            
            except Exception as e:
                print(f'{e}\n')
                return False

        def pattern_finder(self, text:str, pattern:str, key_value:str):
            try:
                import re

                val = ''
                patt = re.compile(f'{pattern}')
                matches = patt.finditer(text)
                for match in matches:
                    val = match[0]

                if val == key_value:
                    promt = text.strip(f'{key_value} ')

                else: promt = 'None'

                return promt

            except Exception as e:
                print(f'{e}\n')
                return False

        def hotword_detection(self, text:str, key_value:str):
            try:
                import re
                
                val = False
                pattern = re.compile(f'{key_value}')
                matches = pattern.finditer(text)
                for match in matches:
                    val = match[0]
                if val in key_value: return True
                elif val not in key_value: return False
                else: return False

            except Exception as e:
                print(f'{e}\n')
                return False

        def time_now(self):
            """It gives you the real time.
            
            Parameter
            =========
            It has no parameter.
            
            Return
            ======
            It returns ``Time`` if function runs else ``None``"""
            try:
                from datetime import datetime

                hour = ''
                h = datetime.now().strftime('%I')
                if h in ['00','01','02','03','04','05','06','07','08','09']:
                    hour = h.strip('0')
                    return datetime.now().strftime(f'{hour} %M %p')
                else:
                    return datetime.now().strftime(f'{h} %M %p')

            except Exception as e:
                print(f'{e}\n')
                return None  

        def date_now(self):
            """It gives you the real date.
            
            Parameter
            =========
            It has no parameter.
            
            Return
            ======
            It returns ``Date`` if function runs else ``None``"""
            try:
                from datetime import datetime
                return datetime.now().strftime('%d %b %Y')

            except Exception as e:
                print(f'{e}\n')
                return None

        def day_now(self):
            """It gives you the real day.
            
            Parameter
            =========
            It has no parameter.
            
            Return
            ======
            It returns ``Day`` if function runs else ``None``"""
            try:
                from datetime import datetime
                return datetime.now().strftime('%A')

            except Exception as e:
                print(f'{e}\n')
                return None

        def telling_jokes(self):
            """It tells you a random joke.
            
            Parameter
            =========
            It has no parameter.
            
            Return
            ======
            It returns an ``tuple`` where the ``1st element is the Joke`` and the ``2nd element is the answer`` of the joke."""
            try:
                from requests import get
                url = 'https://v2.jokeapi.dev/joke/Any'

                send_data = get(url)
                get_data = send_data.json()

                question = get_data['setup']
                answer = get_data["delivery"]

                return question,answer

            except Exception as e:
                print(f'{e}\n')
                return None

        def launch_app(self, app_name_path:str):
            """It launches any application or webpage.
            
            Parameter
            =========
            ``app_name_path`` = The address of the webpage or the application target path.
            
            Return
            ======
            Returns ``True`` if function executes else ``False``."""
            from webbrowser import open
            from os import startfile
            
            try:
                app_paths = data["apps"]
                if app_name_path in app_paths and 'https' not in app_name_path:
                    for x in app_paths:
                        if app_name_path == x: path = app_paths[app_name_path]

                        else: pass

                    startfile(path)
                    return True

                elif '.com' in app_name_path or '.in' in app_name_path or '.org' in app_name_path:
                    open(app_name_path)
                    return True

                else: return False

            except Exception as e:
                print(f'{e}\n')
                return False

        def listen(self):
            """It listen your voice and convert it into text as string format using ``Google Speech Recognition``.
            
            Parameter
            =========
            It has no parameter.
            
            Return
            ======
            It returns the ``STT(Speech To Text)`` else ``None``"""
            from speech_recognition import Recognizer,Microphone,UnknownValueError

            r = Recognizer()
            m = Microphone()

            try:
                with m as mic: r.adjust_for_ambient_noise(mic,1.2)
                print('Listening...')
                r.pause_threshold = 1
                r.dynamic_energy_threshold = 100

                with m as mic: audio = r.listen(mic)

                try:
                    print('Recognizing...')
                    text = r.recognize_google(audio)
                    text = text.lower()
                    print(f'User: {text}\n')
                    return text

                except UnknownValueError: 
                    return 'None'
                    
            except Exception as e:
                print(f'{e}\n')
                return 'None'

        def wp_msg(self, receiver: str,message: str):
            """Instantly sends a perticular whatsapp message to a person.

            Parameters
            ==========
            ``receiver`` = The name of the message receiver person.\n
            ``message`` = The message you want to send.

            Returns
            =======
            It returns ``True`` if the message has been sent succesfuly and ``False`` if the message hasn't sent."""
            try:
                # from pywhatkit.whats import sendwhatmsg_instantly
                from webbrowser import open
                from pyautogui import size,click,press,keyDown,keyUp
                from time import sleep
                w,h = size()
                if receiver in data["contact_no"]:
                    for x in data["contact_no"]:
                        if receiver == x:
                            number = data["contact_no"][receiver]
                        else: pass
                else: return False

                open(f"https://web.whatsapp.com/send?phone={number}&text={message}")
                sleep(15)
                click(w/2,h/2)
                press('enter')
                sleep(5)
                keyDown('ctrl')
                keyDown('w')
                keyUp('w')
                keyUp('ctrl')
                return True

            except Exception as e:
                print(f'{e}\n')
                return False

        def wp_grp_msg(self, receiver: str,message: str):
            """Instantly sends a perticular whatsapp message to a group.\n

            Parameters
            ==========
            ``receiver`` = The name of the message receiver group.\n
            ``message`` = The message you want to send.

            Returns
            =======
            It returns ``True`` if the message has been sent succesfuly and ``False`` if the message hasn't sent."""
            try:
                from pywhatkit.whats import sendwhatmsg_to_group_instantly
                if receiver in data["contact_no"]:
                    for x in data["contact_no"]:
                        if receiver == x:
                            id = data["contact_no"][receiver]

                sendwhatmsg_to_group_instantly(id,message,tab_close = True,close_time = 5)
                return True

            except Exception as e:
                print(f'{e}\n')
                return False

        def wp_pic_send(self, receiver: str,picture: str,caption: str):
            """Instantly sends a perticular picture with caption to a person in whatsapp.

            Parameters
            ==========
            ``receiver`` = The name of the message receiver person.\n
            ``picture`` = The name of the picture you want to send.\n
            ``caption`` = The message you want to send along with picture as a caption.

            Returns
            =======
            It returns ``True`` if the picture has been sent succesfuly and ``False`` if the picture hasn't sent."""
            try:
                from pywhatkit.whats import sendwhats_image
                try:
                    if receiver in data["contact_no"]:
                        for x in data["contact_no"]:
                            if receiver == x:
                                name = data["contact_no"][receiver]
                                
                            else: pass

                    if picture in pictures:
                        for x in pictures:
                            if picture == x:
                                pic = pictures[picture]
                                
                            else: pass

                except Exception as e:
                    print(f'{e}\n')
                    return False
                
                sendwhats_image(name,pic,caption,tab_close = True,close_time = 5)
                return True

            except Exception as e:
                print(f'{e}\n')
                return False

        def wp_grp_pic_send(self, receiver: str,picture: str,caption: str):
            """Instantly sends a perticular picture with caption to a group in whatsapp.

            Parameters
            ==========
            ``receiver`` = The name of the message receiver group.\n
            ``picture`` = The name of the picture you want to send.\n
            ``caption`` = The message you want to send along with picture as a caption.

            Returns
            =======
            It returns ``True`` if the picture has been sent succesfuly and ``False`` if the picture hasn't sent."""
            try:
                from pywhatkit.whats import sendwhats_image
                try:
                    if receiver in data["id"]:
                        for x in data["id"]:
                            if receiver == x:
                                name = data["id"][receiver]
                                
                            else: pass

                    if picture in pictures:
                        for x in pictures:
                            if picture == x:
                                pic = pictures[picture]
                                
                            else: pass

                except Exception as e:
                    print(f'{e}\n')
                    return False
                
                sendwhats_image(name,pic,caption,tab_close = True,close_time = 5)
                return True

            except Exception as e:
                print(f'{e}\n')
                return False

        def email(self, receiver: str,subject: str,message: str):
            """Instantly sends email to any person.

            Parameters
            ==========
            ``receiver`` = The name of the email receiver person.\n
            ``subject`` = The subject of your email.\n
            ``message`` = The message you want to send through email.

            Returns
            =======
            It returns ``True`` if the email has been sent succesfuly and ``False`` if the email hasn't sent."""
            try:
                from pywhatkit.whats import send_mail

                send_mail(EMAIL_ID,APP_PASSWORD,subject,message,receiver)
                return True

            except Exception as e:
                print(f'{e}\n')
                return False

        def get_news(self):
            try:
                from requests import get
                
                news_data = []
                url = f'https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}'

                send_data = get(url)
                get_data = send_data.json()
                for i in range(0,5,1):
                    # titles = get_data['articles'][i]['title']
                    news = get_data['articles'][i]['description']
                    news_data.append(news)
                return news_data

            except Exception as e:
                print(f'{e}\n')
                return None

        def search_google(self, search_sub:str):
            try:
                from webbrowser import open
                open(f"https://www.google.com/search?q={search_sub}")
                return True

            except Exception as e:
                print(f'{e}\n')
                return False

        def search_youtube(self, search_sub:str, open_video:bool = False):
            try:
                if open_video == False:
                    from webbrowser import open
                    open(f"https://www.youtube.com/results?search_query={search_sub}")
                    return True
                else:
                    from pywhatkit.misc import playonyt
                    playonyt(search_sub)
                    return True

            except Exception as e:
                print(f'{e}\n')
                return False

        def speak(self, audio:str, voice_rate:int = 200):
            """It converts text into speech.
            
            Parameter
            =========
            ``audio`` = It takes your text.
            
            Return
            ======
            return ``True`` if function runs else ``False``."""
            try:
                from pyttsx3 import init
                engine = init('sapi5')
                voices = engine.getProperty('voices')
                engine.setProperty('voice',voices[0].id)
                engine.setProperty('rate',voice_rate)
                engine.say(audio)
                engine.runAndWait()
                return True

            except Exception as e:
                print(f'{e}\n')
                return False

        def system_status(self):
            """It tells you about your System status.
            
            Parameter
            =========
            It has no parameter.
            
            Return
            ======
            It returns ``CPU Working Percent`` , ``Used RAM`` and ``total RAM``."""
            try:
                from psutil import virtual_memory,cpu_percent,cpu_freq
                from math import floor,log,pow

                memory_in_use = virtual_memory().used
                total_memory = virtual_memory().total
                if memory_in_use == 0 or total_memory == 0:
                    return "0B"

                size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
                i_used = int(floor(log(memory_in_use, 1024)))
                i_total = int(floor(log(memory_in_use, 1024))) 
                p_used = pow(1024, i_used)
                p_total = pow(1024, i_total)

                ram_u = round(memory_in_use / p_used, 2)
                ram_t = round(total_memory / p_total, 2)

                cpu_u = str(cpu_percent())
                cpu_f = str(cpu_freq())
                return (ram_u,size_name[i_used]),(ram_t,size_name[i_total]),cpu_u,cpu_f

            except Exception as e:
                print(f'{e}\n')
                return None

        def switch_apps(self):
            """It only switchs tabs or windows.

            Parameter
            =========
            It has no Parameters.

            Return
            ======
            It return ``True`` if function executes else ``False``."""
            try:
                from pyautogui import keyDown,keyUp
                from time import sleep
                keyDown('alt')
                keyDown('tab')
                keyUp('tab')
                sleep(.5)
                keyUp('alt')
                return True

            except Exception as e:
                print(f'{e}\n')
                return False

        def taking_screenshot(self):
            """It only takes Screenshots.

            Parameter
            =========
            It has no Parameters.

            Return
            ======
            It return ``True`` if function executes else ``False``."""
            try:
                from pyautogui import keyDown,keyUp
                keyDown('win')
                keyDown('printscreen')
                keyUp('win')
                keyUp('printscreen')
                return True

            except Exception as e:
                print(f'{e}\n')
                return False

        def open_thispc(self):
            """Opens This PC.

            Parameter
            =========
            It has no Parameters.

            Return
            ======
            It return ``True`` if function executes else ``False``."""
            try:
                from pyautogui import keyDown,keyUp
                keyDown('win')
                keyDown('e')
                keyUp('e')
                keyUp('win')

            except Exception as e:
                print(f'{e}\n')
                return False

        def lock_pc(self):
            """It locks pc.

            Parameter
            =========
            It has no Parameters.

            Return
            ======
            It return ``True`` if function executes else ``False``."""
            try:
                from pyautogui import keyDown,keyUp
                keyDown('win')
                keyDown('l')
                keyUp('l')
                keyUp('win')
                return True

            except Exception as e:
                print(f'{e}\n')
                return False

        def close_program(self):
            try:
                from pyautogui import keyDown,keyUp
                keyDown('ctrl')
                keyDown('w')
                keyUp('w')
                keyUp('ctrl')
                return True

            except Exception as e:
                print(f'{e}\n')
                return False

        def minimize_window(self):
            try:
                from pyautogui import keyDown,keyUp
                keyDown('win')
                keyDown('m')
                keyUp('m')
                keyUp('win')
                return True

            except Exception as e:
                print(f'{e}\n')
                return False

        def maximize_window(self):
            try:
                from pyautogui import keyDown,keyUp
                keyDown('win')
                keyDown('shift')
                keyDown('m')
                keyUp('m')
                keyUp('shift')
                keyUp('win')
                return True

            except Exception as e:
                print(f'{e}\n')
                return False

        def floating_window(self):
            try:
                from pyautogui import keyDown,keyUp
                keyDown('win')      
                keyDown('down')
                keyUp('down')
                keyUp('win')
                return True

            except Exception as e:
                print(f'{e}\n')
                return False

        def unfloating_window(self):
            try:
                from pyautogui import keyDown,keyUp
                keyDown('win')      
                keyDown('up')
                keyUp('up')
                keyUp('win')
                return True

            except Exception as e:
                print(f'{e}\n')
                return False

        def play_pause_yt(self):
            try:
                from pyautogui import press
                press("k")
                return True

            except Exception as e:
                print(f'{e}\n')
                return False

        def full_screen_yt(self):
            try:
                from pyautogui import press
                press("f")
                return True

            except Exception as e:
                print(f'{e}\n')
                return False

        def mute_unmute_yt(self):
            try:
                from pyautogui import press
                press("m")
                return True

            except Exception as e:
                print(f'{e}\n')
                return False

        def fetch_weather(self, city:str):
            """It tells you about the weather forcast of a specified city.
            
            parameter
            =========
            ``city`` = The city name you want to fetch weather forcast.
            
            Return
            ======
            It returns the ``Tuple`` where.....\n
            ``1st element is Lontitude``\n
            ``2nd element is Lantitude``\n
            ``3rd element is Sky Status``\n
            ``4th element is Temperature``\n
            ``5th element is Air Pressure``\n
            ``6th element is Humidity``\n
            ``7th element is Wind-Speed``\n
            else it returns ``None``."""
            try:
                from requests import get

                url1 = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}'

                send_request1 = get(url1)
                get_data1 = send_request1.json()

                if get_data1['cod'] == 404:
                    return None

                else:
                    lon = get_data1['coord']['lon']
                    lat = get_data1['coord']['lat']
                    sky = get_data1['weather'][0]['description']
                    temperature = round((get_data1['main']['temp']) - 273.15)
                    pressure = get_data1['main']['pressure']
                    humidity = get_data1['main']['humidity']
                    wind = get_data1['wind']['speed']

                url2 = f'http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={WEATHER_API_KEY}'

                send_request2 = get(url2)
                get_data2 = send_request2.json()

                aqi = get_data2['list'][0]['main']['aqi']

                return lon,lat,sky,temperature,pressure,humidity,wind,aqi

            except Exception as e:
                print(f'{e}\n')
                return None

        def wishMe(self):
            """It wishes you depending on time.
            
            Parameter
            =========
            It has no parameter.
            
            Return
            ======
            It returns the ``Greeting`` if the function runs else ``None``."""
            try:
                from datetime import datetime
                hour = int(datetime.now().strftime('%H'))

                if hour>=5 and hour<12: val = 'goodmorning'

                elif hour>=12 and hour<=16: val = 'goodafternoon'

                elif hour>16 and hour<=21: val = 'goodevening'

                elif hour>21 or hour<5: val = 'goodnight'

                else: pass
                return val

            except Exception as e:
                print(f'{e}\n')
                return None

        def location(self):
            try:
                from socket import gethostname,gethostbyname
                ip = gethostbyname(gethostname())
                return ip
            
            except Exception as e:
                print(f'{e}\n')
                return None

    if __name__ == '__main__':
        pass

except Exception as e: print(f"{e}")