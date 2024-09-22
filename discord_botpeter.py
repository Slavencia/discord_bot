import discord
from logika_bota import gen_pass, gena, genadiy, genka
#from logika_bota import gena
#from logika_bota import genadiy 
#from logika_bota import genka 
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
    elif "Сделай мне пароль" in message.content:
       await message.channel.send(genka(8)) 
    elif "Сделай мне пароль из букв" in message.content:
       await message.channel.send(gena(8)) 
    elif "Замути мне пароль из цифр" in message.content:
       await message.channel.send(genadiy(8)) 
    elif "Сделай мне пароль из символов" in message.content:
       await message.channel.send(gen_pass(8))
    else:
        await message.channel.send(message.content)

    
    
client.run("")



#2 Часть logika_bota
import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password
#print("Приветсвую, это программа для регенирации паролей")




#сделать просто функцию 
def gena(pass_length):
    
    letter = "abcdefghijklnopqrstuvwxyz"
    password = ""
    for i in range(pass_length):
        password += random.choice(letter)
    return password

def genadiy(pass_length):
    
    numbers = "1234567890"
    password = ""
    for i in range(pass_length):
        password += random.choice(numbers)
    return password

def genka(pass_length):
    
    mix = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""
    for i in range(pass_length):
        password += random.choice(mix)
    return password
