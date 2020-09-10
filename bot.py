from telegram.ext import Updater, CommandHandler, MessageHandler
from telegram.ext.filters import Filters
import json

with open('config.json', 'r') as f:
    config = json.load(f)

def forward_message(update, context):
    if update.effective_chat.id == config['input_user']:
        context.bot.forward_message(config['output_user'], config['input_user'], update.message.message_id)

def copy_text(update, context):
    if update.effective_chat.id == config['input_user']:
        context.bot.send_message(config['output_user'], update.message.text)

def copy_photo(update, context):
    if update.effective_chat.id == config['input_user']:
        pid = update.message.photo[-1].file_id
        context.bot.send_photo(config['output_user'], photo=pid)

def copy_video(update, context):
    if update.effective_chat.id == config['input_user']:
        pid = update.message.video.file_id
        context.bot.send_video(config['output_user'], video=pid)

def copy_document(update, context):
    if update.effective_chat.id == config['input_user']:
        pid = update.message.document.file_id
        context.bot.send_document(config['output_user'], document=pid)

def copy_audio(update, context):
    if update.effective_chat.id == config['input_user']:
        pid = update.message.audio.file_id
        context.bot.send_audio(config['output_user'], audio=pid)

def copy_voice(update, context):
    if update.effective_chat.id == config['input_user']:
        pid = update.message.voice.file_id
        context.bot.send_voice(config['output_user'], voice=pid)

updater = Updater(config['token'], use_context=True)
updater.dispatcher.add_handler(MessageHandler(Filters.update.message & ~Filters.voice & ~Filters.audio & ~Filters.document & ~Filters.text & ~Filters.photo & ~Filters.video, forward_message))
updater.dispatcher.add_handler(MessageHandler(Filters.text, copy_text))
updater.dispatcher.add_handler(MessageHandler(Filters.photo, copy_photo))
updater.dispatcher.add_handler(MessageHandler(Filters.video, copy_video))
updater.dispatcher.add_handler(MessageHandler(Filters.document, copy_document))
updater.dispatcher.add_handler(MessageHandler(Filters.audio, copy_audio))
updater.dispatcher.add_handler(MessageHandler(Filters.voice, copy_voice))

updater.start_polling()
updater.idle()

