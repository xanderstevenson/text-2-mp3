import sys
import rich_click as click
import webbrowser
from gtts import gTTS
import ntpath


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
                    .replace(".docx", "")
                    .replace(".doc", "")
                    .replace(".rtf", "")
                )
                mp3.save(f"{file_name}.mp3")
                click.secho(
                    f"MP3 file created at { sys.path[0] }/{file_name}.mp3", fg="green"
                )
                webbrowser.open(f"{file_name}.mp3")
        except FileNotFoundError:
            print(
                "A file named '{}' does not exist. Please try again.".format(self.path)
            )


@click.command()
@click.option(
    "--path",
    prompt="Enter the path of the file yo convert text to speech",
    help="Enter the path of the file yo convert text to speech",
    required=True,
)
def cli(path):
    invoke_class = GetAudio(path)
    invoke_class.create_mp3()


if __name__ == "__main__":
    cli()
