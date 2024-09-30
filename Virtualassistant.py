import speech_recognition
import pyttsx3
from datetime import date
from datetime import datetime 
robot_mouth= pyttsx3.init()

robot_ear = speech_recognition.Recognizer()
robot_brain=""
while True:
	with speech_recognition.Microphone() as mic:
		print("Robot: I'm Listening")
		audio = robot_ear.listen(mic)


	try:
		you = robot_ear.recognize_google(audio)
	except:
		you =""

	print("You: "+you)

	if you == "":
		robot_brain = "I can't hear you, try again"
	elif "hello" in you:
		robot_brain="Hi"
	elif "today" in you:
		today = date.today()
		robot_brain = today.strftime("%B %d, %Y")
	elif "time" in you:
		now = datetime.now()
		robot_brain = now.strftime("%H hours %M minutes %S seconds")
	elif "president" in you:
		robot_brain="Donnal Trump"
	elif "bye" in you:
		robot_brain="bye"
		robot_mouth.say(robot_brain)
		robot_mouth.runAndWait()
		break
	else:
		robot_brain="I'm fine thanks you"

	robot_mouth.say(robot_brain)
	robot_mouth.runAndWait()