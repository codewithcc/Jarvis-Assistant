def Jarvis_Conditions():
    # ALL PROGRAM INCLOSED IN TRY-EXCEPT BLOCK FOR ANY UNKNOWN ERROR HANDEALING
    try:
        from Features import JarvisAssistant # IMPORT THE CLASS WHERE ALL JARVIS FEATURES ARE STORED
        from random import choice # RANDOM MODULE FOR MAKING RANDOM CHOICES
        from json import load # JSON MODULE TO WORK WITH JSON FILES
        from time import sleep # TIME MODULE TO WORK WITH TIME

        with open('Jarvis Assistant\Data.json') as j: # LOADING THE DATA FROM JSON FILE
            data = load(j)

        j = JarvisAssistant() # MAKING A OBJECT OF CLASS

        j.speak(f"hello chanchal! {j.wishMe()}. i am jarvis your personal AI assistant.",180) # WISHES AT STARTUP

        # A WHILE LOOP WHERE ALL CONDITIONS WILL BE SATISFIED AND JARVIS STARTS DOING COOL STUFFS
        while True:
            value = j.listen()

            if value == 'None': pass
            else:
                # GREETINGS OF JARVIS
                if value in data["greetings"]:
                    try:
                        responce = choice(data["greetings"][value])
                        if 'goodbye' in value:
                            j.speak(responce,190)
                            break
                        else: j.speak(responce,190)
                    
                    except: j.speak("Sorry, something is going wrong.",180)

                # OPENS ANY APP OR WEBPAGES
                elif 'open' in value or 'go to' in value or 'launch' in value:
                    try:
                        if 'open' in value: domain = value.replace('open ','')
                        else:
                            if 'go to' in value: domain = value.replace('go to ','')
                            else: domain = value.replace('launch ','')

                        if ".com" in value or ".in" in value or ".org" in value:
                            url = f"https://www.{domain}"
                            j.speak(f"Opening webpage .")
                            j.launch_app(url)

                        else:
                            if domain not in data["apps"]: j.speak(f"Sorry sir , {domain} is not exist in my data.")
                            else:
                                j.speak(f"opening {domain}",180)
                                j.launch_app(domain)
                        
                    except: j.speak("Sorry, something is going wrong.",180)

                # TELLING RANDOM JOKES
                elif 'joke' in value:
                    try:
                        j.speak('This one is required taste...',180)
                        j.speak(j.telling_jokes()[0],150)
                        sleep(.1)
                        j.speak(j.telling_jokes()[1],150)
                        # print(j.telling_jokes()[0])
                        # print(j.telling_jokes()[1])
                        sleep(1)
                        j.speak('wants another ?')
                        l = j.listen()
                        if 'ok' in l or 'yes' in l or 'go it' in l:
                            j.speak('Ok , here is for you...')
                            j.speak(j.telling_jokes()[0],150)
                            sleep(.2)
                            j.speak(j.telling_jokes()[1],150)
                        else: j.speak('ok')

                    except: j.speak("Sorry, something is going wrong.",180)

                # SENDING EMAIL
                elif 'email' in value or 'mail' in value:
                    try:
                        j.speak("whome you want to send ?")
                        n = j.listen()
                        if n not in data["email_id"]: j.speak(f"sorry, {n}'s email id not find in my data or not saved yet.",170)
                        else:
                            j.speak('What should you want to send ?')
                            t = j.listen()
                            j.speak(f"Ok sending email to {n}....")
                            x = j.email(data["email_id"][n],"From Jarvis...",t)
                            if x == True: j.speak("Email has been sent succesfully !")
                            else: j.speak('Sorry sir , email sending failed !')

                    except: j.speak("Sorry, something is going wrong.",180)

                # TELLING TIME
                elif 'time' in value:
                    try:
                        j.speak(f"it's {j.time_now()}.")

                    except: j.speak("Sorry, something is going wrong.",180)

                # TELLING DATE
                elif 'date' in value:
                    try:
                        j.speak(f"it's {j.day_now()}, {j.date_now()}.")

                    except: j.speak("Sorry, something is going wrong.",180)

                # WIKIPEDIA SEARCH
                elif 'what is' in value:
                    try:
                        j.speak(f"according to wikipedia, {j.about_spc(value)}",170)

                    except: j.speak("Sorry, something is going wrong.",180)

                # SEARCH ANYTHING ON GOOGLE
                elif 'search' and 'google' in value:
                    try:
                        x = value.replace('search ','')
                        x = x.replace('on google','')
                        j.speak('Searching...')
                        j.search_google(x)

                    except: j.speak("Sorry, something is going wrong.",180)

                # SEARCH ANYTHING ON YOUTUBE
                elif 'search' and 'youtube' in value:
                    try:
                        j.speak('sir are you want to play the 1st video ?')
                        a = j.listen()
                        x = value.replace('search ','')
                        x = x.replace('on youtube','')
                        j.speak('ok. Searching...')
                        if a == 'yes': j.search_youtube(x,True)
                        else: j.search_youtube(x)

                    except: j.speak("Sorry, something is going wrong.",180)

                # SENDING A WHATSAPP MESSAGE
                elif 'send a message' in value or 'send a whatsapp message' in value:
                    try:
                        j.speak('whom sir ?')
                        r = j.listen()
                        j.speak("and what's the message ?")
                        m = j.listen()
                        x = j.wp_msg(r,m)
                        if x == True: j.speak(f"message send succesfully to {r}.")
                        else: j.speak("sorry sir receiver name is incorrect or somenthing error.")

                    except: j.speak("Sorry, something is going wrong.",180)

                # CHANGES THE WINDOW
                elif 'change window' in value or 'switch window' in value:
                    try: j.switch_apps()

                    except: j.speak("Sorry, something is going wrong.",180)

                # TAKE A SCREENSHOT
                elif 'take a screenshot' in value or 'take screenshot' in value:
                    try:
                        j.taking_screenshot()

                    except: j.speak("Sorry, something is going wrong.",180)

                # LOCK YOUR PC
                # elif 'lock' in value or 'lock pc' in value:
                #     try:
                #         j.lock_pc()

                #     except: j.speak("Sorry, something is going wrong.",180)

                # MINIMIZE THE WINDOW
                elif 'minimise' in value or 'minimise the window' in value:
                    try:
                        j.minimize_window()

                    except: j.speak("Sorry, something is going wrong.",180)

                # MAXIMIZE THE WINDOW
                elif 'maximize' in value or 'maximize the window' in value:
                    try:
                        j.maximize_window()

                    except: j.speak("Sorry, something is going wrong.",180)

                # FLOAT THE WINDOW
                elif 'small the window' in value:
                    try:
                        j.floating_window()

                    except: j.speak("Sorry, something is going wrong.",180)

                # UNFLOAT THE WINDOW
                elif 'large the window' in value:
                    try:
                        j.unfloating_window()

                    except: j.speak("Sorry, something is going wrong.",180)

                # TELLING SYSTEM STATUS
                elif 'system status' in value:
                    try:
                        a = j.system_status()
                        j.speak(f"Currently {a[2]} percent of cpu used and {a[0][0]} {a[0][1]} RAM used in total of {a[1][0]}{a[1][1]}.",180)

                    except: j.speak("Sorry, something is going wrong.",180)

                else: pass

    except Exception as e: print(e)

if __name__ == '__main__':
    pass