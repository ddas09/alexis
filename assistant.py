import random
import webbrowser 
import pyperclip  
import subprocess
from datetime import date, datetime
from engine import VoiceEngine


def queryEquals(voice_data, queries):
    for query in queries:
        if query == voice_data:
            return True        


def queryExists(voice_data, queries):
    for query in queries:
        if query in voice_data:
            return True


def validateQueryAndRespond(user, voice_data, voice_engine):
    # 1: greeting
    if queryEquals(voice_data, ["hey", "hi", "hello", "hi alexis", "hello alexis", "hey alexis"]): 
        greetings = [
            f"I'm listening {user.name}.", 
            f"Hey {user.name}, how can I help you?", 
            f"Hello {user.name}."
        ]

        greet = greetings[random.randint(0,len(greetings)-1)]
        return greet

    # 2: name
    elif queryExists(voice_data, ["what is your name", "what's your name", "tell me your name"]):
        return "My name is Alexis. What's your name?"

    elif queryExists(voice_data, ["my name is"]):
        user_name = voice_data.split("is")[-1].strip()
        user.setName(user_name) 
        return f"Okay, I will remember that {user_name}."

    elif queryExists(voice_data, ["your name should be"]):
        asis_name = voice_data.split("be")[-1].strip()
        return f"Thanks, I loved the name {asis_name}."

    # 3: greeting
    elif queryExists(voice_data, ["how are you", "how are you doing", "what's up"]):
        return f"I'm very well, thanks for asking {user.name}."

    # 4: date
    elif queryExists(voice_data, ["what's today's date", "what's the date", "tell me the date"]):
        current_date = date.today().strftime("%B %d of %Y")
        return f"Today is {current_date}."

    # 5: time
    elif queryExists(voice_data, ["what's the time", "tell me the time", "what time is it"]):
        time = datetime.today().strftime("%H:%M %p")
        return f"It's {time}."

    # 6: search google
    elif queryExists(voice_data, ["search google for"]):
        search_term = voice_data.split("for")[-1].strip()
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        return f"Here is what I found for {search_term} on google."

    # 7: search youtube
    elif queryExists(voice_data, ["search youtube for"]):
        search_term = voice_data.split("for")[-1].strip()
        url = "https://www.youtube.com/results?search_query=" + search_term
        webbrowser.get().open(url)
        return f"Here is what I found for {search_term} on youtube."

    # 8: open any website
    elif (voice_data[0:4] == "open"):
        search_term = voice_data.split("open ")[-1]
        if (search_term != ""):
            url = f"https://{search_term}.com"
            webbrowser.get().open(url) 
            return f"Opening {search_term}."

    # 9: ask any question
    elif queryExists(voice_data, ["what", "what's", "why", "when", "how", "who"]):
        url = f"https://google.com/search?q=" + voice_data
        webbrowser.get().open(url)
        return "Here is what I found on google."

    # 10: stone paper scisorrs
    elif queryExists(voice_data, ["game"]):
        voice_engine.speak("choose among rock paper and scissor")
        voice_data = voice_engine.recogniseUserVoice()
        moves = ["rock", "paper", "scissor"]
        computer_move = random.choice(moves)
        player_move = voice_data

        if voice_data != "NULL":
            voice_engine.speak("The computer chose " + computer_move)
            voice_engine.speak("You chose " + player_move)

            if player_move == computer_move:
                return "So the match is draw."

            elif player_move == "rock" and computer_move == "scissor":
                return "So Player wins."

            elif player_move == "rock" and computer_move == "paper":
                return "So Computer wins."

            elif player_move == "paper" and computer_move == "rock":
                return "So Player wins."

            elif player_move == "paper" and computer_move == "scissor":
                return "So Computer wins."

            elif player_move == "scissor" and computer_move == "paper":
                return "So Player wins."

            elif player_move == "scissor" and computer_move == "rock":
                return "So Computer wins."

            else:
                return "Invalid move."

    # 11: toss a coin
    elif queryExists(voice_data, ["toss", "flip"]):
        moves = ["head", "tails"]   
        computer_move = random.choice(moves)
        return f"The computer chose " + cmove

    # 12: make a note in notepad
    elif queryExists(voice_data, ["make a note", "remember this", "write this down"]): 
        voice_engine.speak("what would you like me to note down?")
        note_text = voice_engine.recogniseUserVoice()

        if (voice_data != "NULL"):
            current_date = datetime.now()
            file_name = str(current_date).replace(":", "-") + "-note.txt" 
            f = open(file_name, "w+")
            f.write(note_text)
            subprocess.Popen(["notepad.exe", file_name])
            f.close
            return "I have made a note of that."

    # 13: read highlighted text
    elif queryExists(voice_data, ["read selected text", "read highlighted text"]):
        pyperclip.copy
        read_text = str(pyperclip.paste())
        return read_text

    # 14: price of any item
    elif queryExists(voice_data, ["price of"]):
        url = "https://google.com/search?q=" + voice_data
        webbrowser.get().open(url)
        return("Here is what I found for " + voice_data + " on google")

    # 15: weather of any city
    elif queryExists(voice_data, ["weather of"]):
        url = "https://google.com/search?q=" + voice_data
        webbrowser.get().open(url)
        return("Here is what I found for " + voice_data + " on google")

    # 16: definition 
    elif queryExists(voice_data, ["definition of", "define"]): 
        if "definition of" in voice_data:
            def_term = voice_data.split("of")[-1].strip()

        else:    
            def_term = voice_data.split("define")[-1].strip()

        url = "https://google.com/search?q=definition of " + def_term
        webbrowser.get().open(url)
        return f"Here is what I found for definition of {def_term} on google."

    # 17: shopping
    elif queryExists(voice_data, ["shop", "buy"]):
            if queryExists(voice_data, ["vegetable", "grocery", "fruit"]):
                voice_engine.speak("what do you want to buy?")
                shop_item = voice_engine.recogniseUserVoice()
                url = "https://bigbasket.com/ps/?q=" + shop_item
                webbrowser.get().open(url)
                return "showing results for " + shop_item

            elif "medicine" in voice_data:
                voice_engine.speak("what's the name of the medicine?")
                shop_item = voice_engine.recogniseUserVoice()
                url = "https://www.netmeds.com/catalogsearch/result?q=" + shop_item  
                webbrowser.get().open(url)
                return "showing results for " + shop_item

            else:
                if "shop" in voice_data:
                    shop_item = voice_data.split("shop")[-1].strip()

                else:
                    shop_item = voice_data.split("buy")[-1].strip()  

                url = "https://amazon.in/s?k=" + shop_item
                webbrowser.get().open(url)
                return "showing results for" + shop_item
    
    # end  
    elif queryEquals(voice_data, ["exit", "quit", "goodbye", "bye", "stop"]): 
        voice_engine.speak(f"Bye {user.name}. Have a nice day!")
        exit()

    # invalid command
    else:
        return "I dont know what to do. Try saying something else."


class User:
    def __init__(self):
        self.name = "User"

    def setName(self, name):
        if (name != ""):
            self.name = name 


if __name__ == "__main__":
    # create the objects for user and speech engine
    user = User()
    engine = VoiceEngine()
    engine.speak("Hi, how can I help you?")
    engine.speak("Say exit, quit or stop to terminate the program.")
    engine.speak("Say something to continue.")

    while(True):
        voice_data = engine.recogniseUserVoice() 
        if not voice_data:
            exit()

        elif voice_data != "NULL":
            print("User: " + voice_data)
            response = validateQueryAndRespond(user, voice_data, engine) 
            engine.speak(response)
    
    
        




