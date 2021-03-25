# screen-shoter-bot
Telegram bot that takes screenshots of the optional site

## Installation Guide [Docker]:

```
$ git clone https://github.com/ElebrUS/screen-shoter-bot.git
$ cd screen-shoter-bot
Change TOKEN in config.py
$ docker-compose up -d --build
```

## Installation Guide [Heroku]:

```
$ git clone -b heroku https://github.com/ElebrUS/screen-shoter-bot.git heroku
$ cd screen-shoter-bot
$ heroku create
$ heroku labs:enable runtime-dyno-metadata
$ heroku config:set BOT_TOKEN=<your token>
$ heroku buildpacks:add heroku/chromedriver
$ heroku buildpacks:add heroku/google-chrome
$ git add .
$ git commit -am 'Deploy screenshots bot'
$ git push heroku master
```

My Deploy https://t.me/screen_shoter_bot

[Dev TG](https://t.me/ElebrUS)
