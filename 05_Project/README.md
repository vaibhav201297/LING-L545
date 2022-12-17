# Project Description

This project performs Audio Speech Recognition for Marathi audio files.
I have used Google's Speech to Text API to create a client session to store marathi audio files on Google's Cloud Bucket and perform audio speech recognition on the files using Google API. 
The project focuses on the two main parameters :
1) Transcription Time
2) Word Error Rate

For the first part, we derive the Transcription times for audio files of different sizes and plot a graph of the time taken to transcribe large audio files.

The audio files have been segmented based on fixed intervals and silence segmentation using Python's pydub library. The audio chunks are passed to Google Speech to Text API which transcribes the files and generates the word error rate %.

The project was tested with 20 audio files of varying sizes and a Word Error Rate % of 42% was achieved.