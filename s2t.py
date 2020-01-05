import io

import os
# this line is writen in the dialogsys branch
# let's write again
# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

# Instantiates a client
client = speech.SpeechClient()

# The name of the audio file to transcribe
file_name = os.path.join(
    os.path.dirname(__file__),
    
    'test2.mp3')

#print('--------------------------load data---------------------')
#print(file_name)
# Loads the audio into memory
with io.open(file_name, 'rb') as audio_file:
    content = audio_file.read()
#    print(content)
#    print(type(content))
    audio = types.RecognitionAudio(content=content)
		
config = types.RecognitionConfig(
    encoding=enums.RecognitionConfig.AudioEncoding.ENCODING_UNSPECIFIED,
    #encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=16000,
    language_code='en-US')

# Detects speech in the audio file
response = client.recognize(config, audio)
#print(response)
#print(type(response))
for result in response.results:
    print('Transcript: {}'.format(result.alternatives[0].transcript))
