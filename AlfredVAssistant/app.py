import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
from datetime import datetime


# this method is for taking the commands and recognizing the command from the
# speech_Recognition module we will use the recongizer method for recognizing
def takeCommand():

	r = sr.Recognizer()

	# from the speech_Recognition module we will use the Microphone module for listening the command
	with sr.Microphone() as source:
		print('Listening')
		
		# seconds of non-speaking audio before a phrase is considered complete
		r.pause_threshold = 0.7
		audio = r.listen(source)
		
		try:
			print("Recognizing")
			
			#setting for english
			Query = r.recognize_google(audio, language='en-in')
			print("the command is printed=", Query)
			
		except Exception as e:
			print(e)
			print("Say that again sir")
			return "None"
		
		return Query

def speak(audio):
	
	engine = pyttsx3.init()
	# getter method(gets the current value of engine property)
	voices = engine.getProperty('voices')
	
	# setter method .[0]=male voice and [1]=female voice in set Property.
	engine.setProperty('voice', voices[0].id)
	
	# Method for the speaking of the assistant
	engine.say(audio)
	
	# Blocks while processing all the currently queued commands
	engine.runAndWait()

def tellDay():
	# get current datetime
	dt = datetime.now()
	#Speak the day of the week
	speak("The day is " + dt.strftime('%A'))


def tellTime():
	time = datetime.now()
	#convert time into speakable string
	print(time)
	currentTime = str(time.today().strftime("%I:%M %p"))
	speak("Master Wayne, the time is " + currentTime)

def Hello():
	
	#triggers greeting
	speak("Hello Master Wayne. how may I help you")


def Take_query():

	#triggers a greeting from Alfred
	Hello()
	
	#Continue to loop until command to shutdown
	while(True):
		
		#Lower Case Queries work the best
		query = takeCommand().lower()

		if "tell me your name" in query:
			speak("I am Alfred. Your Virtual Assistant")

		elif "alfred i have a question" in query:
			speak("What is your question sir")
			#ask alfred your question
			query = takeCommand().lower()
			speak("Displaying the results on the bat computer Master Wayne")
			#displays the search results from your default internet browser
			webbrowser.open(f"{str(query)}")
			continue

		elif "alfred play pandora" in query:
			speak("Playing music Master Wayne")
			webbrowser.open("www.pandora.com")
			
		elif "alfred what's today" in query:
			tellDay()
			continue
		
		elif "alfred what time is it" in query:
			tellTime()
			continue
		
		# this will exit and terminate the program
		elif "alfred shut down" in query:
			speak("Goodbye Master Wayne")
			exit()

if __name__ == '__main__':
	# main method 
	Take_query()
