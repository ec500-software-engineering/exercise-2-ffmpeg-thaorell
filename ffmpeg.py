import queue
import length
import threading
import subprocess
import os

vids_path = './videos'
out = './finished'


def ffmpeg_convert(Q,path):
	while not Q.empty():
		vid = Q.get()
		vid720 = "ffmpeg -i "+vid+" -s hd720 -b:v 1M -r 30 "+vid[:-4]+"720.mp4"
		vid480 = "ffmpeg -i "+vid+" -s hd720 -b:v 1M -r 30 "+vid[:-4]+"480.mp4"
		name = vid[len(vids_path):]
		print(name + " 720 is processing")
		subprocess.call(vid720, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT, shell=True)
		print(name + " 720 is finished")
		print(name + " 480 is processing")
		subprocess.call(vid480, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT, shell=True)
		print(name + " 480 is finished")
	return length.getLen(vid)

def main():
	q = queue.Queue()
	folder = os.listdir(vids_path)
	for file in folder:
		q.put(vids_path+"/"+file)
	for i in range(3):
		# create 3 threads
		worker = threading.Thread(target=ffmpeg_convert, args=(q,vids_path))
		worker.start()

if __name__ == "__main__":
	main()
	
