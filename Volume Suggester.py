
## importing necessary library
from tkinter import filedialog, Tk
from playsound import playsound
import pyaudio
import time
from pynput import keyboard
from pydub import AudioSegment
import wave
import os
import numpy as np
import matplotlib.pyplot as plt
import librosa
import mutagen
from mutagen.wave import WAVE
import subprocess
import pathlib
from pathlib import Path


## declared necessary global variable
file = "" ## for selected file path
wav_file = "" ## for converted wav path
paused = False ## to keep track of audio being paused
stopped = False ## to keep track of audio being stopped


## function to convert .mp3 to .wav
'''
ffmpeg path 
MAQ : C:/Users/MAQ/Path_programs/ffmpeg.exe
Personal : C:/Users/aakas/PATH_Programs/ffmpeg-master-latest-win64-gpl/bin/ffmpeg.exe
'''
def mp3towav():
    global file, wav_file

    dir_name = os.path.dirname(file)
    base_file_name = Path(file).stem
    wav_file = dir_name + "/" + base_file_name + "_wav" + ".wav"
    # print(wav_file)
    subprocess.call(['C:/Users/MAQ/Path_programs/ffmpeg.exe', '-i', file, wav_file])
    # subprocess.call(['C:/Users/aakas/PATH_Programs/ffmpeg-master-latest-win64-gpl/bin/ffmpeg.exe', '-i', file, wav_file])


## function defined to play and pause the audio file
'''
ctrl - to play and pause
esc - to stop
'''
def play_pause_stop():
    global paused, stopped, file, wav_file

    ## opening .wav audio fle
    wf = wave.open(wav_file, 'rb')

    # instantiate PyAudio
    p = pyaudio.PyAudio()

    # define callback
    def callback(in_data, frame_count, time_info, status):
        data = wf.readframes(frame_count)
        return (data, pyaudio.paContinue)

    ## on_press function defined
    def on_press(key):
        global paused, stopped
        # print (key)
        if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
            if stream.is_stopped():     # time to play audio
                print ('[CTRL Pressed] Audio Playing...')
                stream.start_stream()
                paused = False
                return False
            elif stream.is_active():   # time to pause audio
                print ('[CTRL Pressed] Audio Paused...')
                stream.stop_stream()
                paused = True
                return False
        elif key == keyboard.Key.esc:
            print("[ESC Pressed] Audio Stopped...")
            stopped = True
            return False
        return False

    # open stream using callback
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True,
                    stream_callback=callback)

    # start the stream
    stream.start_stream()
    print("\nStream Starts...")

    while stream.is_active() or paused==True:
        if stopped==True:
            break
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()
        time.sleep(0.1)

    # stop stream
    stream.stop_stream()
    stream.close()
    wf.close()

    print("Stream Ends...")

    # close PyAudio
    p.terminate()

## function to get the audio duration
def audio_duration(length):
    hours = length // 3600 # calculate in hours
    length %= 3600
    mins = length // 60 # calculate in minutes
    length %= 60
    seconds = length # calculate in seconds

    return hours, mins, seconds # returns the duration

## function defined to extract generic features of audio file
'''
Channels: number of channels; 1 for mono, 2 for stereo audio
Sample width: number of bytes per sample; 1 means 8-bit, 2 means 16-bit
Frame rate/Sample rate: frequency of samples used (in Hertz)
Frame width: Number of bytes for each “frame”. One frame contains a sample for each channel.
Length: audio file length (in milliseconds)
Frame count: the number of frames from the sample
Intensity: loudness in dBFS (dB relative to the maximum possible loudness)
'''
def extract():
    global file, wav_file
    # Load files
    audio_segment = AudioSegment.from_file(wav_file)
    # Print attributes
    print("\nAudio Generic Features : ")
    print(f"Channels: {audio_segment.channels}")
    print(f"Sample width: {audio_segment.sample_width}")
    print(f"Frame rate (sample rate): {audio_segment.frame_rate}")
    print(f"Frame width: {audio_segment.frame_width}")
    print(f"Duration (sec): {audio_segment.frame_count()/audio_segment.frame_rate}")

    audio = WAVE(wav_file)
    audio_info = audio.info
    length = int(audio_info.length)
    hours, mins, seconds = audio_duration(length)
    print('Total Duration: {}:{}:{}'.format(hours, mins, seconds))

    print(f"Length (ms): {len(audio_segment)}")
    print(f"Frame count: {audio_segment.frame_count()}")
    print(f"Intensity: {audio_segment.dBFS}")


## function defined to generate amplitude wave
def amplitude_wave():
    global file, wav_file

    file_name = os.path.basename(file)

    # Open wav file and read frames as bytes
    sf_filewave = wave.open(wav_file, 'r')
    signal_sf = sf_filewave.readframes(-1)
    # Convert audio bytes to integers
    soundwave_sf = np.frombuffer(signal_sf, dtype='int16')
    # Get the sound wave frame rate
    framerate_sf = sf_filewave.getframerate()
    # Find the sound wave timestamps
    time_sf = np.linspace(start=0, stop=len(soundwave_sf) / framerate_sf, num=len(soundwave_sf))
    # Set up plot
    f, ax = plt.subplots(figsize=(15, 5))
    # Setup the title and axis titles
    plt.title('Amplitude over Time')
    plt.ylabel('Amplitude')
    plt.xlabel('Time (seconds)')
    # Add the audio data to the plot
    plt.plot(time_sf, soundwave_sf, label=file_name, alpha=0.5)
    plt.legend()
    plt.show()


