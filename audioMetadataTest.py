from tinytag import TinyTag
import sys

path="C:/Users/admin/Desktop/desktop latest windows 10/songs/Kygo & Selena Gomez - It Ain't Me (CDQ).mp3"

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

def main():
	get_song_metadata(path)

if __name__ == '__main__':
	main()
