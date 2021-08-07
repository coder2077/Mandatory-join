''''
Example code by @coder2077 . Press star and follow me.
If you have found a bug, create issue.

Attention: Bot must be administrator in channel or supergroup for getting status.
'''


import telebot
from telebot import types
from config import *

bot = telebot.TeleBot(TOKEN)

def buttons():
	markup = types.InlineKeyboardMarkup()
	markup.add(types.InlineKeyboardButton(text='Channel Name', url=channel_url))
	markup.add(types.InlineKeyboardButton(text='Check', callback_data='check'))

	return markup

# /start command handler
@bot.message_handler(commands=['start'])
def send_welcome(message):
	welcome_text = "First, subscribe to our channel!"
	# Attention: Bot must be administrator in channel or supergroup for getting status.
	status = bot.get_chat_member(chat_id=channel_username, user_id=message.from_user.id).status

	allowed_list = ['member','administrator','creator']
	if status in allowed_list:
		bot.send_message(chat_id=message.chat.id, text="You are already a member. Thank you!")
	else:
		bot.send_message(chat_id=message.chat.id, text=welcome_text, reply_markup=buttons())

# Callback query handler
@bot.callback_query_handler(func = lambda call: call.data == "check")
def check(call):
	status = bot.get_chat_member(chat_id=channel_username, user_id=call.from_user.id).status
	allowed_list = ['member','administrator','creator']
	if status in allowed_list:
		bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Thank you")
	else:
		bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
		bot.send_message(chat_id=call.message.chat.id, text=f'First, subscribe to our channel!\nChannel: {channel_username}', reply_markup=buttons())

bot.polling(none_stop=True)

''' Example code by @coder2077 '''
