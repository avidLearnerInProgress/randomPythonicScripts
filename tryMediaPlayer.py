#using winsound and time python package beeping sound
'''
import winsound,time
winsound.Beep(440, 250) # frequency, duration
time.sleep(0.25)
'''

import easygui,os,sys

from pydub import AudioSegment
from pydub.playback import play
from ctypes import cast, POINTER


'''
os.system('cls')
AudioSegment.converter=r"C:/ffmpeg/bin/ffmpeg.exe"  #can be converted to absolute path by bringing the ffmpeg folder to relative program
print("Choose file you want to play:")

choosen_path=easygui.fileopenbox("Multiple audio files you want to play:", "Choose", multiple=True)
print("You have choosen:")
for option in choosen_path:
	head,tail=os.path.split(option)
	print(tail)

option=input("Shall we begin playing : 'Yes'/'No' ")
if option.lower()=="yes":
	for option in choosen_path:
		print("Playing"+option)
		song=AudioSegment.from_mp3(option)
		play(song)	
else:
	print("Closing application")	
	sys.exit()

'''
'''
print("You have choosen:")
head,tail=os.path.split(choosen_path)
print(tail)
option=input("Shall we begin playing : 'Yes'/'No' ")
if option.lower()=="yes":
	os.startfile(choosen_path)
else:
	print("Closing application")	
	sys.exit()

'''
