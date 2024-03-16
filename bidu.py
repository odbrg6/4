import requests
import os
import telebot
from telebot import types
token = "7039462535:AAHNXJQu3BPYLFBk3UHj1QJszpfvNXHHRQc"#Token
bot = telebot.TeleBot(token)
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id,f'''- أهلا انا بوت تحميل من تيك توك .\n- فقط ارسلي رابط الفيديو لكي احمله لك بدون حقوق .''')
@bot.message_handler(func=lambda m:True)
def send(message):
    bot.send_message(message.chat.id,f"<strong>Wait Please</strong>",parse_mode="html")
    url = requests.get(f"https://hbbans.panlhadi.shop/olga/d.php?url={message.text}").json()
    io = url["result"]["download"]
    li = url["result"]["like"]
    co = url["result"]["comment"]
    sh = url["result"]["share"]
    cr = url["result"]["created"]
    by = url["source"]
    bot.send_video(message.chat.id,io,caption=f"""
    Done ✅
لايكات : {li}
تعليقات : {co}
مشاركة : {sh}
نشر بتاريخ : {cr}
    """)
    bot.send_message(message.chat.id,text=f'اشترك شايفك : \n {by}',)
    
bot.polling()
