from aiohttp import web
from settings import config
from routes import setup_routes
from views import setup
from telegram import Bot

def setWebhook(bot, telegram_webhoook, cert):
    bot.setWebhook(url=telegram_webhoook, certificate=open(cert, 'rb'))

app = web.Application()
app['config'] = config
setup_routes(app)

server_conf = app['config']['server']
telegram_conf = app['config']['telegram']

app['bot'] = Bot(telegram_conf['token'])

setWebhook(app['bot'], telegram_conf['webhook'], telegram_conf['cert'])
setup(app['bot'])
web.run_app(app, host=server_conf['host'] ,port=server_conf['port'])

