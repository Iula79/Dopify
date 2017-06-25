#!/usr/bin/env python2 2.X.X
#Steven Yoo 06-23-2017

import speech_recognition as sr
import requests
import timeit
import logging
# obtain path to "english.wav" in the same folder as this script
from os import path
import os
from api_keys import BING_KEY
from api_keys import SPELL_KEY
from api_keys import SUBSCRIPTION_KEY
from monotonic import monotonic

#requestSpeech = requests.get('https://api.cognitive.microsoft.com/sts/v1.0', auth=("janetlaichang@gmail.com", "Ww176162036")) #SPEECH
#requestSpell = requests.get('https://api.cognitive.microsoft.com/bing/v5.0/spellcheck') # SPELL

AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "example.wav")
# AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "french.aiff")
# AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "chinese.flac")

class RequestError(Exception):
	pass

class BingSpeechAPI:
	def __init__(self): #, key=SUBSCRIPTION_KEY):
		self.key = SUBSCRIPTION_KEY
		self.access_token = None
		self.expire_time = None
		self.session = requests.Session()

	def authenticate(self):
		if self.expire_time is None or monotonic() > self.expire_time: # first credential request, or the access token from the previous one expired
			# get an access token using OAuth
			#credential_url = "https://api.cognitive.microsoft.com/sts/v1.0/issueToken"
			headers = {"Ocp-Apim-Subscription-Key": self.key}
        	start_time = monotonic()
        	response = self.session.post("https://api.cognitive.microsoft.com/sts/v1.0/issueToken", headers=headers)
        	print ("This is the response", response)

		if response.status_code != 200:
			raise RequestError("http request error with status code {}".format(response.status_code))
			self.access_token = response.content
			expiry_seconds = 590 # document mentions the access token is expired in 10 minutes
			self.expire_time = start_time + expiry_seconds

	def get_audio_file():
		# use the audio file as the audio source
		r = sr.Recognizer()
		with sr.AudioFile(AUDIO_FILE) as source:
			audio = r.record(source)  # read the entire audio file
		print ("Get audio file result", audio)

	def recognize_speech():
		# recognize speech using Microsoft Bing Voice Recognition
		try:
 			print("Microsoft Bing Voice Recognition thinks you said " + r.recognize_bing(audio, key=BING_KEY))
 		except sr.UnknownValueError:
 			print("Microsoft Bing Voice Recognition could not understand audio")
		except sr.RequestError as e:
			print("Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))

def main():
    logging.basicConfig(level=logging.DEBUG)
    bing = BingSpeechAPI()
    bing.authenticate()
    bing.get_audio_file()
    bing.recognize_speech()

if __name__ == '__main__':
	main()

# Text to Slang Transcribe


#try:
    #print("We are going to translate into Dopify language " + slang)
#except sr.UnknownValueError:
    #print("Microsoft Bing Voice Recognition could not understand audio")
#except sr.RequestError as e:
    #print("Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))

"""
import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

print(r.recognize_google(audio))
"""