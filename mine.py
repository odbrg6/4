from telethon.sync import TelegramClient, events

# تعريف المتغيرات اللازمة للوصول إلى الحساب
api_id = '25789625'
api_hash = '3a161749a26291b8315e7769251dea3a'
phone_number = '+37122233543'

# تعريف دالة لإرسال الإخطارات
def send_notification(message):
    print("تم حذف رسالة: ", message)

# إنشاء وتهيئة العميل
client = TelegramClient('session_name', api_id, api_hash)
client.start(phone_number)

# تحديد المحادثة أو القناة
channel_username = 'sdsfsasd'

# التفاعل مع حذف الرسائل
@client.on(events.MessageDeleted(chats=channel_username))
async def handle_deleted_messages(event):
    for msg_id in event.deleted_ids:
        send_notification(f"تم حذف رسالة بالرقم: {msg_id}")

# بدء تشغيل العميل
client.run_until_disconnected()

