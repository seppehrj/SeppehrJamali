
import telebot

bot = telebot.TeleBot("7011020012:AAEV3n4j2nn_JDzbSXgGjX-AQBjM6fixVY4", parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "سلام🫰🏽 به ربات مستر سپهر خوش آمدید. چطور میتونم کمکتون کنم؟🤔👀")
	

bot.infinity_polling()