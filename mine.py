import asyncio
from pyrogram import Client

# تعيين متغيرات البيئة
api_id = '25789625'
api_hash = '3a161749a26291b8315e7769251dea3a'
phone_number = '+37122233543'
channel_username = 'sdsfsasd'

# إنشاء وتهيئة العميل
app = Client("my_account", api_id, api_hash)

# دالة لالتقاط لقطة شاشة لآخر الأحداث في القناة
async def capture_last_event_screenshot():
    # الاتصال بالحساب
    await app.start()

    try:
        # الحصول على المحادثة
        chat = await app.get_chat(channel_username)

        # الحصول على آخر رسالة في المحادثة
        last_message = await app.get_history(chat.id, limit=1)

        # التأكد من وجود رسالة
        if last_message:
            # الحصول على الوسائط المرتبطة بالرسالة
            media = last_message[0].media

            # التأكد من وجود وسائط
            if media:
                # التقاط لقطة شاشة للوسائط
                screenshot_bytes = await app.download_media(media)

                # حفظ اللقطة الشاشة
                with open("last_event_screenshot.jpg", "wb") as file:
                    file.write(screenshot_bytes)

                print("تم حفظ اللقطة الشاشة بنجاح.")
            else:
                print("لا توجد وسائط في الرسالة.")
        else:
            print("لا توجد رسالة في المحادثة.")

    finally:
        # إيقاف العميل
        await app.stop()

# تشغيل الدالة
asyncio.run(capture_last_event_screenshot())
