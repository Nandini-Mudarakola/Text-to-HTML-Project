# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 20:11:32 2021

@author: codengocool
"""

from gtts import gTTS
 
language = 'en'
with open('lyrics.txt') as f:
    lines = f.readlines()

#print(len(lines))

text=""
for x in lines:
 text+=x     
 
#print(lines)
print(text)
output = gTTS(text=text, lang=language,slow=False)
 



output.save("butter.mp3")
from pygame import mixer  # Load the popular external library

sound = mixer.Sound('Butter - BTS instrumental.wav')
sound.play()

mixer.init()
mixer.music.load('butter.mp3')
mixer.music.play(1,0.0)

##sound.stop()
f.close()
