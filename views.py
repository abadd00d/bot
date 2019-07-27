from aiohttp import web
from queue import Queue  # in python 2 it should be "from Queue"
from threading import Thread
from telegram.ext import Dispatcher

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
    return web.Response(text=text)

async def receive_message_from_user(request):
    update.message.reply_text("You said: " + user_says)
    text = 'OK'
    return web.Response(text=text)

async def send_message_to_user(request):
    text = 'send'
    chat_id = 43638581
    request.app['bot'].send_message(chat_id=chat_id, text="I'm sorry Dave I'm afraid I can't do that.")
    return web.Response(text=text)

def start_callback(update, context):
    user_says = " ".join(context.args)
    update.message.reply_text("You said: " + user_says)