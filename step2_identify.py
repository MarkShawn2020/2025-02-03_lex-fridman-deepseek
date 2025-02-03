# Start by making sure the `assemblyai` package is installed.
# If not, you can install it by running the following command:
# pip install -U assemblyai
#
# Note: Some macOS users may need to use `pip3` instead of `pip`.

import assemblyai as aai

# Replace with your API key
aai.settings.api_key = "f8349c7f68f5476e9faaabed83d6ed45"

# URL of the file to transcribe
FILE_URL = "DeepSeek, China, OpenAI, NVIDIA, xAI, TSMC, Stargate, and AI Megaclusters ｜ Lex Fridman Podcast #459 [_1f-o0nqpEI].mp3"

# You can also transcribe a local file by passing in a file path
# FILE_URL = './path/to/file.mp3'

config = aai.TranscriptionConfig(speaker_labels=True)

transcriber = aai.Transcriber()
transcript = transcriber.transcribe(
  FILE_URL,
  config=config
)


with open("transcription.txt", "w", encoding="utf-8") as f:
    for utterance in transcript.utterances:
        t = f"Speaker {utterance.speaker}: {utterance.text}"
        print(t)
        f.write(t + "\n\n")

