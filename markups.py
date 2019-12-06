from telebot import types


start_markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
start_markup_btn1 = types.KeyboardButton('/start')
start_markup.add(start_markup_btn1)


source_markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
source_markup_btn1 = types.KeyboardButton('Секс практики')
source_markup_btn2 = types.KeyboardButton('ИППП')
source_markup_btn3 = types.KeyboardButton('Контроцепция')
source_markup.add(
        source_markup_btn1,
        source_markup_btn2,
        source_markup_btn3)
