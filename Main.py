# ALL PROGRAM INCLOSED IN TRY-EXCEPT BLOCK FOR ANY UNKNOWN ERROR HANDEALING
try:
    from Conditions import Jarvis_Conditions # IMPORT ALL THE SUTAIBLE CONDITIONS.
    from Features import JarvisAssistant # IMPORT THE JARVIS CLASS WHICH HAVE ALL FEATURES.

    j = JarvisAssistant() # MAKING A OBJECT OF THE CLASS.

    def start_up(permision:bool):
        """Simple Startup things it can do.
        
        Parameter
        =========
        ``permision`` = The permision to startup it is can be ``True`` or ``False``.
        
        Return
        ======
        It has no returns."""
        # IF FACE RECOGNIZED IT CONTINUE THE PROGRAM EITHER IT WARNS YOU.
        if permision:
            j.speak(f'face recognized!')
            j.speak('all things are checked, i am ready for your command!')
            Jarvis_Conditions()

        else: j.speak('sorry! face is not recognized.')

except Exception as e: print(f"{e}")

if __name__ == '__main__':
    try:
        while True:
            x = j.listen()
            if x == "wake up jarvis":
                j.speak("Starting face recognition, please look at the camera!",190)
                start_up(j.faceId()) # STARTING THE FACE RECOGNITION.
            elif x == "turn off": break # TERMINATES THE PROGRAM.
            else: pass

    except Exception as e: print(f"{e}")