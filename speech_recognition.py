# -*- coding: utf-8 -*-
"""speech recognition.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gJxRgcxvTqxd2rkkZU4bXBxdVfXFoRl_
"""

!pip install speechrecognition

import speech_recognition as sr

r= sr.Recognizer()

audio = sr.AudioFile('/content/OSR_us_000_0034_8k.wav')

with audio as source:                 #source is used for audio processing in slow and  one by one correct process
  audio=r.listen(source)

text = r.recognize_google(audio)    #translating audio into text

text = text.lower()

text