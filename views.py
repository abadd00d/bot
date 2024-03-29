from aiohttp import web
from queue import Queue  # in python 2 it should be "from Queue"
from threading import Thread
import telegram
from telegram.ext import Dispatcher, CommandHandler
import requests

def getWebhookStatus(telegram_token):
    r = requests.get('https://api.telegram.org/bot' + telegram_token + '/getWebhookInfo')
    json_data = r.json()
    return json_data['ok']

def setup(bot):
    # Create bot, update queue and dispatcher instances
    update_queue = Queue()

    dispatcher = Dispatcher(bot, update_queue)

    ##### Register handlers here #####
    dispatcher.add_handler(CommandHandler("start", start_callback))

    # Start the thread
    thread = Thread(target=dispatcher.start, name='dispatcher')
    thread.start()

    return update_queue

def webhook(update):
    update_queue.put(update)

async def get_stats(request):
    text = 'OK'
    telegram_token = request.app['config']['telegram']['token']
    text = getWebhookStatus(telegram_token)
    return web.Response(text=str(text))

async def receive_message_from_user(request):
    bot = request.app['bot']
    t_json = (await request.json())
    t_message = telegram.Update.de_json(t_json, bot)
    chat_id = t_message.message.chat.id
    text = 'OK'
    bot.sendMessage(chat_id=chat_id, text=text)
    return web.Response(text=text)

async def send_message_to_user(request):
    text = 'send'
    chat_id = 43638581
    request.app['bot'].send_message(chat_id=chat_id, text="I'm sorry Dave I'm afraid I can't do that.")
    return web.Response(text=text)

def start_callback(update, context):
    user_says = " ".join(context.args)
    update.message.reply_text("You said: " + user_says)