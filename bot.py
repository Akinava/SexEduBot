import telebot
import key
import markups as m


TOKEN = key.TOKEN
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    chat_id = message.chat.id
    bot.send_message(message.chat.id, 'Привет, я секс инстркутор')
    msg = bot.send_message(chat_id, 'Выбери тему', reply_markup=m.source_markup)
    bot.register_next_step_handler(msg, step_1)


def step_1(message):
    chat_id = message.chat.id
    text = message.text.lower()
    msg = bot.send_message(chat_id, 'Вы вели {}'.format(text))


bot.polling()
