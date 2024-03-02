import asyncio
from telethon import TelegramClient
from telethon.tl.functions.messages import SendMessageRequest, DeleteMessagesRequest

# تعيين المتغيرات
api_id = '22877012'
api_hash = '6d59bf3287c22f491e291a8a366c997c'
phone_number = '3584573989485'

# بدء الاتصال بالتليجرام
client = TelegramClient('session_name', api_id, api_hash)
client.start(phone_number)

# دالة لإرسال الرسالة وحذفها بعد فترة زمنية محددة
async def send_and_delete(message, delay):
    # إرسال الرسالة
    sent_message = await client(SendMessageRequest('-1002106912636', message))
    # انتظار فترة زمنية محددة
    await asyncio.sleep(delay)
    # حذف الرسالة
    await client(DeleteMessagesRequest('-1002106912636', [sent_message.id]))

async def main():
    # إرسال الرسالة رقم 1
    await send_and_delete('ارسال 1', 40)
    # انتظار ثانيتين
    await asyncio.sleep(2)
    # إرسال الرسالة رقم 2
    await send_and_delete('ارسال 2', 40)

# تشغيل البرنامج الرئيسي
asyncio.run(main())
