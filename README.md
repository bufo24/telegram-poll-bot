# telegram-poll-bot
A telegram bot that keeps track of votes on memes.


# Development instructions

## Getting this project up and running

Clone this project, in a terminal do:
```
git clone git@github.com:satoshiradio/telegram-poll-bot.git
```

Create a new virtual env, activate it and install the required libraries:
```
cd telegram-poll-bot
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

Open the folder of this project in your favorite IDE (e.g. Visual Studio Code or PyCharm)

Copy the example config to create a local configuration file:
```
cp config.example.py config.py
```

## Register a bot for local testing

To do this, send the [BotFather](https://t.me/botfather) a `/newbot` command and follow the instructions. 
When you finished the registration your will receive a token to access the HTTP API. Copy this token to the `token` field in `config.py`

That's it!  
Now run `main.py` with either the command `python3 ./main.py` or by running it from your IDE.
