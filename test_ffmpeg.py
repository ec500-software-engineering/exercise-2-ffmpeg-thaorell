from compute import process
import queue 
import pytest
from test_init import genpat

def test_ffmpeg(genpat):
	q = queue.Queue()
	vid = str(genpat)
	q.put(vid)
	length = process(q,vid)
	assert length == pytest.approx(1.)

if __name__ == '__main__':
	pytest.main(['-x',__file__])