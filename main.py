# Код бота для бд крыша клиенсткая часть
import telebot

telebot.apihelper.proxy = {'https': 'socks5h://user:73758765@proxy.foxhub.ru:1080'}
bot = telebot.TeleBot("962512266:AAHvYRv83bBSQBY5uKSQKA-0mZ8wJe9Wv2A")
# Переменные
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Печати 📊', 'Кальяны 💨', 'Депозит 💰', 'Помощь 💡')


@bot.message_handler(commands=['start'])
def hellow_message(message):
	bot.send_message(message.chat.id, 'Привет, я твой личный помошник. Моя задача состиоит в том, чтобы ты всегда знал, сколько печатей и кальянов есть на твоем счету. Для продолжения, выбери соответсвующий пункт в меню снизу.', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_info(message):
	if message.text.lower() == 'печати 📊':
		bot.send_message(message.chat.id, 'Введите свой номер телефона, для получение данных')
	elif message.text.lower() == 'кальяны 💨':
		bot.send_message(message.chat.id, 'Введите свой номер телефона, для получение данных')
	elif message.text.lower() == 'депозит 💰':
		bot.send_message(message.chat.id, 'Введите свой номер телефона, для получение данных')
	elif message.text.lower() == 'помощь 💡':
		bot.send_message(message.chat.id, 'Я умею показывать колличесво печатей на твоей карточке, а также колличество бесплатных кальянов на твоём счету. Также, меня можно попросить показать остаток по твоему депозиту, если таковой имеется. Выбери соответствующий пунк в меню и мы начнем!')


bot.polling(none_stop = True)