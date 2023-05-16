from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from config import bot_username
from utils.dbcommands import DBCommands

database = DBCommands()


async def start(message: types.Message, state: FSMContext):
    """Стартовая функция.

    Закрывает все состояния, если они были, добавляет пользователя в БД
    и отправляет приветственное сообщение.
    """
    await state.finish()

    # Занесение пользователя в БД
    referral = message.get_args()
    await database.add_new_user(referral=referral)
    await database.add_new_chat()

    # Реферальная ссылка и текст сообщения при инициации бота или с помощью команд start или help
    user_id = message.from_user.id
    name = message.from_user.full_name
    bot_link = f'https://t.me/{bot_username}?start={user_id}'
    text = '''
Привет, {0}! Я бот, который может выполнить следующие функции:
1. /weather - Определить текущую погоду в определенном городе.
2. /currency - Конвертировать валюты.
3. /animals - Отправить случайную картинку с милыми животными.
4. /poll - Создать опрос в групповом чате.
5. /cancel или "Отмена" - Отменить текущее действие.

Ваша реферальная ссылка: {1}
'''
    # Добавляет дополнительные строчки для чатов
    if message.chat.type in ['group', 'supergroup']:
        text += '''
А также присутствуют команды для чатиков:
1. /reg - Регистрация в игре "Красавчик дня".
2. /hm_day - Собственно сам красавчик дня.
3. /hm_my_count - Моя статистика в игре.
'''
    await message.answer(text.format(name, bot_link))


async def cancel(message: types.Message, state: FSMContext):
    """Функция отмены.

    Закрывает все состояния, если они были и отправляет подтверждение прекращения действий.
    """
    await state.finish()
    await message.answer('Действие отменено', reply_markup=types.ReplyKeyboardRemove())


def register_common_handlers(dp: Dispatcher):
    """Регистрация обработчиков событий.

    Регистрирует все общие обработчики событий.
    """
    dp.register_message_handler(start, commands=['start', 'help'], state='*')
    dp.register_message_handler(cancel, commands=['cancel'], state='*')
    dp.register_message_handler(cancel, Text(equals='отмена', ignore_case=True), state='*')
