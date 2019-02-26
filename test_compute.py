from compute import process
import queue 
import subprocess
import pytest
import length

def test_compute(genpat):
	q = queue.Queue()
	vid = str(genpat)
	vid_720p = vid[:-4] + '_720p.mp4'
	vid_480p = vid[:-4] + '_480p.mp4'
	q.put(vid)
	len = process(q,vid)
	length_720p = length.getLen(vid_720p)		
	length_480p = length.getLen(vid_480p)
	if len != length_720p or len != length_480p:
		raise Exception("Processing Error. Length Mismatched!")
	original_fr = getRate(vid)
	fr_720p = getRate(vid_720p)
	fr_480p = getRate(vid_480p)
	if original_fr != fr_480p or original_fr != fr_720p:
		raise Exception("Processing Error. Framerate mismatched!")
	assert len == pytest.approx(1.)

## Check the frame rates
def getRate(vid):
	return subprocess.call(['ffprobe', '-v' , 'error',
		'-select_streams' , 'v:0' , '-show_entries' , 'stream=avg_frame_rate' ,
		'-of' , 'default=noprint_wrappers=1:nokey=1' , vid])
if __name__ == '__main__':
	pytest.main(['-x',__file__])