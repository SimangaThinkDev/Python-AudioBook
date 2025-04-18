# Python Audiobook

*A simple Python script that converts text files into audiobooks using the Google Text-to-Speech (gTTS) library.*


## Requirements
- Python 3.x
- gTTS library (pip install gTTS)

## Usage
1. Install the required library by running pip install gTTS in your terminal/command prompt.
2. Replace "denzel.txt" with the path to your desired text file.
3. Run the script using Python (e.g., python audiobook.py).
4. The script will create an MP3 file with the same name as the text file but with an .mp3 extension.
5. Optionally, the script can play the audiobook automatically (Windows only).

## Notes
- Make sure the text file is encoded in UTF-8 for proper reading.
- The script uses the English language by default (lang="en"). You can change this to support other languages.
- The audiobook will be saved in the same directory as the script.

## Future Improvements
- Build a UI using either tkinter or django
- Add option to customize the audiobook's voice and speed

## Contributing
Feel free to modify and improve the script to suit your needs. Pull requests and suggestions are welcome!