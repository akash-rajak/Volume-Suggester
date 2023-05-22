
## importing necessary library
from tkinter import filedialog, Tk
from tkinter.filedialog import askdirectory
from playsound import playsound
import pyaudio
import wave
import time
from pynput import keyboard
from pydub import AudioSegment


file = "" ## global variable declared to store file location
paused = False # global to track if the audio is paused
stopped = False # global variable declared to keep track of stopping audio

## function to convert .mp3 to .wav
def mp3towav():
    pass

'''
ctrl - to play and pause
esc - to stop
'''
## function defined to play and pause the audio file
def play_pause_stop():
    global paused, stopped, file

    ## opening .wav audio fle
    wf = wave.open(file, 'rb')

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
    print("Stream Starts...")

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

'''
Channels: number of channels; 1 for mono, 2 for stereo audio
Sample width: number of bytes per sample; 1 means 8-bit, 2 means 16-bit
Frame rate/Sample rate: frequency of samples used (in Hertz)
Frame width: Number of bytes for each “frame”. One frame contains a sample for each channel.
Length: audio file length (in milliseconds)
Frame count: the number of frames from the sample
Intensity: loudness in dBFS (dB relative to the maximum possible loudness)
'''
## function defined to extract generic features of audio file
def extract():
    global file
    # Load files
    audio_segment = AudioSegment.from_file(file)
    # Print attributes
    print("\n\nAudio Generic Features : ")
    print(f"Channels: {audio_segment.channels}")
    print(f"Sample width: {audio_segment.sample_width}")
    print(f"Frame rate (sample rate): {audio_segment.frame_rate}")
    print(f"Frame width: {audio_segment.frame_width}")
    print(f"Length (ms): {len(audio_segment)}")
    print(f"Frame count: {audio_segment.frame_count()}")
    print(f"Intensity: {audio_segment.dBFS}")


## function defined to generate amplitude wave
def amplitude_wave():
    global file


## defining main function
def main():
    global file
    print("Select Audio file : ")
    file = filedialog.askopenfilename(title="Select file")
    if (file != ""):
        print(file)
        # playsound(file)

        ## calling play_pause_stop function
        # play_pause_stop(file)
    else:
        print("No File Selected")


## calling main function
main()
play_pause_stop()
extract()

