import os
TOKEN = os.getenv('BOT_TOKEN')

HEROKU_APP_NAME = os.getenv('HEROKU_APP_NAME')
GOOGLE_CHROME_SHIM = os.getenv('GOOGLE_CHROME_SHIM')


# webhook settings
WEBHOOK_HOST = f'https://{HEROKU_APP_NAME}.herokuapp.com'
WEBHOOK_PATH = f'/webhook/{TOKEN}'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

# webServer settings
WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = int(os.getenv('PORT', '8431'))
