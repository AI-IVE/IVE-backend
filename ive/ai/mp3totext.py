
BASE_DIR = ""



# get_ipython().system('pip install openai')
# # !pip install python-docx
# get_ipython().system('pip install -U openai-whisper')
# get_ipython().system('pip install AudioSegment')
# # !pip install aspose.words
# # !pip install flextable
# get_ipython().system('pip install sys')


from openai import OpenAI
import whisper
from pydub import AudioSegment
import sys
from configparser import ConfigParser

def load_config(filename='config.properties'):
    parser = ConfigParser()
    parser.read(filename)
    return parser

config = load_config()

OPENAI_API_KEY = config.get('Secrets', 'OPENAI_API_KEY')

client = OpenAI(
    api_key=OPENAI_API_KEY
)


song = AudioSegment.from_mp3("C:\\Users\\lyuji\\Downloads\\baggage.mp3")

ten_minutes = 10 * 60 * 1000

first_10_minutes = song[:ten_minutes]

first_10_minutes.export("C:\\Users\\lyuji\\Downloads\\baggage_10.mp3", format="mp3")


audio_file = open("C:\\Users\\lyuji\\Downloads\\baggage.mp3", "rb")
transcript = client.audio.transcriptions.create(
  file=audio_file,
  model="whisper-1",
  response_format="verbose_json",
  timestamp_granularities=["word"]
)

print(transcript.words)



audio_file = open("C:\\Users\\lyuji\\Downloads\\baggage.mp3", "rb")
transcription = client.audio.transcriptions.create(
  model="whisper-1",
  file=audio_file,
  response_format="text"
)

print(transcript)

print(transcription)


audio_file = open("C:\\Users\\lyuji\\Downloads\\baggage.mp3" , "rb")
transcription2 = client.audio.translations.create(
    model = "whisper-1",
    file=audio_file,
    response_format="text"
)

print(transcription2)


f = open("C:\\Users\\lyuji\\Downloads\\baggage.txt", 'w')
print(transcription, file=f)

f.close()





