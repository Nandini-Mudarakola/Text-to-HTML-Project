import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
import soundfile as sf
from colorama import init, Fore, Back, Style

# Sampling frequency
freq = 44100

# Recording duration
duration = 3
init(autoreset=True)

input("\nPRESS ENTER TO RECORD YOUR VOICE...")
print(Style.BRIGHT+ Fore.GREEN + "\nSpeak Now...")

# Start recorder with the given values
# of duration and sample frequency
recording = sd.rec(int(duration * freq),
        samplerate=freq, channels=1)

# Record audio for the given number of seconds
sd.wait()
#taking input of speakers name
print(Style.BRIGHT + Fore.GREEN +"\n\nEnter speaker's name : ")
input_label = input()
speaker_name=input_label+".wav"
wv.write(speaker_name, recording, freq, sampwidth=2)

data, samplerate = sf.read(speaker_name)
sf.write(speaker_name, data, samplerate, subtype='PCM_16')

print(Style.BRIGHT + Fore.GREEN +"\nDone.......")



input("\nPRESS ENTER TO PLAY VOICE ... ")
# Extract data and sampling rate from file
data, fs = sf.read(speaker_name, dtype='float32')
sd.play(data, fs)
status = sd.wait()  # Wait until file is done playing
ob = sf.SoundFile(speaker_name)

print(Style.BRIGHT  + Fore.GREEN +"\n.....Audio Details.....")
print(Style.BRIGHT  + Fore.GREEN +'\nSample rate: {}'.format(ob.samplerate))
print(Style.BRIGHT  + Fore.GREEN +'Channels: {}'.format(ob.channels))
print(Style.BRIGHT  + Fore.GREEN +'Subtype: {}'.format(ob.subtype))
