# A simple program to convert text to speech


from gtts import gTTS
tts = gTTS('Hello every one dev this side ', lang='en')
tts.save('hello.mp3')