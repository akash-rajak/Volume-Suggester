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
![image](https://github.com/akash-rajak/Volume-Suggester/assets/57003737/1c53e1fa-faec-4082-9951-078a4d6f46e3)
#### Amplitude over Time Plot
![image](https://github.com/akash-rajak/Volume-Suggester/assets/57003737/986d75e4-b448-47b0-8b48-89ad09b82bb7)
#### Spectogram
![image](https://github.com/akash-rajak/Volume-Suggester/assets/57003737/d3c6bdc3-03a6-4bf4-9363-9264e1bdd8c6)
#### RMS/Energy Spectogram
![image](https://github.com/akash-rajak/Volume-Suggester/assets/57003737/90cc3291-46c0-43f2-a0c3-b065e81c3f32)
#### Zero Crossing Rate
![image](https://github.com/akash-rajak/Volume-Suggester/assets/57003737/2b9f18bc-859f-41ce-910d-095f5cc37718)
#### Mel Frequency Cepstral Coefficients
![image](https://github.com/akash-rajak/Volume-Suggester/assets/57003737/47809936-9d71-4241-97cf-c000f365960f)
#### Mel Frequency Spectogram
![image](https://github.com/akash-rajak/Volume-Suggester/assets/57003737/fe9e501e-bb6d-4ba5-a322-ce80d8b89ab9)
#### Chroma Feature
![image](https://github.com/akash-rajak/Volume-Suggester/assets/57003737/fdf21d27-42f6-4320-85c8-a38366a77193)
#### Tempogram
![image](https://github.com/akash-rajak/Volume-Suggester/assets/57003737/4fe7b54b-35f5-46c3-be01-22fb92bf1989)

****

### Owner :
- Akash Rajak
