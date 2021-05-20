import speech_recognition as sr 
import pyttsx3  


class VoiceEngine:
    def __init__(self):
        self.recogniser = sr.Recognizer() # initialise a speech recogniser object

    def speak(self, message):
        engine = pyttsx3.init() # text to speech converter
        engine.say(message)
        print(f"Assistat: {message}")
        engine.runAndWait()

    def recogniseUserVoice(self):
        with sr.Microphone() as source: # using default system mic as source
            try:
                audio = self.recogniser.listen(source, 5, 5) # listen for the audio via source
                voice_data = self.recogniser.recognize_google(audio) # convert audio to text
                return voice_data.lower()

            except sr.WaitTimeoutError:
                #quit, no response from user
                self.speak("No response from user. Quitting Application.")
                return None

            except sr.UnknownValueError: 
                # error: recognizer does not understand
                self.speak("Sorry, I did not get that.")
                return "NULL"
        
                  
                