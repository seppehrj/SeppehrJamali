import gtts

my_text = "i am a programmer"

x = gtts.gTTS(my_text, lang="en", slow=False)
x.save("Season 8/voice.mp3")
