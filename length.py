import subprocess
import json

def getLen(filein):
	command = subprocess.check_output(['ffprobe', '-print_format', 'json', '-v', 'warning', 
                      '-show_streams', '-show_format', filein],
                      universal_newlines=True)
	data = json.loads(command)
	length = float(data['streams'][0]['duration'])
	return length
 