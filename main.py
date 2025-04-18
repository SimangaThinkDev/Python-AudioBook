# MAke sure you have installed the library gTTS
# [ pip install gTTS ]
from gtts import gTTS
import os
from click import echo, style

def create_audiobook( text_file, output_file ):
    
    # Open the file you would like to turn into an audio book
    with open( text_file, "r", encoding = "utf-8" ) as file :
        speech = file.read()
        
    # Use the gTTS library to convert to mp3
    as_audio = gTTS( text = speech, lang = "en" )
    
    as_audio.save( output_file )
    echo( style( f"Your file has been saved as {output_file}", fg = "green", bold = True ) )
    

# Implement Logic
if __name__ == "__main__" :
    
    text_file = "denzel.txt" # Change to your desired txt file if any
    output_file = f"{ text_file[ :-4 ] }.mp3"
    
    create_audiobook( text_file, output_file )
    
    # Optional play the Audio Book
    os.system( f"start {output_file}" )

# ARIGATO