from dotenv import load_dotenv
load_dotenv()
import os
import discord
import requests
import speech_recognition
from pydub import AudioSegment

async def voc(message: discord.message.Message):
    data = requests.get(message.attachments[0].url)
    with open(str(message.id) + ".ogg", "wb") as file:
        file.write(data.content)
    AudioSegment.from_ogg(str(message.id) + ".ogg").export(str(message.id) + ".wav", format="wav")
    
    with speech_recognition.AudioFile(str(message.id) + ".wav") as source:
        r.adjust_for_ambient_noise(source, duration=0.2)
        audio = r.listen(source)
        msg = r.recognize_google(audio, language='fr-FR')
        os.remove(str(message.id) + ".ogg")
        os.remove(str(message.id) + ".wav")
        await message.channel.send(msg + " - " + str(message.author))

r = speech_recognition.Recognizer()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message: discord.message.Message):
    if message.author == client.user:
        return
    
    if(message.flags.voice):
        try:
            await voc(message)
        except speech_recognition.RequestError as e:
            print(e)
            await message.channel.send('Erreur de reconnaissance vocale')
        except speech_recognition.UnknownValueError as e:
            print(e)
            await message.channel.send('Erreur de reconnaissance vocale')

    if (message.content.startswith("dit coucou")):
        await message.channel.send('connard')
    
    if (message.content == "github"):
        await message.channel.send('https://github.com/huhulacolle/juli1/')
    

client.run(os.getenv('TOKEN'))