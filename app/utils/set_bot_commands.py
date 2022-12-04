from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand('b', 'Якщо зникли кнопки'),
        types.BotCommand('reset', 'Сброс настроек'),
        types.BotCommand('prepods', 'Рейтинг і розклад викладачів'),
        types.BotCommand('search', 'Розклад групи'),
    ])
