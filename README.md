<h1 align="center">
  <b>Subtitle-Translater</b>
</h1>

<h3 align="center">
මෙම බොට් මගින් ඔබට කුමක් හෝ භාෂාවකින් ඇති උපසිරසියක් තවත් භාෂාවකට පරිවර්තනය කල හැක.
</h3>  

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/d/db/Google_Translate_Icon.png" alt="Translate Logo">
</p>

## Installation

#### The Easy Way


[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/OshadhaVimukthiM/Subtitle-Translater)



#### Deploy On VPS


Simply Folk the repository and run the main file:
```sh
git clone https://github.com/OshadhaVimukthiM/Subtitle-Translater

cd Subtitle-Translater

python3 -m venv venv

. ./venv/bin/activate

pip install -r requirements.txt

python3 bot.py

```

### Create Firebase database

#### Folk the Repo and edit the creds.py with your own variables like below with your own values


```python3
class cred():
    BOT_TOKEN = "your bot token from botfather"
    API_ID = "your api id from my.telegram.org!"       
    API_HASH = "your api hash from my.telegram.org!"   
    DB_URL = "your database url from google firebase" 
    BOT_NAME = "your bot name"     
```
