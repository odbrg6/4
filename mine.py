import telebot

# Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual bot token
bot = telebot.TeleBot('6724095206:AAGeobKqBMfSC_o72mbowIFm1OLlBC-_nO4')

# Replace 'YOUR_DEVELOPER_CHAT_ID' with the chat ID of the developer
developer_chat_id = '-1001844054913'

@bot.message_handler(func=lambda message: True, content_types=['delete_chat_photo', 'delete_message'])
def handle_deleted_message(message):
    if message.content_type == 'delete_chat_photo':
        bot.send_message(developer_chat_id, f"Admin {message.from_user.username} deleted a photo from the channel.")
    elif message.content_type == 'delete_message':
        bot.send_message(developer_chat_id, f"Admin {message.from_user.username} deleted a message from the channel.")
    
# Start the bot
bot.polling()
