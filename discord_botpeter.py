import discord
from logika_bota import gen_pass
from logika_bota import gena
from logika_bota import genadiy 
from logika_bota import genka 
# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('Как дела?'):
        await message.channel.send("Круто, работаю!")
    elif "Бот" in message.content:
        await message.channel.send("Опять я :( ")       
    elif "пароль из букв" in message.content:
       print("буквы")
       await message.channel.send(gena(8)) 
    elif "пароль из цифр" in message.content:
       print("цифры")
       await message.channel.send(genadiy(8)) 
    elif "пароль из символов" in message.content:
       print("символы")
       await message.channel.send(gen_pass(8))
    elif "пароль" in message.content:
       print("всё")
       await message.channel.send(genka(8))   
    else:
       await message.channel.send(message.content)

client.run("")
