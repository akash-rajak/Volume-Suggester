
## importing necessary library
from pathlib import Path
from tkinter import filedialog, Tk
from tkinter.filedialog import askdirectory

## defining main function
def main():
    print("Select Audio file : ")
    file = filedialog.askopenfilename(title="Select file")
    if (file != ""):
        print("Currently Processing {" + str(Path(file).stem) + ".mp3}...")
    else:
        print("No File Selected")

main()