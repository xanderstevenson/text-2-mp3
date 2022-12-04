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
        accent,
    ):
        self.path = "files-to-read/" + path

        # function to assign accent code based on numerical choice
        def match_accent(accent):
            if accent == "1":
                return "com.au"
            elif accent == "2":
                return "co.uk"
            elif accent == "3":
                return "com"
            elif accent == "4":
                return "ca"
            elif accent == "5":
                return "co.in"
            elif accent == "6":
                return "ie"
            elif accent == "7":
                return "co.za"
            else:
                return "com"

        self.accent = match_accent(accent)

    # main function
    def create_mp3(self):
        print(self.path)
        language = "en"
        # load text, convert to mp3, save file and play sample for user
        try:
            with open(self.path) as f:
                the_text = f.read()
                # conversion magic
                mp3 = gTTS(the_text, lang=language, tld=self.accent)
                # strip filename from filepath
                file_name = ntpath.basename(self.path)
                # strip file type extension from name
                file_name = file_name.replace(".txt", "")
                # save mp3
                mp3.save(f"{ sys.path[0] }/mp3s/{file_name}.mp3")
                # Alert use of success and location of mp3
                click.secho(
                    f"\n\nMP3 file created at { sys.path[0] }/mp3s/{file_name}.mp3\n\n",
                    fg="green",
                )
                # Automatically play audio sample and alert user
                pygame.mixer.init()  # initialize mixer module
                pygame.mixer.music.load(f"{ sys.path[0] }/mp3s/{file_name}.mp3")
                pygame.mixer.music.play()
                print("Audio sample will play for 3 seconds\n\n")
                time.sleep(3)
        # handle exception (exits program)
        except FileNotFoundError:
            print(
                "\n\nERROR\n\nA file named '{}' does not exist. Please try again.\n\n".format(
                    self.path
                )
            )


# Prompt user for file input, store as 'path'
@click.command()
@click.option(
    "--path",
    prompt="\n\nWELCOME to TXT-2-MP3\n\nEnter the .txt file in the files-to-read folder to convert from text to speech (example: 'readthis.txt').\n\n",
    help="Enter the file in the files-to-read folder to convert from text to speech (example: 'readthis.txt')",
    required=True,
)
# Prompt user for accent input, store as 'accent'
@click.option(
    "--accent",
    prompt="\nPlease choose an English accent (type a number and hit ENTER)\n\n\
        1. English (Australia)\n\
        2. English (United Kingdom)\n\
        3. English (United States)\n\
        4. English (Canada)\n\
        5. English (India)\n\
        6. English (Ireland)\n\
        7. English (South Africa)\n\n",
    help="Please choose an English accent",
    required=True,
)


# Call main class and function
def cli(path, accent):
    invoke_class = GetAudio(path, accent)
    invoke_class.create_mp3()


# if you're main, and not remote, this will be invoked ; ) and start the program
if __name__ == "__main__":
    cli()
