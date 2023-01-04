import sys
import threading
import tkinter as tk

import speech_recognition
from neuralintents import GenericAssistant

class Assistant():
    def __init__(self):
        self.recognizer = speech_recognition.Recognizer()
        
        self.assistant = GenericAssistant("C:\\Users\\Zacha\\Python\\chat\\intents.json") #, intent_methods={"tag_name" : self.function_name})
        self.assistant.train_model()

        self.root = tk.Tk()
        #self.label = tk.Label(text="R", font=("Arial", 120, "bold"))
        #self.label.pack()

        threading.Thread(target=self.run_assistant).start()

        self.root.mainloop()

    def run_assistant(self):
        done = False
        while not done:
            try:
                with speech_recognition.Microphone() as mic:
                    #self.recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                    #audio = self.recognizer.listen(mic)
                    
                    #text = self.recognizer.recognize_google(audio)
                    text = input("Enter a text: ")
                    text = text.lower()

                    if "hey bot" in text:
                        #self.label.config(fg="red")
                        #audio = self.recognizer.listen(mic)
                        #text = self.recognizer.recognize_google(audio)
                        text = input("Enter a text: ")
                        text = text.lower()

                        if text == "stop":
                            print("bye")
                            self.root.destroy()
                            done = True
                            sys.exit()
                        else:
                            if text is not None:
                                response = self.assistant.request(text)
                                if response is not None:
                                    #self.label.config(fg="blue")
                                    print(response)
                                    #self.speaker.say(response)
                                    #self.speaker.runAndWait()
                            #self.label.config(fg="black")
            except:
                #self.label.config(fg="black")
                continue

if __name__ == "__main__":
    Assistant()
    exit()