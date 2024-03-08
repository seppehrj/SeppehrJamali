import telebot

bot = telebot.TeleBot("6560636516:AAE51x_zR8zmMzZavwX4r3qluaGqeEu0p1s", parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "سلام🫰🏽 به ربات مستر سپهر خوش آمدید. چطور میتونم کمکتون کنم؟🤔👀")
	

bot.infinity_polling()