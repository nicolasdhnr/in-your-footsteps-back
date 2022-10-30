# API KEY AIzaSyBfHN0NOcu3P59Amub88pTg19xr8oAgwrU
# Imports the Google Cloud client library
from google.cloud import speech
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="F:/hackathon/bgn-hack22lon-6503-3ca0088146eb.json"
# Key = 'AIzaSyBfHN0NOcu3P59Amub88pTg19xr8oAgwrU'

# Instantiates a client
client = speech.SpeechClient()

# The name of the audio file to transcribe
def audio_file_url(gcs_uri):
    audio = speech.RecognitionAudio(uri=gcs_uri)


    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
    )

    # Detects speech in the audio file
    response = client.recognize(config=config, audio=audio)

    for result in response.results:
        print("Transcript: {}".format(result.alternatives[0].transcript))

gcs_uri = "gs://cloud-samples-data/speech/brooklyn_bridge.raw"
audio_file_url(gcs_uri)