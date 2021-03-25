from aiogram import Bot, Dispatcher, executor, types
from config import *
from aiogram.dispatcher.filters import Filter
import validators
from pyppeteer import launch
import io


class IsUrl(Filter):
    """
    Этот Filter проверяет отправленное смс на содержание ссылки
    """
    async def check(self, message: types.Message) -> bool:
        return validators.url(message.text)


async def take_screen(url: str, delete_static: bool = False):
    """
    Функция прогрузки url и создания скриншота
    """
    browser = await launch(
        headless=True,
        args=[
            '--no-sandbox',
            '--single-process',
            '--disable-dev-shm-usage',
            '--disable-gpu',
            '--no-zygote'
        ])
    page = await browser.newPage()
    await page.goto(url, waitUntil='domcontentloaded')
    height = await page.evaluate('document.body.scrollHeight', force_expr=True)
    await page.setViewport({
      'width': 1920,
      'height': height,
      'deviceScaleFactor': 1,
    })
    await page.waitForFunction("document.readyState === 'complete'")
    if delete_static:
        page = await remove_static(page)

    img = await page.screenshot(encoding='binary')
    await browser.close()
    return io.BytesIO(img)


async def remove_static(page):
    """
    Функция Удаление статики из driver
    """
    list_elements_delete = ['jdiv', '#chatra', '#fca_phone_div', '#clbh_phone_div', '#bingc-phone-button',
                            '#top_btn', '#upButton', '.back-top', '.button-up']

    for element in list_elements_delete:
        try:
            el = await page.querySelector(element)
            await page.evaluate('(element) => element.remove()', el)
        except Exception as e:
            pass
    return page
