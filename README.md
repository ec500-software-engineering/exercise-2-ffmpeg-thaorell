# python-CI-template
Python CI template for EC500 Software Engineering

## Introduction
The task for this assignment is to convert videos to 720p and 480p resolutions. 

In compute.py, function process would take a video from a queue and convert to 720p and 480p format
The program will creat three threads as helpers. 
After finishing a job, the program will also check the processed outputs and print "done". 
The program does get the right duration and satisfy the requirements

## Architecture diagram
![alt text](https://imgur.com/a/ca9heoE)

1. When an input gets in, the main program will create three threads.
2. On each threads, the follwing tasks are performed in ffmpeg:
    a. ffmpeg will convert all videos in videos/ directory to 720p and 480p resolutions. Files are named <original_name>_480p and <original_name>_720p for each perspective format
    b. compute.py has a mechanism that checks if there are errors during processing
    c. The output is the length of the processed videos
3. For testing, a sample video "bars.avi" is created and run through compute.py to convert videos. After that. we check the length and frame rate to see if they match the specs of the original video

## Run code
To run code, follow these instructions
1. Clone/download this repo
2. Put videos into ./videos
3. Run:
```
python3 ffmpeg.py
```