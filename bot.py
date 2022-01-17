from ast import keyword, pattern
from typing import Pattern
from telegram.ext import  Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, chat, message, parsemode, replymarkup
import random
import json
import nltk
from mynltk import botReact
from telegram import ParseMode

API_KEY="5003371417:AAHY5M5l1BRepyt787fM45TC_4zWVcyQT7Q"

A,B,C,D= range(4)

def welcome(update,context):
	context.user_data['message_id'] = update.message.message_id
	keyboard = [
		[InlineKeyboardButton("About ASTU",   callback_data ='about')],
		[InlineKeyboardButton("About Programs",     callback_data ="program")],
		[InlineKeyboardButton("About School", callback_data ="school")],
		[InlineKeyboardButton("Question",     callback_data ="question")],
		[InlineKeyboardButton("Contact Us",  callback_data="contact")]
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


def contact(update,context):
	query= update.callback_query
	context.user_data['message_id'] =query.message.message_id
	keyboard=[
		[InlineKeyboardButton("Facebook Account",callback_data='facebook')],
		[InlineKeyboardButton("Email",callback_data='email')],
		[InlineKeyboardButton("Website",callback_data='web')],
		[InlineKeyboardButton("phone",callback_data='phone')]
	]
	reply_markup=InlineKeyboardMarkup(keyboard)
	context.bot.edit_message_text(
		chat_id=query.message.chat_id,
		message_id = query.message.message_id,
		text="We're on Social Networks.Follow us & get in touch",
		reply_markup = reply_markup
	)
	return D

def facebook(update,context):
	context.bot.send_message(chat_id=update.effective_chat.id,text="https://www.facebook.com/adamaastu/",parse_mode=ParseMode.HTML)
def web(update,context):
	context.bot.send_message(chat_id=update.effective_chat.id,text="http://www.astu.edu.et/",parse_mode=ParseMode.HTML)
def email(update,context):	
	context.bot.send_message(chat_id=update.effective_chat.id,text="irccd@astu.edu.et",parse_mode=ParseMode.HTML)
def phone(update,context):
	query=update.callback_query
	context.user_data['message_id']=query.message.message_id
	context.bot.edit_message_text(chat_id=query.message.chat_id,message_id= query.message.message_id,text="International Relations and Corporate Communications\nOffice: +251 -22-211-3961\n\n Office of Registrar \n Office: +251 -221-100001")
	
	


def question(update,context):
	query=update.callback_query
	context.user_data['message_id']=query.message.message_id
	context.bot.edit_message_text(chat_id=query.message.chat_id,message_id= query.message.message_id,text="you can ask what you want about astu")
	

def school(update,context):
	query =update.callback_query
	context.user_data['message_id']=query.message.message_id
	with open('about.json') as f:
		data = json.load(f)
	mess = "".join(data['about'])
	keyboard=[
		[InlineKeyboardButton("School of Applied Natural Sciences", callback_data='applied')],
		[InlineKeyboardButton("School of Civil Engineering and Architecture", callback_data='civil')],
		[InlineKeyboardButton("School of Electrical Engineering and Computing", callback_data='electrical')],
		[InlineKeyboardButton("School of Mechanical Chemical and Materials Engineering", callback_data='mechanical')]
	]
	reply_markup=InlineKeyboardMarkup(keyboard)

	context.bot.edit_message_text(
		chat_id=query.message.chat_id,
		message_id = query.message.message_id,
		text = mess + "\nchoose:" ,
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
			InlineKeyboardButton("Undergrauate", callback_data="Undergrauat"),
			InlineKeyboardButton("Postgraduate", callback_data="Postgradat")
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

def Undergrauat(update, context):
	context.bot.send_document(chat_id = update.effective_chat.id, document =open('undergraduate.txt'))

def Postgradat(update,context):
	context.bot.send_document(chat_id= update.effective_chat.id, document=open('postgraduate.txt'))


def answer(update, context):
	text = update.message.text
	mess = botReact(text)
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
				CallbackQueryHandler(question,pattern = "^(question)$"),
				CallbackQueryHandler(contact,    pattern="^(contact)$")],

			B: [CallbackQueryHandler(Postgradat, pattern = "^(Postgradat)$"),
				CallbackQueryHandler(Undergrauat, pattern = "^(Undergrauat)$")],

			C: [CallbackQueryHandler(applied,    pattern= "^(applied)$"),
			    CallbackQueryHandler(civil,      pattern= "^(civil)$"),
			    CallbackQueryHandler(electrical, pattern= "^(electrical)$"),
			    CallbackQueryHandler(mechanical, pattern= "^(mechanical)$")],   
			D: [CallbackQueryHandler(facebook,   pattern="^(facebook)$"),
			 	CallbackQueryHandler(email,      pattern="^(email)$"),
				CallbackQueryHandler(web,        pattern="^(web)$"),
				CallbackQueryHandler(phone,       pattern="^(phone)$")
			]
		}, 
	 	fallbacks=[CommandHandler('start', welcome)],
	)

	dp.add_handler(con_handler)
	dp.add_handler(CommandHandler('start', welcome))
	dp.add_handler(MessageHandler(Filters.text, answer))
	updater.start_polling()
	updater.idle()


main()