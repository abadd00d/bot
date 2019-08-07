from aiohttp import web
from settings import config
from routes import setup_routes
from views import setup
from telegram import Bot

def setWebhook(bot, host, port, token, cert):
    bot.setWebhook(url='https://%s:%s/%s' % (host, port, token), certificate=open(cert, 'rb'))

app = web.Application()
setup_routes(app)
app['config'] = config

server_conf = app['config']['server']
telegram_conf = app['config']['telegram']

app['bot'] = Bot(telegram_conf['token'])


setWebhook(app['bot'], server_conf['host'], server_conf['port'], telegram_conf['token'], telegram_conf['cert'])
setup(app['bot'])
web.run_app(app, host=server_conf['host'] ,port=server_conf['port'])

