from telegram.ext import Updater, MessageHandler, filters
from telegram import ChatAction

# تعريف دالة للرد على حذف الرسائل
def deleted_message(update, context):
    message = update.message
    if message:
        # إرسال رسالة تسأل العضو عن سبب حذف الرسالة
        context.bot.send_message(
            chat_id=message.chat_id,
            text=f"عذراً! لماذا قمت بحذف الرسالة؟",
            reply_to_message_id=message.message_id
        )

def main():
    # تعريف التوكن الخاص بالبوت
    token = '6724095206:AAGeobKqBMfSC_o72mbowIFm1OLlBC-_nO4'

    # إنشاء مستعرض
    updater = Updater(token, use_context=True)

    # حدد المنظف للحصول على الرسائل المحذوفة
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(filters.all, deleted_message))

    # بدء البوت
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
