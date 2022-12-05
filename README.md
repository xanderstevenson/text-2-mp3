<p align="center"><img src="https://github.com/xanderstevenson/txt-2-mp3/blob/main/media/txt-2-mp3-colors.png?raw=true" width=400) /></p>

<h3 align="center">A Python program to convert a .txt file, in English, into an MP3 audio file, with choice of English language accent</h3>


* Known to work on Python versions 3.7.13, 3.8.13, 3.9.11, 3.10.0, 3.10.3 and 3.10.8 (at least)

------


### 1. Clone this repository
```
git clone https://github.com/xanderstevenson/txt_2_mp3
```


### 2. cd into txt_2_mp3
```
cd txt_2_mp3
```


### 3. Create and activate virtual environment
```
python3 -m venv venv

source venv/bin/activate # for Mac and Linux
source venv/Scripts/activate # for Windows
```


### 4. Install requirements
```
pip install -r requirements.txt
```
*** requirments sometimes vary per OS, so please install other dependencies as your system advises.



### 5. Run Program
```
$ python3 txt_2_mp3.py 


WELCOME to TXT_2_MP3

Enter the .txt file in the files-to-read folder to convert from text to speech (example: 'readthis.txt').

: readthis.txt

Please choose an English accent (type a number and hit ENTER)

        1. English (Australia)
        2. English (United Kingdom)
        3. English (United States)
        4. English (Canada)
        5. English (India)
        6. English (Ireland)
        7. English (South Africa)

: 6


MP3 file created at /txt_2_mp3/mp3s/readthis.mp3

```

* For a long text, such as several pages, it could take a few minuted for the mp3 file to be rendered.

- MP3s are always saved to 'mp3s' folder one level down from txt-2-mp3.py

- Automatic play of audio sample can be achieved by uncommenting a few lines of code, although overuse could damage your speakers. Mine started crackling after playing these samples hundreds of times while debugging the main function but a system restart cleared it up. Still, use at your own risk. I'm not responsible for any damages.

- Tip: When pasting from a web page or Word doc, delete the image file names or it will read them (they are often long).


- Credit: Much was borrowed from John Capobianco's wiktrola project for this: https://www.youtube.com/watch?v=HbHaZRWq3_I
