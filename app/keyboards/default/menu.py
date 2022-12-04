from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='ПН'),
            KeyboardButton(text='ВТ'),
            KeyboardButton(text='СР'),
            KeyboardButton(text='ЧТ'),
            KeyboardButton(text='ПТ'),
            KeyboardButton(text='СБ'),
        ],
        [
            KeyboardButton(text='Сьогодні'),
            KeyboardButton(text='Зараз'),
            KeyboardButton(text='Завтра'),
            KeyboardButton(text='Ще')
        ]
    ],
    resize_keyboard=True)
