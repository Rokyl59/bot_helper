import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler
from telegram.ext import Filters, CallbackContext

from dialogflow import dialogflow_response


def start(update: Update, context: CallbackContext):
    update.message.reply_text('Здравствуйте!')


def send_message(update: Update, context: CallbackContext):
    text = update.message.text
    session_id = update.message.chat_id
    response_text = dialogflow_response(project_id, session_id, text)
    update.message.reply_text(response_text)


if __name__ == '__main__':
    load_dotenv()
    project_id = os.getenv('DF_PROJECT_ID')
    tg_bot_api_key = os.getenv('TOKEN_TG')
    updater = Updater(tg_bot_api_key)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(
        MessageHandler(Filters.text & ~Filters.command, send_message)
    )
    updater.start_polling()
    updater.idle()
