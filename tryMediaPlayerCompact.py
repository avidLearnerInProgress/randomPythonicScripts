import easygui,os,sys
import curses
from pydub import AudioSegment
from pydub.playback import play
from tinytag import TinyTag
import eyed3

#Trying to implement single responsibility principle design pattern

def absolute_path_shortner(absolute_path):
		head,tail=os.path.split(absolute_path)
		return tail
'''
def absolute_path_shortner_individual(absolute_path):
	head,tail=os.path.split(absolute_path)
	print(tail)
'''

'''
#To-DO list:
1. check last 3 letters of choosen song for audio format validation
2. CMD or Ncurser module implementation
3. OOP 
4. Do while loop inside init_song_play() for repeated playing of songs
5. To incorporate playlist functionality 
6. other gui details
'''

def get_song_metadata(song_path):
	#title,artist,duration,filesize,year,album,genre,bitrate,disc...
	tag = TinyTag.get(song_path)
	song_title=str(tag.title)
	song_artist=str(tag.artist)
	song_duration=int(tag.duration)
	song_size=int(tag.filesize)
	song_year=float(tag.year)
	song_bitrate=int(tag.bitrate)
	song_genre=str(tag.genre)
	attri_input=int(input("\n(All the attributes)?(Custom Attributes)'Press 1':'Press 2'"))
	if attri_input==1:
		print("Title: %s"%song_title+\
			  "\nArtist: %s"%song_artist+\
			  "\nDuration: %d"%song_duration+\
			  "\nSize: %d"%song_size+\
			  "\nYear: %d"%song_year+\
			  "\nBitrate: %d"%song_bitrate+\
			  "\nGenre: %s"%song_genre)
	elif attri_input==2:	
		get_input=input("Enter attribute detail which you want: ")
		if get_input.lower()=="title":
			print("\nTitle: %s"%song_title)
		elif get_input.lower()=="artist":
			print("\nArtist: %s"%song_artist)
		elif get_input.lower()=="duration":
			print("\nDuration: %d"%song_duration)
		elif get_input.lower()=="size":
			print("\nSize: %d"%song_size)
		elif get_input.lower()=="year":
			print("\nYear: %d"%song_year)
		elif get_input.lower()=="bitrate":
			print("\nBitRate: %d"%song_bitrate)
		elif get_input.lower()=="genre":
			print("\nGenre: %s"%song_genre)
		else:
			print("Attribute Error.")
			sys.exit()
	else:
		print("Error")

def set_song_metadata(song_path):
	#Beta supports only few tag setting options(artist,album,title,genre)
	#Never explored id3 library of python
	#It does support many tags setting options including modifying copyrights etc..
	#URL: http://id3.org/id3v2.3.0#head-70a65d30522ef0d37642224c2a40517ae35b7155

	set_song_title=str(input("Enter title: "))
	set_song_artist=str(input("Enter artist: "))
	set_song_album=str(input("Enter album: "))
	set_song_tracknum=int(input("Enter track number: "))
	
	audiofile=eyed3.load(song_path)
	audiofile.tag.artist=u(set_song_artist)
	audiofile.tag.album=u(set_song_album)
	audiofile.tag.title=u(set_song_title)
	audiofile.tag.genre=u
	audiofile.tag.save()



def lower_system_volume():
	#for linux remove r and set / instead of \\
	os.system(r"D:\\pythonProjectsToStartWith\\KarnGoelSolutions\\data\\getCurrentVolume.exe > data\\outCurrentVolume.txt")
	f=open("data\\outCurrentVolume.txt","r")
	getCurrentVolume=int(f.read())
	print(getCurrentVolume)
	if getCurrentVolume==0:
		volOption=int(input("Volume is in mute state.\nPress 1 to set average volume.\nPress 2 to choose custom volume level:\n"))
		if volOption==1:
			os.system("nircmd.exe setsysvolume 32727")
		elif volOption==2:
			volInput=int(input("Enter volume: "))
			volFinalIp=str(655*volInput)
			os.system("nircmd.exe setsysvolume "+volFinalIp)
		else: 
			print("wrong input.")
			sys.exit()
	else:
		volInput=int(input("Enter volume: "))
		volFinalIp=str(655*volInput)
		os.system("nircmd.exe setsysvolume "+volFinalIp)

def init_audio_player():  #helper function for main 
	choosen_path=easygui.fileopenbox("Choose multiple audio files you want to play", multiple=True)
	print("You have choosen:\n")
	for option in choosen_path:
		returnedObj=absolute_path_shortner(option)
		print(returnedObj)
	print(choosen_path)	
	return choosen_path

def set_metadata_module(selected_files):
	for option in selected_files:
		get_song_metadata(option)

def get_metadata_module(seletecd_files):
	for option in seletecd_files:
		set_song_metadata(option)



#lower media player volume
'''
def addOnFeatures():
    quiteOption=input("Do you want to lower the track sound ? 'Yes/'No' ")
    if quiteOption.lower()=="yes":
        lessdB=lower_song_volume(int(input("Enter value")),song)
	play(lessdB)
    elif quiteOption.lower()=="no":
	play(song)

def lower_song_volume(value,song):
	quiter_song=song-int(value)
	return quiter_song
'''


def init_song_play(choosen_path):
	option=input("Shall we begin playing : 'Yes'/'No' ")
	if option.lower()=="yes":
		for it in choosen_path:
			print("Playing:"+absolute_path_shortner(it))
			song=AudioSegment.from_mp3(it)
			play(song)

def main():
	os.system('cls')
	AudioSegment.converter=r"C:/ffmpeg/bin/ffmpeg.exe"  #can be converted to absolute path by bringing the ffmpeg folder to relative program
	lower_system_volume()
	print("Choose file you want to play:")
	all_choosen_files=init_audio_player()
	init_song_play(all_choosen_files)
	set_metadata_module(all_choosen_files)
	set_metadata_module(all_choosen_files)


if __name__ == '__main__':
	main()
