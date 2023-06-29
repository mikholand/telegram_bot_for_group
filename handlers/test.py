from aiogram import Dispatcher, types

from config import bot_admin_id
from utils.dbcommands import DBCommands

database = DBCommands()


async def test(message: types.Message):
    """Секретная тестовая функция.

    Ничего из себя не представляет в общем и целом.
    """
    text = 'Ооо, ты тоже тестировщик?'
    await message.answer(text)


async def count_users(message: types.Message):
    """Количество всех юзеров в БД.

    Выводит количетсво юзеров в БД админу бота.
    """
    if message.from_user.id == int(bot_admin_id):
        count_users = await database.count_users()
        await message.answer(f'Сейчас в БД {count_users} юзеров')


async def test_contact(message: types.Contact):
    print(message)


async def all_handler(message: types.Message):
    """Обработчик всех сообщений.

    Тестовый обработчик всех сообщений.
    """
    print(message)


def register_test_handlers(dp: Dispatcher):
    """Регистрация обработчиков событий.

    Регистрирует все тестовые обработчики событий.
    """
    dp.register_message_handler(test, commands=['test'])
    dp.register_message_handler(count_users, commands=['count_users'])
    dp.register_message_handler(test_contact, content_types=types.ContentType.CONTACT)
    dp.register_message_handler(all_handler)
