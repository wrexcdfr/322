from time import sleep
from random import randint
import telebot
import sqlite3
from TOKEN import TOKEN
from telebot import types

'----------------------------------------------------------------'
BOT_TOKEN = TOKEN
bot = telebot.TeleBot(BOT_TOKEN)
'----------------------------------------------------------------'
conn = sqlite3.connect('database.db')
cursor = conn.cursor()
conn.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY
                    )''')
conn.commit()

'----------------------------------------------------------------'

cns = 50


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bttn1 = types.KeyboardButton("Меню")
    markup.add(bttn1)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Я бот-игра РУССКАЯ РУЛЕТКА.".format(
                         message.from_user), reply_markup=markup)

@bot.message_handler(commands=['game'])
def start(message):
    coins = cns

    if message.text == '1':
        bot.send_message(message.chat.id, text='Игра начинается')
        sleep(3)

        rand = randint(1, 6)

        bot.send_message(message.chat.id, text='Сейчас бот выбирает число между от 1 до 6.')
        sleep(2)
        bot.send_message(message.chat.id, text='Теперь ваш черед.')
        num = message.text(int)
        if num == rand:
            coins -= 5
            bot.send_message(message.chat.id,
                                 text='Вы проиграли и потеряли 5 монет. Ваш баланс: {coins}')
        elif num != rand:
            coins += 5
            bot.send_message(message.chat.id,
                                 text='Вы выиграли и получили 5 монет. Ваш баланс: {coins}')

    elif message.text == '2':
        bot.send_message(message.chat.id, text='Игра начинается')
        sleep(3)

        rand1 = randint(1, 6)
        rand2 = randint(rand1, 6)
        rand3 = randint(1, rand2)

        bot.send_message(message.chat.id, text='Сейчас бот выбирает 3 числа между от 1 до 6.')
        sleep(2)
        bot.send_message(message.chat.id, text='Теперь ваш черед.')
        num1 = message.text(int)
        if num1 == rand1 or rand2 or rand3:
            coins -= 15
            bot.send_message(message.chat.id,
                                     text='Вы проиграли и потеряли 15 монет. Ваш баланс: {coins}')
        elif num1 != rand1 or rand2 or rand3:
            coins += 15
            bot.send_message(message.chat.id,
                                     text='Вы выиграли и получили 15 монет. Ваш баланс: {coins}')


    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    bttn3 = types.KeyboardButton('2')
    bttn4 = types.KeyboardButton('1')
    markup.add(bttn4, bttn3)

    bot.send_message(message.chat.id, text='''Добро пожаловать в Русскую Рулетку
                    Правила игры указаны в комманде /info''', reply_markup=markup)

    bot.send_message(message.chat.id, text='''Пожалуйста, выберете сложность''')
    sleep(0.2)
    bot.send_message(message.chat.id,
                         text='''Первая сложность - проще выиграть, меньше ставка (5 монет)''')
                        
    sleep(0.2)
    bot.send_message(message.chat.id,
                         text='''Вторая сложность - сложнее выиграть, больше ставка (15 монет)''')

    

'----------------------------------------------------------------'


@bot.message_handler(content_types=['text'])
def fnc(message):
    coins = cns
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bttn2 = types.KeyboardButton("Информация о игре")
    bttn7 = types.KeyboardButton("Меню")
    bttn8 = types.KeyboardButton("Баланс")
    bttn9 = types.KeyboardButton('Начать игру')
    markup.add(bttn2, bttn7, bttn8, bttn9)
    if message.text == 'Меню':
        bot.send_message(message.chat.id, text='''Добро пожаловать в меню!
Все доступные команды 
/start 
Меню - вы находитесь здесь
Начать игру (/game) - начните игру
Баланс - узнайте свой баланс
Информация о игре - узнайте о игре
Бот был разработан пользователем @wrexcdfr''', reply_markup=markup)

    elif message.text == "Информация о игре":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bttn5 = types.KeyboardButton("Начать игру")
        bttn6 = types.KeyboardButton("Меню")
        markup.add(bttn5, bttn6)
        bot.send_message(message.chat.id, text=
        '''Правила русской рулетки просты. 
        Игра происходит на внутриигровую валюту
        Выбираете любое число от 1 до 6.
        Если это число не является таким же, какое выбрал бот, вы выигрываете в 2 раза больше валюты, чем поставили на игру.''')

        bot.send_message(message.chat.id, text='Ниже вы можете начать игру либо попасть в меню', reply_markup=markup)


    elif message.text == 'Баланс':
        bot.send_message(message.chat.id, text='Ваш баланс:')
        bot.send_message(message.chat.id, text=coins)


bot.infinity_polling()
