import requests
import telebot

token = "6724095206:AAHcTqyenhPr3CJUlsRQblMYNHAYiJxZnmc"
bot = telebot.TeleBot(token)
headers = {
    'authority': 'my.telegram.org',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://my.telegram.org',
    'referer': 'https://my.telegram.org/auth',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 12; M2004J19C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}
@bot.message_handler(commands=["start"])
def start(message):
	bot.reply_to(message,'ارسل رقمك مع رمز الدول ')
@bot.message_handler(func=lambda brok:True)
def num(message):
    data = {
    'phone': message.text,
    }
    response = requests.post('https://my.telegram.org/auth/send_password', headers=headers, data=data)
    
    
    bot.reply_to(message,'تم الارسال')
    
bot.polling()
