# Код бота для бд крыша админ часть
import telebot

telebot.apihelper.proxy = {'https': 'socks5h://user:73758765@proxy.foxhub.ru:1080'}
bot = telebot.TeleBot("962512266:AAHvYRv83bBSQBY5uKSQKA-0mZ8wJe9Wv2A")
# Переменные
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Занести', 'Получить', 'Вычесть')
keyboard2 = telebot.types.ReplyKeyboardMarkup(True)
keyboard2.row('Номер', 'Печать', 'Депозит', 'Возврат')


@bot.message_handler(commands=['start'])
def hellow_message(message):
	bot.send_message(message.chat.id, 'Выбери раздел', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_info(message):
	if message.text.lower() == 'занести':
		bot.send_message(message.chat.id, 'Выбери операцию', reply_markup=keyboard2)
	elif message.text.lower() == 'получить':
		bot.send_message(message.chat.id, 'Выбери операцию', reply_markup=keyboard2)
	elif message.text.lower() == 'вычесть':
		bot.send_message(message.chat.id, 'Выбери операцию', reply_markup=keyboard2)
	elif message.text.lower() == 'возврат':
		bot.send_message(message.chat.id, 'Возвращаю в основное меню', reply_markup=keyboard1)
	elif message.text.lower() == 'номер':
		bot.send_message(message.chat.id, 'Введи номер для проведения операции')
	elif message.text.lower() == 'печать':
		bot.send_message(message.chat.id, 'Введи номер для проведения операции')
	elif message.text.lower() == 'депозит':
		bot.send_message(message.chat.id, 'Введи номер для проведения операции')
	

bot.polling(none_stop = True)