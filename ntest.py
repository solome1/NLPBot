from telegram.ext import  Updater, CommandHandler, MessageHandler, Filters 
import random
API_KEY="5003371417:AAHY5M5l1BRepyt787fM45TC_4zWVcyQT7Q"


def welcome(update,context):
	context.bot.send_message(chat_id=update.message.chat_id,text="welcom")



def response(text):
	if text in text in ["how are you", "heyy", "hi", "hello"]:
		arr = ["hello", "hi", "hi there", "good to see you", "nice to meet you"]
		rep = random.choice(arr)
	elif text in ["chaw", "bye", "good bye", "see you"]:
		arr = ["bye", "see you later", "bye bye", "chaw", "goodbye"]
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

	dp.add_handler(CommandHandler('start', welcome))
	dp.add_handler(MessageHandler(Filters.text, answer))
	updater.start_polling()
	updater.idle()


main()