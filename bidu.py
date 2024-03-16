import telebot , requests , json ; from telebot import types
token = "7039462535:AAHNXJQu3BPYLFBk3UHj1QJszpfvNXHHRQc"#Token
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start(message):
	start = types.InlineKeyboardButton(text='- تنزيل فيديو',callback_data='start')
	Ronaldo = types.InlineKeyboardMarkup(row_width=2) ; Ronaldo.add(start)
	bot.send_message(message.chat.id,text='- اهلا بك عزيزي في بوت تحميل من تيك توك اختر من الازرار التاليه',reply_markup=Ronaldo)
@bot.callback_query_handler(func=lambda call:True)
def start2(call):
	if call.data=='start':
		ji = bot.send_message(call.message.chat.id,text='- اهلاً بَك عزيزي ارسل الرابط الان .')
		bot.register_next_step_handler(ji,dow)
def dow(message):
		url = message.text
		headers = {"referer":"https://lovetik.com/sa/video/","origin":"https://lovetik.com","user-agent":"Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0"}
		payload = {"query":url}
		url =requests.post("https://lovetik.com/api/ajax/search",headers = headers,data=payload).json()
		try:
			respones=json.loads('{"ok":"true","Video":{"authorUser":"'+url['author']+'","authorName":"'+url['author_name']+'","authorImage":"'+url['author_a']+'","cover":"'+url['cover']+'","vidID":"'+url['vid']+'","desc":"'+url["desc"]+'","link":"'+url['links'][4]['a']+'","audioName":"'+url['links'][5]['s']+'","audioLink":"'+url['links'][5]['a']+'"}}') 
		except:
			bot.send_message(message.chat.id,'- عذراً عزيزي الرابط غير صالح !')
		bot.send_video(message.chat.id,respones['Video']['link'],caption='- Done Download Video .')
if __name__=="__main__":
	bot.infinity_polling()
