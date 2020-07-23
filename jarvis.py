import pyttsx3
import datetime
import speech_recognition as SR
import wikipedia
import webbrowser
import os



engine= pyttsx3.init('sapi5') # 'sapi5 is a speach recognition API designed by Microsoft'
voices= engine.getProperty('voices') #voices is basically a list of voice available in our Computer

engine.setProperty('voice',voices[0].id) #setProperty sets the voice from the list


#speak function which takes a string as an input and reads it
def speak(audio):
	engine.say(audio)
	engine.runAndWait()

#function to make the assistant wish me according to the current time
def wish_me():
	hour=int(datetime.datetime.now().hour)
	if hour>=0 and hour<12:
		speak("Good Morning,Sir!")
	elif hour>=12 and hour<14:
		speak("Good Afternoon,Sir!")
	else :
		speak("Good Evening,Sir!")

	speak("I am Felina. Please tell me how may I help you!")

#this takeCommand() takes microphone input from the user and returns a string as an output

def takeCommand():
	r= SR.Recognizer() #funtion in SR module to help recognise the voice

	with SR.Microphone() as source:
		print("Listening....")
		r.pause_threshold=1#the time that the speech recogniser considers after which it assumes that the phrase is complete.
		r.energy_threshold=450
		r.non_speaking_duration=0
		r.phrase_threshold=0.1
		r.opertion_timeout=0.1
		audio= r.listen(source)

	try:
		print("Recognizing...")
		query= r.recognize_google(audio, language='en-in')

		#print(f"User Said:- {query}\n")

	except Exception as e:
		print(e)
		print("Say that again!")

		return "None"

	return query

	
	
running=True



if __name__ == '__main__':
	wish_me()
	

	


	#An infinite while loop to handle all the different queries from the user

	while running:
		query=takeCommand().lower() #converting the query into lowercase

		if "wikipedia" in query:    #if the query contains wikipedia then search wikipedia for the query
			speak("Searching wikipedia....")
			query=query.replace("wikipedia","")  #replacing all wikipedias with blank in the query

			try:
				results=wikipedia.summary(query,sentences=2) # this function will return 2 sentecnes from the wikipedia artcile
				speak("According to wikipedia..")
				print(results)
				speak(results) # the results are being spoken by the assistant

			except Exception as e:
				speak("No Results Found!")
				print("No Results Found")

		elif "open codeforces" in query:
			speak("Opening Codeforces in a moment...")
			webbrowser.open("codeforces.com")

		elif "open youtube" in query:
			speak("Opening Youtube in a moment...")
			webbrowser.open("youtube.com")

		elif "open google" in query:
			speak("Opening Google in a moment...")
			webbrowser.open("google.com")

		elif "open geeks for geeks" in query:
			speak("Opening GFG in a moment...")
			webbrowser.open("geeksforgeeks.org")

		elif "open stack overflow" in query:
			speak("Opening stackoverflow in a moment...")
			webbrowser.open("stackoverflow.com")
		
		elif "open sublime" in query:
			speak("Opening Sublime Text in a moment...")
			path="D:\\Sublime Text 3\\sublime_text.exe"
			os.startfile(path)

		elif "the time" in query:

			time= datetime.datetime.now().strftime("%H:%M:%S")
			speak(f"the time is {time}")

		elif "the date" in query:
			date=datetime.datetime.now().strftime("%x")
			speak(f"the date is {date}")


		elif "photoshop" in query:
			speak("Opening Photoshop in a moment...")
			path="C:\\Program Files\\Adobe\\Adobe Photoshop 2020\\photoshop.exe"
			os.startfile(path)

		elif "quit" in query:
			speak("GoodBye Sir, it has been a great time serving you")
			running=False

		elif  "how are you" in query:
			speak("I am very fine, Sir! What about you?")

		elif " love you" in query:
			speak("Mind your tounge, Sir!")

		

		else:
			speak("I couldn't understand you Sir! Please try again!")

		
		




