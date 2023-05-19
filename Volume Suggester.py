
## importing necessary library
from pathlib import Path
from tkinter import filedialog, Tk
from tkinter.filedialog import askdirectory
from playsound import playsound

import pyaudio
import wave
import time
from pynput import keyboard


## function defined to play and pause the audio file
def play_pause(file):
    paused = False    # global to track if the audio is paused

    # you audio here
    wf = wave.open(file, 'rb')

    # instantiate PyAudio
    p = pyaudio.PyAudio()

    # define callback
    def callback(in_data, frame_count, time_info, status):
        data = wf.readframes(frame_count)
        return (data, pyaudio.paContinue)

    def on_press(key):
        global paused
        print (key)
        if key == keyboard.Key.space:
            if stream.is_stopped():     # time to play audio
                print ('play pressed')
                stream.start_stream()
                paused = False
                return False
            elif stream.is_active():   # time to pause audio
                print ('pause pressed')
                stream.stop_stream()
                paused = True
                return False
        elif key == keyboard.Key.esc:
            stream.stop_stream()
            stream.close()
            wf.close()
            p.terminate()
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

    while stream.is_active() or paused==True:
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()
        time.sleep(0.1)

    # stop stream
    stream.stop_stream()
    stream.close()
    wf.close()

    # close PyAudio
    p.terminate()


## defining main function
def main():
    print("Select Audio file : ")
    file = filedialog.askopenfilename(title="Select file")
    if (file != ""):
        print(file)
        # playsound(file)

        play_pause(file)
    else:
        print("No File Selected")


## calling main function
main()