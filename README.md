# Alexis: Voice Assistant

## About 
Python app that uses [speech recognition](https://pypi.org/project/SpeechRecognition/)
and text-to-speech module to perform actions based on user's voice commands. 
This app initially used the [Google text-to-speech API](https://pypi.org/project/gTTS/) (gTTS), 
but has been updated to use the offline text-to-speech module [pyttsx3](https://pypi.org/project/pyttsx3/).

## Environment
Python 3.8.3

## To run the application
Use `python assitant.py` from the root directory of the project.

### Dependencies
```
pip install SpeechRecognition
pip install pyttsx3
pip install PyAudio
pip install pyperclip
```
(If there is any issue in installing [PyAudio](https://pypi.org/project/PyAudio/] then download and install the 
appropriate .whl file from this [link](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio))

For example, as I used python 3.8 for this project, I had downloaded PyAudio-0.2.11-**cp38-cp38**-win32.whl
from the link.

### Voice Commands
You can add other commands, but these are some tasks it can currently perform
- Tell current date and time
- Search google and youtube
- Play rock, paper and scissor
- Read highlighted / selected text 
- Open any website 

### Apple Mac OS X (Homebrew & PyAudio)
Use Homebrew to install the prerequisite portaudio library, then install PyAudio using pip:
`brew install portaudio`
`pip install pyaudio`

#### Notes:
If not already installed, download Homebrew.
pip will download the PyAudio source and build it for your version of Python.
Homebrew and building PyAudio also require installing the Command Line Tools for Xcode.
Visit https://people.csail.mit.edu/hubert/pyaudio/ for more information.