## function defined to generate spectogram graph
'''
A visual representation of the spectrum of frequencies of a signal as it varies with time.
The vertical axis shows frequency, the horizontal axis shows the time of the clip, and the color variation shows the intensity of the audio wave.
'''
def spectogram():
    global file, wav_file

    x, sr = librosa.load(wav_file)
    # Spectrogram of frequency
    X = librosa.stft(x)
    Xdb = librosa.amplitude_to_db(abs(X))
    plt.figure(figsize=(15, 5))
    librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='hz')
    plt.colorbar()
    plt.show()


## function defined to generate RMS/Enerygy Spectogram
'''
Root Mean Square refers to total magnitude of the signal, which in layman terms can be interpreted as the loudness or energy parameter of the audio file.
For loud and rock music RMS value is high
'''
def rms_energy_spectogram():
    global file, wav_file

    y, sr = librosa.load(wav_file)
    # Get RMS value from each frame's magnitude value
    S, phase = librosa.magphase(librosa.stft(y))
    rms = librosa.feature.rms(S=S)
    # Plot the RMS energy
    fig, ax = plt.subplots(figsize=(15, 6), nrows=2, sharex=True)
    times = librosa.times_like(rms)
    ax[0].semilogy(times, rms[0], label='RMS Energy')
    ax[0].set(xticks=[])
    ax[0].legend()
    ax[0].label_outer()
    librosa.display.specshow(librosa.amplitude_to_db(S, ref=np.max), y_axis='log', x_axis='time', ax=ax[1])
    ax[1].set(title='log Power spectrogram')
    plt.show()


## function defined to generate graph for ZCR(Zero Crossing Rate)
'''
ZCR is the rate at which a signal changes from positive to zero to negative or from negative to zero to positive. 
Its value has been widely used in both speech recognition and music information retrieval, being a key feature to classify percussive sounds. 
Highly percussive sounds like rock, metal, emo, or punk music tend to have higher zero-crossing rate values.
For loud and rock music ZCR value is high
'''
def zero_crossing_rate():
    global file, wav_file

    y, sr = librosa.load(wav_file)
    zcrs = librosa.feature.zero_crossing_rate(y)
    print(f"Zero crossing rate: {sum(librosa.zero_crossings(y))}")
    plt.figure(figsize=(15, 3))
    plt.plot(zcrs[0])
    plt.title('Action Rock')
    plt.show()


## function defined to generate graph for MFCC(Mel-Frequency Cepstral Coefficients)
'''
MFCC is a representation of the short-term power spectrum of a sound, based on some transformation in a Mel-scale. 
It is commonly used in speech recognition as people’s voices are usually on a certain range of frequency and different from one to another.
The MFCCs values on human speech seem to be lower and more dynamic than the music files.
'''
def mel_frequency_cepstral_coefficients():
    global file, wav_file

    x, sr = librosa.load(wav_file)
    mfccs = librosa.feature.mfcc(y=x, sr=sr)
    # Displaying  the MFCCs:
    fig, ax = plt.subplots(figsize=(15, 3))
    img = librosa.display.specshow(mfccs, sr=sr, x_axis='time')
    fig.colorbar(img, ax=ax)
    ax.set(title='Music - Warm Memories')
    plt.show()

def mel_frequency_spectogram():
    global file, wav_file

    y, sr = librosa.load(wav_file)
    S = librosa.feature.melspectrogram(y=y, sr=sr)
    S_dB = librosa.power_to_db(S, ref=np.max)
    fig, ax = plt.subplots(figsize=(15, 3))
    # fig, ax = plt.figure(figsize=(15, 3))
    img = librosa.display.specshow(S_dB, sr=sr, x_axis='time')
    fig.colorbar(img, ax=ax, format='%+2.0f dB')
    ax.set(title='Mel-frequency spectrogram')
    plt.show()


## function defined to get the visualization of dominancy of certain pitches{C, C♯, D, D♯, E, F, F♯, G, G♯, A, A♯, B} characteristics
'''
Chroma feature visualization is to know how dominant the characteristics of a certain pitch {C, C♯, D, D♯, E, F, F♯, G, G♯, A, A♯, B} is present in the sampled frame.
'''
def chroma_feature():
    global file, wav_file

    x, sr = librosa.load(wav_file)
    hop_length = 512
    chromagram = librosa.feature.chroma_stft(y=x, sr=sr, hop_length=hop_length)
    plt.figure(figsize=(15, 5))
    librosa.display.specshow(chromagram, x_axis='time', y_axis='chroma', hop_length=hop_length, cmap='coolwarm')
    plt.show()


## function defined to get the tempogram
'''
Tempo refers to the speed of an audio piece, which is usually measured in beats per minute (bpm) units.
Upbeat music like hip-hop, techno, or rock usually has a higher tempo compared to classical music, and 
*** hence tempogram feature can be useful for music genre classification.
'''
def tempogram():
    global file, wav_file


## defining main function
def main():
    global file
    print("Select Audio file : ")
    file = filedialog.askopenfilename(title="Select an Audio file", filetypes=[("Audio Files", "*.mp3"), ("All Files", "*.*")])
    if (file != ""):
        print(file)
        # playsound(file)

        ## calling play_pause_stop function
        # play_pause_stop(file)
    else:
        print("No File Selected")


## calling main function
main()
mp3towav()
extract()
play_pause_stop()
amplitude_wave()
spectogram()
rms_energy_spectogram()
zero_crossing_rate()
mel_frequency_cepstral_coefficients()
mel_frequency_spectogram()
