import queue
import threading
import os
import compute
vids_path = './videos'
out = './processed'

def main():
	q = queue.Queue()
	directory = os.listdir(vids_path)
	for file in directory:
		q.put(vids_path+"/"+file)
	for i in range(3):
		worker = threading.Thread(target=compute.process, args=(q,vids_path))
		worker.start()
		worker.join()

if __name__ == "__main__":
	main()
	
