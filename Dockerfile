# сообщает нам на каком образе будет построен наш образ
FROM python:3.9
# копирует файл зависимостей в наш образ
COPY /requirements.txt /app/requirements.txt
# задаем рабочую директорию
WORKDIR /app
# запускаем команду которая установит все зависимости для нашего проекта
RUN pip install -r /app/requirements.txt
# копируем все остальные файлы нашего приложения в рабочую директорию
COPY . /app
RUN apt-get update && apt install -y gconf-service libasound2 libatk1.0-0 libc6 libcairo2 libcups2 \
 libdbus-1-3 libexpat1 libfontconfig1 libgcc1 libgconf-2-4 libgdk-pixbuf2.0-0 libglib2.0-0 libgtk-3-0 \
  libnspr4 libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxcomposite1 \
   libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 libxss1 libxtst6 \
    ca-certificates fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils wget
# заупскаем наше приложение
CMD python /app/bot.py