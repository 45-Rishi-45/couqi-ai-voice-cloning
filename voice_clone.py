
from TTS.api import TTS
import os
from pydub import AudioSegment

# Define the paths for the input audio files
audio_files = [
    r"C:\Users\Rishith\Downloads\Git repo\dataset\billgates_3 .mp3",
    r"C:\Users\Rishith\Downloads\Git repo\dataset\billgates_2 .mp3",
    r"C:\Users\Rishith\Downloads\Git repo\dataset\billgates_1.mp3" #Paste the path of input audio files
]

# Output directory
output_dir = r"E:\Intern (12.24-1.25)\Day 13\ravish\output_cloned"#Paste the path of output folder to be saved
os.makedirs(output_dir, exist_ok=True)

# Initialize the TTS model
print("Loading XTTS model...")
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")

# Text to synthesize
text_to_speak = (
   "Hello, this is a demonstration of a cloned voice created using AI technology."#Put your own choose of text
)

# Prepare the final list of speaker WAV paths
final_speaker_wavs = []
for i, audio_path in enumerate(audio_files):
    if not os.path.exists(audio_path):
        print(f"Audio file does not exist: {audio_path}")
        continue

    # Convert MP3 to WAV if needed
    if audio_path.endswith(".mp3"):
        print(f"Converting {audio_path} to WAV...")
        mp3_audio = AudioSegment.from_mp3(audio_path)
        wav_path = os.path.join(output_dir, f"converted_audio_{i}.wav")
        mp3_audio.export(wav_path, format="wav")
        final_speaker_wavs.append(wav_path)
    else:
        # If it's already a WAV file, use it directly
        final_speaker_wavs.append(audio_path)

# Generate the cloned voice using the prepared speaker WAVs
if final_speaker_wavs:
    print("Generating speech with combined voice...")
    output_file = os.path.join(output_dir, "cloned_voice_combined.wav")
    tts.tts_to_file(
        text=text_to_speak,
        file_path=output_file,
        speaker_wav=final_speaker_wavs,
        language="en"
    )
    print(f"Cloned voice saved to: {output_file}")
else:
    print("No valid input files were found. Please check the provided paths.")

print("Voice cloning process completed!")
