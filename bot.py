from typing import Pattern
from telegram.ext import  Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, chat, message, replymarkup
import random
import nltk
import json


API_KEY="5003371417:AAHY5M5l1BRepyt787fM45TC_4zWVcyQT7Q"

A,B,C= range(3)


def welcome(update,context):
	context.user_data['message_id'] = update.message.message_id
	keyboard = [
		[InlineKeyboardButton("About astu", callback_data = 'about')],
		[InlineKeyboardButton("Programs", callback_data = "program")],
		[InlineKeyboardButton("About school", callback_data = "school")],
		[InlineKeyboardButton("Question",callback_data="question")]
	]
	mykeyboard = InlineKeyboardMarkup(keyboard)

	context.bot.send_message(
		chat_id=update.message.chat_id,
		text="welcome to ASTUinfo bot",
		reply_markup = mykeyboard
	)
	return A

def about(update, context):
	context.bot.send_document(chat_id=update.effective_chat.id, document = open('astu.txt'))


def question(update,context):
	query=update.callback_query
	context.user_data['message_id']=query.message.message_id
	context.bot.edit_message_text(chat_id=query.message.chat_id,message_id= query.message.message_id,text="you can ask what you want about astu")


def school(update,context):
	with open('about.json') as f:
		data = json.load(f)
	mess = "".join(data['about'])
	context.bot.send_message(chat_id = update.effective_chat.id, text = mess)

	query =update.callback_query

	context.user_data['message_id']=query.message.message_id
	keyboard=[
		[InlineKeyboardButton("School of Applied Natural Sciences",callback_data='applied')],
		[InlineKeyboardButton("School of Civil Engineering and Architecture",callback_data='civil')],
		[InlineKeyboardButton("School of Electrical Engineering and Computing",callback_data='electrical')],
		[InlineKeyboardButton("School of Mechanical Chemical and Materials Engineering",callback_data='mechanical')]
	]
	reply_markup=InlineKeyboardMarkup(keyboard)

	context.bot.edit_message_text(
		chat_id=query.message.chat_id,
		message_id = query.message.message_id,
		text = "choose: ",
		reply_markup = reply_markup
	)
	return C


def applied(update,context):
	context.bot.send_document(chat_id=update.effective_chat.id,document=open('applied.txt'))

def civil(update,context):
	context.bot.send_document(chat_id=update.effective_chat.id,document=open('civil.txt'))

def electrical(update,context):
	context.bot.send_document(chat_id=update.effective_chat.id,document=open('elec.txt'))

def mechanical(update,context):
	context.bot.send_document(chat_id=update.effective_chat.id,document=open('mec.txt'))



def program(update, context):
	query = update.callback_query

	context.user_data['message_id'] = query.message.message_id
	keyboard=[
		[
			InlineKeyboardButton("Undergrauate", callback_data="Undergrauate"),
			InlineKeyboardButton("Postgraduate", callback_data="Postgraduate")
		]
	]
	reply_markup = InlineKeyboardMarkup(keyboard)

	context.bot.edit_message_text(
		chat_id = query.message.chat_id,
		message_id = query.message.message_id,
		text = "choose: ",
		reply_markup = reply_markup
		)
	return B

def Undergrauate(update, context):
	context.bot.send_message(chat_id = update.effective_chat.id, text = "0996529960")

def response(text):
	if text in text in ["how are you", "heyy", "hi", "hello"]:
		arr = ["hello", "hi", "good to see you", "nice to meet you"]
		rep = random.choice(arr)
	elif text in ["chaw", "bye", "good bye", "see you"]:
		arr = ["bye", "see you later", "bye bye" , "goodbye"]
		rep = random.choice(arr)

	else:
		rep = "I didn't understand you"
	return rep


def answer(update, context):
	text = update.message.text
	mess = response(text)
	context.bot.send_message(chat_id = update.message.chat_id, text = mess)	


def main():
	updater = Updater(API_KEY)

	dp = updater.dispatcher
	con_handler = ConversationHandler(
		entry_points=[CommandHandler('start', welcome)],
		states= {
			A: [CallbackQueryHandler(about,   pattern = "^(about)$"),
				CallbackQueryHandler(program, pattern = "^(program)$"),
				CallbackQueryHandler(school,  pattern = "^(school)$"),
				CallbackQueryHandler(question,pattern= "^(question)$")],

			B: [CallbackQueryHandler(Undergrauate, pattern = "^(Undergrauate)$")],

			C: [CallbackQueryHandler(applied,    pattern= "^(applied)$"),
			    CallbackQueryHandler(civil,      pattern= "^(civil)$"),
			    CallbackQueryHandler(electrical, pattern= "^(electrical)$"),
			    CallbackQueryHandler(mechanical, pattern= "^(mechanical)$")]	
		},
	 	fallbacks=[CommandHandler('start', welcome)],
	)

	dp.add_handler(con_handler)
	dp.add_handler(CommandHandler('start', welcome))
	dp.add_handler(MessageHandler(Filters.text, answer))
	updater.start_polling()
	updater.idle()


main()