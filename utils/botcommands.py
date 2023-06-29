from aiogram import types
from load_all import bot


async def set_commands():
    default_commands = [
        types.BotCommand(
            command='start',
            description='Запуск бота (помощь)'
        ),
        types.BotCommand(
            command='cancel',
            description='Отменить текущее действие'
        ),
        types.BotCommand(
            command='weather',
            description='Определить текущую погоду в определенном городе'
        ),
        types.BotCommand(
            command='currency',
            description='Конвертировать валюты'
        ),
        types.BotCommand(
            command='animals',
            description='Отправить случайную картинку с милыми животными'
        )
    ]

    all_group_commands = default_commands.copy()
    group_commands = [
        types.BotCommand(
            command='poll',
            description='Создать опрос в групповом чате'
        ),
        types.BotCommand(
            command='reg',
            description='Регистрация в игре "Красавчик дня"'
        ),
        types.BotCommand(
            command='hm_day',
            description='Собственно сам красавчик дня'
        ),
        types.BotCommand(
            command='hm_my_count',
            description='Моя статистика в игре'
        )
    ]
    for command in group_commands:
        all_group_commands.append(command)

    await bot.set_my_commands(default_commands, types.BotCommandScopeDefault())
    await bot.set_my_commands(default_commands, types.BotCommandScopeAllPrivateChats())
    await bot.set_my_commands(all_group_commands, types.BotCommandScopeAllGroupChats())
