from telegram import Update, Bot
from telegram.ext import Updater, MessageHandler, filters, CallbackContext

# تعيين توكن البوت الخاص بك
TOKEN = '6724095206:AAGeobKqBMfSC_o72mbowIFm1OLlBC-_nO4'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('مرحبًا! البوت جاهز لمراقبة الرسائل.')

def delete_message(update: Update, context: CallbackContext) -> None:
    deleted_message = update.message
    chat_id = update.effective_chat.id
    bot = context.bot
    bot.send_message(chat_id=chat_id, text=f"تم حذف رسالة نصية: {deleted_message.text}")

def main() -> None:
    bot = Bot(token=TOKEN)
    updater = Updater(bot=bot)
    dispatcher = updater.dispatcher

    # يقوم البوت بالاستجابة عند بدء المحادثة
    dispatcher.add_handler(MessageHandler(filters.command & filters.private, start))
    
    # يقوم البوت بمراقبة حذف الرسائل
    dispatcher.add_handler(MessageHandler(filters.update.message.delete, delete_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
