from TTS.api import TTS
from pydub import AudioSegment
from pydub.silence import detect_nonsilent

def trim_silence(audio, silence_thresh=-40, chunk_size=10):
	non_silent = detect_nonsilent(audio, min_silence_len=100, silence_thresh=silence_thresh)
	if not non_silent:
		return audio
	start = non_silent[0][0]
	end = non_silent[-1][1]
	return audio[start:end]

def split_text(text, max_len=50):
	words = text.split()
	print(words)
	chunks = []
	current = ""

	for word in words:
		if len(current) + len(word) + 1 <= max_len:
			current += " " + word if current else word
		else:
			chunks.append(current)
			current = word
	if current:
		chunks.append(current)
	return chunks

file=input("enter audio file name :- ")
format = input("enter audio format :- ").lower()
path= file+"."+format 

# Step 1: Convert MP3 to WAV

if format!="wav":

	audio = AudioSegment.from_file(path)
	audio = audio.set_channels(1).set_frame_rate(23500)
	audio.export("voice.wav", format="wav")
	path="voice.wav"
	print("MP3 converted to WAV")


# Step 2: Load TTS model
tts = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2")

text= input("Enter your text:- ")

text=split_text(text)


lan = {0:"en" , 1:"hi" , 2:"es" , 3:"fr" , 4:"de" , 5:"it" , 6 :"pt" , 7:"pl" , 8:"tr" , 9:"ru" , 10:"nl" ,  11:"cs" , 12:"ar" , 13:"zh-cn" , 14:"ja" , 15:"ko" }
print(lan)
choice= int(input("enter language number :- "))

# Step 3: Generate and combine audio

final_audio = AudioSegment.empty()   #  important

for i, speak in enumerate(text):
	speak = speak.strip()
	if speak == "":
		continue
	temp_file = f"temp_{i}.wav"
	tts.tts_to_file(text=speak,speaker_wav=path,language=lan[choice],file_path=temp_file)
	print(f"Generated part {i}")

    # Load generated audio
	speech = AudioSegment.from_wav(temp_file)
#  REMOVE INTERNAL SILENCE
	speech = trim_silence(speech)

    # 🔻 Slow down playback
	slow_speech = speech._spawn(speech.raw_data,overrides={"frame_rate": int(speech.frame_rate * 0.999)}).set_frame_rate(23500)

    # Add to final audio
	final_audio += slow_speech

# Create silence (1 second)
silence = AudioSegment.silent(duration=1000)

final_audio=silence+final_audio+silence

# Step 4: Export final merged audio
final_audio.export("output.wav", format="wav")

print("✅ Final merged audio saved as output.wav")
