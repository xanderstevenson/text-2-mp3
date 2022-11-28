import sys
import os
import rich_click as click
from gtts import gTTS
import ntpath
import time
# without this, pygame prints a header in the console
import contextlib
with contextlib.redirect_stdout(None):
    import pygame

# main class
class GetAudio:
    def __init__(
        self,
        path,
    ):
        self.path = path 
    # main function
    def create_mp3(self):
        language = "en-US"
        # load text, conver to mp3, save file and play sample for user
        try:
            with open(self.path) as f:
                the_text = f.read()
                # conversion magic
                mp3 = gTTS(the_text, lang=language)
                # strip filename from filepath
                file_name = ntpath.basename(self.path)
                # strip file type extension from name
                file_name = (
                    file_name.replace(".txt", "")
                    .replace(".rtf", "")
                    .replace(".md", "")
                )
                # save mp3
                mp3.save(f"{ sys.path[0] }/mp3s/{file_name}.mp3")
                # Alert use of success and location of mp3
                click.secho(
                    f"\n\nMP3 file created at { sys.path[0] }/mp3s/{file_name}.mp3\n\n", fg="green"
                )
                # Automatically play audio sample and alert user
                pygame.mixer.init()  # initialize mixer module
                pygame.mixer.music.load(f"{ sys.path[0] }/mp3s/{file_name}.mp3")
                pygame.mixer.music.play()
                print("Audio sample will play for 3 seconds\n\n")
                time.sleep(3)
        #handle exception (exits program)
        except FileNotFoundError:
            print(
                "\n\nERROR\n\nA file named '{}' does not exist. Please try again.\n\n".format(self.path)
            )
# Prompt user for input, store as 'path'
@click.command()
@click.option(
    "--path",
    prompt="\n\nWELCOME to TEXT-2-MP3\n\nEnter the path of the file to convert text to speech (.txt, .rtf or .md)\n\n",
    help="Enter the path of the file to convert text to speech (.txt, .rtf or .md)",
    required=True,
)
# Call main class and function
def cli(path):
    invoke_class = GetAudio(path)
    invoke_class.create_mp3()


if __name__ == "__main__":
    cli()


