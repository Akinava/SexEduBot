import json
import telebot


def parce_data(file_name):
    data = {}
    with open('data.json') as j:
        data = j.read()
    return json.loads(data)


def make_reply_markup(options):
    source_markup = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    source_markup_btns = []
    for v in options:
        source_markup_btns.append(telebot.types.KeyboardButton(v))
    source_markup.add(*source_markup_btns)
    return source_markup


start_markup = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
start_markup_btn1 = telebot.types.KeyboardButton('/start')
start_markup.add(start_markup_btn1)


data = parce_data('data.json')
bot = telebot.TeleBot(data['tocken'])


@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    chat_id = message.chat.id
    introduction = data.get('introduction')
    if not introduction is None:
        bot.send_message(message.chat.id, introduction)
    message.text = data['defoult']
    bot_response(message)


def bot_response(message):
    chat_id = message.chat.id
    text = message.text

    if not text in data.keys():
        bot.send_message(chat_id, data['wrong_menu'])
        text = data['defoult']

    responce_text = data[text].get('text', '')
    reply_markup = make_reply_markup(data[text].get('options'))

    message = bot.send_message(chat_id, responce_text, reply_markup=reply_markup)
    bot.register_next_step_handler(message, bot_response)


bot.polling()
