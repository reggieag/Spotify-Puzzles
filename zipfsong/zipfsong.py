#zipfsong
import fileinput
import re

data=[]


for line in fileinput.input():
	line = re.split(r'\s', line)
    data.append(line)

numSongs = int(data[0][0])
numSelect = int(data[0][1])
songs = data[1:]
#songs looks like [['30','one'],['30','two']]
#Remember we will need the position of the song

def quality(songs):
	qi=[]
    for x in songs:
        
#possible solution is to normalize according to songs[-1] and then multiply by position

#take songs[-1] and multiply according to position, then divide actualy plays