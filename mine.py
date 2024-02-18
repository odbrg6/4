import pytesseract
import telebot
import time
import cv2
a = '@iMok7'
b = '@SuPeRx1'
token = "6427291613:AAEriF736i-qdI1aLBDI-TST0pMYwdVIK9o"#token
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start(message):
	bot.reply_to(message,"*send a image*",parse_mode="markdownV2")
@bot.message_handler(content_types=['photo'])
def Start(message):
    ids = message.photo[-1].file_id
    foto = bot.get_file(ids)
    download = bot.download_file(foto.file_path)
    bot.send_message(message.chat.id,text=f'''
		مبرمج الملف : {a}
     & قناة المبرمج : {b}''',parse_mode="MarkdownV2")

    with open('image.png', 'wb') as file:
        file.write(download)
        file.close()
    time.sleep(0.7)

    try:
        img = cv2.imread('image.png')
        texto = pytesseract.image_to_string(img)
        bot.reply_to(message, texto)
    except:
        bot.send_message(message.chat.id, 'حدث خطأ في الصورة ، حاول مرة أخرى‌‌')

bot.infinity_polling()
