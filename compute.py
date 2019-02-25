
import subprocess
import length

vids_path = './videos/'
out = './processed/'
#This is the function that would convert videos into 720p and 480p and get their durations
#
def process(Q,path):
    while not Q.empty():
        video = Q.get()
        print ("length of this video before processing is " + str(length.getLen(video)))
    
        vid_720p = 'ffmpeg -i '+ video + ' -s hd720 ' + video[:-4] + '_720p.mp4'
        name = video[len(vids_path):] #list of names
        subprocess.call(vid_720p, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT, shell=True)
        print (name + ' 720p done')
        print ("length of this video after converting to 720p is " + str(length.getLen(video[:-4] + '_720p.mp4')))

        vid_480p = 'ffmpeg -i '+ video +' -s hd480 '+video[:-4] + '_480p.mp4'
        subprocess.call(vid_480p, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT, shell=True)
        print (name + ' 480p done')
        print ("length of this video after converting to 480p is " + str(length.getLen(video[:-4] + '_480p.mp4')))
        return length.getLen(video)