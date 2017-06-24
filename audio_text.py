#!/usr/bin/env python2 2.X.X
#Steven Yoo 06-23-2017

import speech_recognition as sr
import requests
# obtain path to "english.wav" in the same folder as this script
from os import path
from api_keys import BING_KEY
from api_keys import SPELL_KEY
requestSpeech = requests.get('https://api.cognitive.microsoft.com/sts/v1.0/issueToken') #SPEECH
#requestSpell = requests.get('https://api.cognitive.microsoft.com/bing/v5.0/spellcheck') # SPELL

AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "example.wav")
# AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "french.aiff")
# AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "chinese.flac")

# use the audio file as the audio source
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)  # read the entire audio file

# recognize speech using Microsoft Bing Voice Recognition

try:
    print("Microsoft Bing Voice Recognition thinks you said " + r.recognize_bing(audio, key=BING_KEY))
except sr.UnknownValueError:
    print("Microsoft Bing Voice Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))

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