import random
import telebot
from telebot import types
from datetime import datetime
import jdatetime as jdate
from gtts import gTTS
import qrcode
import io

TOKEN = "7011020012:AAEV3n4j2nn_JDzbSXgGjX-AQBjM6fixVY4"
bot = telebot.TeleBot(TOKEN, parse_mode=None)

user_states = {}

keyboard = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
key_1 = types.KeyboardButton("استارت 🕸")
key_2 = types.KeyboardButton("گیم 🏀")
key_3 = types.KeyboardButton("سن 🧨")
key_4 = types.KeyboardButton("ویس 📢")
key_5 = types.KeyboardButton("مکس 🎩")
key_6 = types.KeyboardButton("ارگ مکس 📎")
key_7 = types.KeyboardButton("کیو ار کد 🧧")
key_8 = types.KeyboardButton("عکس 📸")
key_9 = types.KeyboardButton("دستور ها 🩸")
keyboard.add(key_1, key_2, key_3, key_4, key_5, key_6, key_7, key_8,key_9)

def start_game(chat_id):
    user_states[chat_id] = {"game": {"playing": True, "number": random.randint(1,100), "guesses": 0}}
    game_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    game_keyboard.add(types.KeyboardButton("ّبازی جدید ♦"))
    bot.send_message(chat_id, "بازی شروع شد! عددی را بین 1 تا 100 حدس بزنید.", reply_markup=game_keyboard)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"سلام {message.from_user.first_name}, به بات خوش آمدید☺, لطفا درخواست خود را از منو انتخاب کنید", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == "استارت 🕸")
def start_message(message):
    bot.send_message(message.chat.id, f"سلام {message.from_user.first_name}🎃, لطفا درخواست خود را از منو انتخاب کنید", reply_markup=keyboard)
@bot.message_handler(commands=['game'])
@bot.message_handler(func=lambda message: message.text == "گیم 🏀")
def handle_game_start(message):
    start_game(message.chat.id)

@bot.message_handler(func=lambda message: message.chat.id in user_states and "game" in user_states[message.chat.id] and user_states[message.chat.id]["game"]['playing'])
def handle_guess(message):
    chat_id = message.chat.id
    game_state = user_states[chat_id]["game"]
    guess = int(message.text) if message.text.isdigit() else None
    if guess is None:
        bot.send_message(chat_id, "لطفا یک شماره معتبر وارد کنید.")
        return

    game_state['guesses'] += 1

    if guess == game_state['number']:
        bot.send_message(chat_id, f"آفرین درسته✨, عدد تصادفی بود : {game_state['number']}, تعداد حدس: {game_state['guesses']}")
        game_state['playing'] = False
        bot.send_message(chat_id, "یک گزینه را از منو انتخاب کنید یا یک بازی جدید را شروع کنید.", reply_markup=keyboard)
    elif guess < game_state['number']:
        bot.send_message(chat_id, "برو بالا 🔼")
    else:
        bot.send_message(chat_id, "برو پایین 🔽")
@bot.message_handler(commands=['age'])
@bot.message_handler(func=lambda message: message.text == "سن 🧨")
def ask_for_birthdate(message):
    bot.send_message(message.chat.id, "لطفا تاریخ تولد خود را در شمسی وارد کنید. برای مثال (1379/5/11)")

@bot.message_handler(func=lambda message: "/" in message.text and len(message.text.split("/")) == 3)
def calculate_age(message):
    birthdate = message.text.split("/")
    birthdate = jdate.date(int(birthdate[0]), int(birthdate[1]), int(birthdate[2]))
    today = jdate.date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    bot.send_message(message.chat.id, f"شما {age} ساله هستید.")

@bot.message_handler(commands=['voice'])
@bot.message_handler(func=lambda message: message.text == "ویس 📢")
def ask_for_text(message):
    bot.send_message(message.chat.id, "لطفا برای من یک جمله به زبال انگلیسی برای تبدیل به صدا ارسال کنید / به طور مثال : v:hello im rich")

@bot.message_handler(func=lambda message: "v:" in message.text)
def text_to_voice(message):
    text_to_convert = message.text.replace('v:', '').strip()
    tts = gTTS(text_to_convert, lang='en')
    voice = io.BytesIO()
    tts.write_to_fp(voice)
    voice.seek(0)
    bot.send_voice(message.chat.id, voice)

@bot.message_handler(commands=['max',"argmax"])
@bot.message_handler(func=lambda message: message.text == "مکس 🎩" or message.text == "ارگ مکس 📎")
def ask_for_array(message):
    user_states[message.chat.id] = {"command": message.text}
    bot.send_message(message.chat.id, "لطفا فهرستی از اعداد را وارد کنید که با کاما از هم جدا شده اند, به عنوان مثال: (1,2,3...).")

@bot.message_handler(func=lambda message: "," in message.text and message.chat.id in user_states)
def handle_array_commands(message):
    command = user_states[message.chat.id].get("command")
    numbers = [int(n) for n in message.text.split(',') if n.isdigit()]
    if command == "مکس 🎩" or command == "/max":
        max_value = max(numbers)
        bot.send_message(message.chat.id, f"حداکثر عدد: {max_value}")
    elif command == "ارگ مکس 📎" or command == "/argmax":
        max_index = numbers.index(max(numbers))
        bot.send_message(message.chat.id, f"شاخص حداکثر عدد: {max_index+1}")

    if message.chat.id in user_states:
        del user_states[message.chat.id]

@bot.message_handler(commands=['qrcode'])
@bot.message_handler(func=lambda message: message.text == "کیو ار کد 🧧")
def ask_for_qr_data(message):
    bot.send_message(message.chat.id, " لطفا داده هایی را که می خواهید در یک کد کیو ار کد بزارید را برای من ارسال کنید. بطور مثال qr:im seppehr my age is 23")

@bot.message_handler(func=lambda message: "qr:" in message.text)
def generate_qr_code(message):
    data_for_qr = message.text.replace('qr:', '').strip()
    qr = qrcode.make(data_for_qr)
    img = io.BytesIO()
    qr.save(img, 'PNG')
    img.seek(0)
    bot.send_photo(message.chat.id, img)
    
@bot.message_handler(commands=['photo'])
@bot.message_handler(func=lambda message: message.text == "عکس 📸")
def random_photo(message):
    bot.send_message(message.chat.id, "ممکن است چند لحظه طول بکشد...")
    file = "C:/Users/Tec-9/Pictures/Saved Pictures/"
    random_photo = random.randint(1,3)
    photo_random = str(random_photo)
    photo_selected = file + photo_random + ".jpg"
    photo = open(photo_selected, "rb")
    bot.send_photo(message.chat.id, photo)
    bot.send_message(message.chat.id, "اینجا عکس تصادفی شماست.")

@bot.message_handler(commands=['help'])
@bot.message_handler(func=lambda message: message.text == "دستور ها 🩸")
def show_help(message):
    help_text = """
    /start × با نام کاربر احوال پرسی میکند
/game × یک بازی حدس زدن اعداد را شروع کنید
/age × سن خود را بر اساس تقویم شمسی (هجری شمسی) محاسبه کنید
/voice × تبدیل یک جمله به زبان انگلیسی به صدا
/max × حداکثر تعداد را در یک لیست پیدا کنید
/argmax × شاخص حداکثر تعداد را در یک لیست پیدا کنید
/qrcode × از متن ورودی یک کیو ار کد ایجاد کنید
/photo × شما می توانید یک عکس تصادفی داشته باشید
/help × این پیام راهنما را نشان دهید
    """
    bot.send_message(message.chat.id, help_text)

bot.infinity_polling()