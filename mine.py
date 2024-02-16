from telegram.ext import Updater, MessageHandler, Filters

# تعريف وظيفة لإرسال رسالة عند حذف الرسالة
def deleted_message(update, context):
    deleted_message_text = "تم حذف الرسالة التالية:\n{}".format(update.effective_message.text)
    context.bot.send_message(chat_id=update.effective_chat.id, text=deleted_message_text)

# تعريف وظيفة البدء للتفاعل مع الرسائل
def main():
    # تعيين التوكن الخاص بالبوت
    updater = Updater("6724095206:AAHcTqyenhPr3CJUlsRQblMYNHAYiJxZnmc", use_context=True)

    # اضافة المناسبة لمعالجة الرسائل المحذوفة
    updater.dispatcher.add_handler(MessageHandler(Filters.update.deleted_message, deleted_message))

    # بدء البوت
    updater.start_polling()

    # البقاء في الحلقة الرئيسية
    updater.idle()

# تنفيذ الدالة الرئيسية
if __name__ == '__main__':
    main()
