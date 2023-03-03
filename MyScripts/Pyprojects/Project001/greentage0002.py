import speach_recorgnition as talk
import pyttsx3 as p3
from salenium import webdriver

r1 = talk.recorgizer()
engine = p3.init()
engine.say("Hae")
engine.runAndWait()
with talk.Microphone() as source:
	r1.adjust_for_ambient_noice(source)
	print("Hae")
	audio = r1.listen(source)
	try:
		text = r1.recorgnize_google(audio)
		print(text)
	except talk.UnknownValueError:
		print("unknown value")
	except talk.RequestError as err:
		print("request error")

		