# text-2-mp3

## Python program to convert a text file into an MP3


1. Clone this repository
```
git clone (https://github.com/xanderstevenson/text-2-mp3
```


2. cd into test-2-mp3
```
cd test-2-mp3
```


3. Create and activate virtual environment
```
python3 -m venv venv

source venv/bin/activate # for Mac and Linux
source venv/Scripts/activate # for Windows
```


4. Install requirements
```
pip install -r requirements.txt
```

5. Run Program
```
python3 text-2-mp3.py


WELCOME to TEXT-2-MP3

Enter the path of the file to convert text to speech (.txt, .rtf or .md)
:

readthis.txt


MP3 file created at ////text-2-mp3/mp3s/readthis.mp3


Audio sample will play for 3 seconds
```

*** For a long text, such as several pages, it could take a few minuted for the mp3 file to be rendered.

You can put the relative or absolute file path. MP3s are always saved to 'mp3s' folder one level down from python3 text-2-mp3.py


Credit: I borrowed much from John Capodianco's wiktrola project for this: https://www.youtube.com/watch?v=HbHaZRWq3_I
