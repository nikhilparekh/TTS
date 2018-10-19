from gtts import gTTS

s = input("Enter Your Name: ")
tts = gTTS(text="Hello ! Welcome "+s, lang="en")
tts.save("sample.mp3")