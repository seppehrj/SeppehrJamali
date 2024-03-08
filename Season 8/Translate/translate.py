import gtts
import os


def read_from_file():
    global words_bank
    p = os.listdir("Season 8/Translate")
    if "Translate.txt" in p:
        f = open("Season 8/Translate/Translate.txt","r")
        temp = f.read().split("\n")
        words_bank = []
        for i in range(0, len(temp), 2):
            my_dict = {"en": temp[i], "fa": temp[i+1]}
            words_bank.append(my_dict)
        f.close()
        return words_bank
    else:
        print("Word bank not found")
        exit(0)
    


def show_menu():
    print('*************************************')
    print("Welcome to my Translate by seppehr")
    print("1- Translate English to Persian ")
    print("2- Translate Persian to English ")
    print("3- Add a new word to database ")
    print("4- Exit ")
    print('**************************************')


def en_voice(a):
    x = gtts.gTTS(a, lang="en", slow=False)
    x.save("Season 8/Translate/en_voice.mp3")


def fa_voice(a):
    x = gtts.gTTS(a, lang="ar", slow=False)
    x.save("Season 8/Translate/fa_voice.mp3")
    return x

def translate_en_sentence(user_main):
    user_en_text = user_main.split(".")
    o_en = ""
    for i in user_en_text:
        o_en = o_en + translate_en_to_fa(i) + "\n"
    return o_en

def translate_fa_sentence(user_main):
    user_fa_text = user_main.split(".")
    o_fa = ""
    for i in user_fa_text:
        o_fa = o_fa + translate_fa_to_en(i) + "\n"
    return o_fa

def translate_en_to_fa(user_en_text):
    user_words = user_en_text.split(" ")
    output = ""

    for user_word in user_words:
        for word in words_bank:
            if user_word == word["en"]:
                output = output + word["fa"] + " "
                break
        else:
            output = output + user_word + " "
    return output
    


def translate_fa_to_en(user_fa_text):
    user_words = user_fa_text.split(" ")
    output = ""

    for user_word in user_words:
        for word in words_bank:
            if user_word == word["fa"]:
                output = output + word["en"] + " "
                break
        else:
            output = output + user_word + " "
    return output


def add_new_word(en_word:str, fa_word:str):

    f = open("Season 8/Translate/Translate.txt",'a')
    f.write('\n')
    f.write(en_word + '\n')
    f.write(fa_word)
    f.close()


read_from_file()
while True:
    show_menu()
    choice = int(input("Enter your choice: "))

    if choice == 1:
        user_en_text = input("Enter your english text: ")
        print(translate_en_sentence(user_en_text))
        fa_voice(translate_en_sentence(user_en_text))

    if choice == 2:
        user_fa_text = input("Enter your Persian text: ")
        print(translate_fa_sentence(user_fa_text))
        en_voice(translate_fa_sentence(user_fa_text))

    if choice == 3:
        en = input("Enter your en word: ")
        fa = input("Enter your fa word: ")
        add_new_word(en,fa)
        print("Word added successfully")

    if choice == 4:
        exit(0)