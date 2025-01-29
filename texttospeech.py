# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 02:58:20 2021

@author: hp
"""

from gtts import gTTS
import os

text="থাকবো নাকো বদ্ধ ঘরে"

language = 'bn'

output = gTTS(text=text, lang=language,slow=False)

output.save("output.mp3")
from pygame import mixer  # Load the popular external library

mixer.init()
mixer.music.load('output.mp3')
mixer.music.play()

#output.system("output.mp3")
