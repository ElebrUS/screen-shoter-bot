import asyncio
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils import exceptions
from aiogram.dispatcher.filters import Filter
import json
import config
from function import IsUrl, take_screen
from urllib.parse import urlparse

# Configure logging
logging.basicConfig(level=logging.ERROR)

# Initialize bot and dispatcher
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    Этот обработчик будет вызываться, когда пользователь отправляет `/start` комманду
    """
    await message.reply(f"Привет, {message.from_user.full_name}"
                        f"\n\nЧтобы получить скриншот сайта"
                        f"\nОтправь ссылку на сайт")


@dp.message_handler(IsUrl())
async def all_message(message: types.Message):
    """
    Этот обработчик будет вызываться, когда пользователь отправляет URL
    """
    try:
        await bot.send_chat_action(message.chat.id, 'typing')
        await message.reply('Начинаю обработку, понадобиться время')
        photo = await take_screen(message.text, True)
        site_name = urlparse(message.text).netloc
        await bot.send_chat_action(message.chat.id, 'upload_document')
        await bot.send_document(
            message.chat.id,
            types.InputFile(photo, f'{site_name}.png'),
            caption='🖼 Ваш Скриншот сайта',
        )
    except Exception as e:
        logging.error(e)
        await message.reply('Ой, что-то пошло не так!')


async def on_startup(dis):
    logging.info('Старт бота....')
    await bot.set_webhook(config.WEBHOOK_URL, drop_pending_updates=True)


def start_heroku():
    executor.start_webhook(
        dispatcher=dp,
        webhook_path=config.WEBHOOK_PATH,
        skip_updates=True,
        on_startup=on_startup,
        host=config.WEBAPP_HOST,
        port=config.WEBAPP_PORT,
    )


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
