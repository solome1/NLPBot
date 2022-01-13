from telegram.ext import *
import random
API_KEY="5003371417:AAHY5M5l1BRepyt787fM45TC_4zWVcyQT7Q"


def start_command(update,context):
	update.massage.replay_text('welcome')


def chooes(update,context):
	update.message.replay_text('I can help you with the follwing')


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

	dp.add_handler(CommandHandler('start', start_command))
	dp.add_handler(MessageHandler(Filters.text, answer))
	dp.add_handler(chooes('start',chooes))
	updater.start_polling()
	updater.idle()


main() 