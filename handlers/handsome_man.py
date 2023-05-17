from aiogram import Dispatcher, types

from utils.dbcommands import DBCommands

database = DBCommands()


async def reg_handsome_man(message: types.Message):
    """Функция регистрации в игре.

    Добавляет пользователя в БД и регистрирует в игре.
    """
    await database.add_new_user()
    text = await database.reg_handsome_man()
    await message.answer(text)


async def score_add(message: types.Message):
    """Выбор красавчика дня.

    Проверяет, был ли сегодня красавчик дня и если нет, то выбирает его.
    """
    text = await database.score_add()
    await message.answer(text, parse_mode='MarkdownV2')


async def score_count(message: types.Message):
    """Личная статистика красавчика дня.

    Отправляет сообщение в чат с личной статистикой - сколько раз был красавчиком дня и когда последний раз
    """
    text = await database.score_count()
    await message.answer(text)


async def score_top5(message: types.Message):
    """ТОП-5 игроков.

    Показывает статистику ТОП-5 участников игры в чате.
    """
    text = await database.score_top()
    await message.answer(text, parse_mode='MarkdownV2')


# async def score_test(message: types.Message):
#     """Тестовая функция.

#     Для разного рода тестов по игре.
#     """
#     await database.score_test()
#     await message.answer('Test')


def register_handsome_man_handlers(dp: Dispatcher):
    """Регистрация обработчиков событий.

    Регистрирует все обработчики событий игры "Красавчик дня".
    """
    dp.register_message_handler(reg_handsome_man, commands=['reg'])
    dp.register_message_handler(score_add, commands=['hm_day'])
    dp.register_message_handler(score_count, commands=['hm_my_count'])
    dp.register_message_handler(score_top5, commands=['hm_top5'])
    # dp.register_message_handler(score_test, commands=['score_test'])
