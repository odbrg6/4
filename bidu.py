import asyncio
from telethon import TelegramClient
from telethon.tl.functions.messages import SendMessageRequest, DeleteMessagesRequest

# تعريف الجلسة
session = '1BJWap1sBuzDl_dHpqdh56xRpRnd7L6BkcfS1UJjWAl9uCX8oGuRO0P727UZoK55c-vj_8GRle90HQ4boWB_FL6a7bhiI9mSBYnBcAygyHvn49mZyF8NwlQNLzT-SOqw80Svc4zz1xj56G2mkMNZWIvPHIv9SRLN1620GM6A8DpjmYAHSJpxr7OlM66qRcPzgDeEXOKzPfZkBJOX-jrSmTyO1LQeJu4N1dgYjMZs4_ScSG7Rv-0gWQ1byUP7AuO6MniLyo6uFmMIQZUGnj5BT6HLmkeSXOKGL0yK0CflL8lfK5ZnYpuBSZ1bT-1_Wj50LpWaVzx1a-rDTG68IyRi92hYiLCacMdg='

# تعريف بيانات الوصول
api_id = '22877012'
api_hash = '6d59bf3287c22f491e291a8a366c997c'

# بدء الاتصال بالتليجرام باستخدام الجلسة
client = TelegramClient(session, api_id, api_hash)
client.start()

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
