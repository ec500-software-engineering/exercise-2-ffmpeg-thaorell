
import subprocess
import length

vids_path = './videos/'
out = './processed/'
#This is the function that would convert videos into 720p and 480p and get their durations
#
def process(Q,path):
    while not Q.empty():
        video = Q.get()
        original_len = length.getLen(video)
        print ("length of " + video + " before processing is " + str(original_len))
    
        vid_720p = 'ffmpeg -i '+ video + ' -s hd720 ' + video[:-4] + '_720p.mp4'
        name = video[len(vids_path):] #list of names
        subprocess.call(vid_720p, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT, shell=True)
        print (name + ' 720p done')
        len_720 = length.getLen(video[:-4] + '_720p.mp4')
        print ("length of " + video + " after 720p processing is " + str(len_720))
        if len_720 != original_len: 
            raise Exception("Processing error. Length mismatched")

        vid_480p = 'ffmpeg -i '+ video +' -s hd480 '+video[:-4] + '_480p.mp4'
        subprocess.call(vid_480p, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT, shell=True)
        print (name + ' 480p done')
        len_480 = length.getLen(video[:-4] + '_480p.mp4')
        print ("length of " + video + " after 480p processing is " + str(len_480))
        if len_480 != original_len: 
            raise Exception("Processing error. Length mismatched")

        return length.getLen(video)