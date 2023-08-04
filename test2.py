import librosa
import matplotlib.pyplot as plt
import numpy as np

def display_spectrogram(audio_segment):
    # Calculate the spectrogram of the audio segment
    spectrogram = librosa.spectrogram(audio_segment)

    # Plot the spectrogram
    plt.figure(figsize=(12, 8))
    plt.imshow(spectrogram, aspect="auto", cmap="gray")
    plt.xlabel("Time (ms)")
    plt.ylabel("Frequency (Hz)")
    plt.show()

def play_audio_segment(audio_segment):
    # Play the audio segment
    librosa.output.play(audio_segment)

def main():
    # Load the audio file
    audio_file, _ = librosa.load("/Users/lechonminhdat/Desktop/Workspace/NOHCEL-1/dataset/wav/FPTOpenSpeechData_Set001_V0.1_000024.wav")

    # Select a segment of the audio file
    audio_segment = audio_file[0:10000]

    # Display the spectrogram of the audio segment
    display_spectrogram(audio_segment)

    # Play the audio segment
    play_audio_segment(audio_segment)

if __name__ == "__main__":
    main()