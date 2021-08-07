import telebot
from telebot import types
from config import *

bot = telebot.TeleBot(TOKEN)

def buttons():
	markup = types.InlineKeyboardMarkup()
	markup.add(types.InlineKeyboardButton(text='Channel Name', url=channel_link)
	markup.add(types.InlineKeyboardButton(text='Check', callback_data='check')

@bot.message_handler(commands=['start'])
def send_welcome(message):
	welcome_txt = f"_First, subscribe to our channel!_"
	status = bot.get_chat_member(chat_id=my_channel_id, user_id=message.from_user.id).status
	print(status)
	if status != 'left':
		bot.send_message(chat_id=message.chat.id, text="You are already a member.\n*Thank you)*")
	else:
		bot.send_message(chat_id=message.chat.id, text=welcome_txt, reply_markup=channel())

@bot.callback_query_handler(func = lambda query: query.data == "check")
def check(query):
	status = bot.get_chat_member(chat_id=my_channel_id, user_id=query.from_user.id).status
	print(status)
	if status != 'left':
		bot.edit_message_text(chat_id = query.message.chat.id, message_id=query.message.message_id, text="Thank you")
	else:
		bot.delete_message(chat_id = query.message.chat.id, message_id = query.message.message_id)
		bot.send_message(chat_id = query.message.chat.id, text = 'First, subscribe to our channel!\nChannel: @channellink', reply_markup=channel())

bot.polling(none_stop=True)
