import sys
import os
import rich_click as click
from gtts import gTTS
import ntpath
import time
import contextlib
with contextlib.redirect_stdout(None):
    import pygame


class GetAudio:
    def __init__(
        self,
        path,
    ):

        self.path = path 

    def create_mp3(self):
        language = "en-US"
        try:
            with open(self.path) as f:
                the_text = f.read()
                mp3 = gTTS(the_text, lang=language)
                # Save MP3
                # strip filename from filepath
                file_name = ntpath.basename(self.path)
                # strip file type extension from name
                file_name = (
                    file_name.replace(".txt", "")
                    .replace(".rtf", "")
                    .replace(".md", "")
                )
                mp3.save(f"{ sys.path[0] }/mp3s/{file_name}.mp3")
                click.secho(
                    f"\n\nMP3 file created at { sys.path[0] }/mp3s/{file_name}.mp3\n\n", fg="green"
                )
                pygame.mixer.init()  # initialize mixer module
                pygame.mixer.music.load(f"{ sys.path[0] }/mp3s/{file_name}.mp3")
                pygame.mixer.music.play()
                print("Audio sample will play for 3 seconds\n\n")
                time.sleep(3)
        except FileNotFoundError:
            print(
                "\n\nERROR\n\nA file named '{}' does not exist. Please try again.\n\n".format(self.path)
            )

@click.command()
@click.option(
    "--path",
    prompt="\n\nWELCOME to TEXT-2-MP3\n\nEnter the path of the file to convert text to speech (.txt, .rtf or .md)\n\n",
    help="Enter the path of the file to convert text to speech (.txt, .rtf or .md)",
    required=True,
)

def cli(path):
    invoke_class = GetAudio(path)
    invoke_class.create_mp3()


if __name__ == "__main__":
    cli()


