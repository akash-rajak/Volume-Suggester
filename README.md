## ✔ Volume Suggester
- Python tool to provide suggestion on volume at which the music audio file needs to be played for better experience and feeling.
- In backend, it extracts various generic features for particular audio and analyze among them and provide feedback on volumne on it.  
- This tools helps in maintaining goob vibes along the music playout.

![image](https://github.com/akash-rajak/Volume-Suggester/assets/57003737/1d332d56-b26a-4ba6-8b72-46efca4f1deb)
****

### REQUIREMENTS :
- python 3
- tkinter
- from tkinter import filedialog
- pyaudio
- time
- from pynput import keyboard
- from pydub import AudioSegment
- wave
- os
- numpy
- matplotlib.pyplot
- librosa
- mutagen
- from mutagen.wave import WAVE
- subprocess
- pathlib
- from pathlib import Path

****

### How this Script works :
- First user need to download the script and run Volume Suggester.py in the local system.
- After running it, user will be prompted to select an audio file(mp3 file) using dialog box.
- Once user has selected the audio file, following feature extraction and analysis graph will be generated at the backend.
	- Generic Audio Features:
		- `Channels` : (number of channels; 1 for mono, 2 for stereo audio)
		- `Sample Width` : (number of bytes per sample; 1 means 8-bit, 2 means 16-bit)
		- `Frame Rate / Sample Rate` : (frequency of samples used (in Hertz))
		- `Frame Width` : (Number of bytes for each “frame”. One frame contains a sample for each channel.)
		- `Audio Length / Duration` : (audio file length (in milliseconds))
		- `Frame Count` : (the number of frames from the sample)
		- `Intensity` : (loudness in dBFS (dB relative to the maximum possible loudness))
	- Plot on `Amplitude over Time` Analysis
	- Following Derived Audio Features:
		- `Spectogram`
		- `RMS/Energy Spectogram`
		- `Zero Crossing Rate`
		- `Mel Frequency Cepstral Coefficients`
		- `Mel Frequency Spectogram`
		- `Chroma Feature`
		- `Tempogram`
- After these feature extraction is done, user will be able to Play/Pause(using CTRL button) and Stop(using ESC button) the selected song.

****

### SCREENSHOTS :
#### Amplitude over Time Plot
![image](https://github.com/akash-rajak/Volume-Suggester/assets/57003737/986d75e4-b448-47b0-8b48-89ad09b82bb7)

****

### Owner :
- Akash Rajak
