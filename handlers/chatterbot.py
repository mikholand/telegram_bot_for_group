from aiogram import Dispatcher, types

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Костыль для запуска
import time
import collections.abc
time.clock = time.time
collections.Hashable = collections.abc.Hashable

# Инициализация и тренировка бота
chatbot = ChatBot("Ron Obvious")
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.russian')


async def run_chatterbot(message: types.Message):
    """Запуск Chatterbot.

    Запуск Chatterbot.
    """
    text = message.text
    if message.chat.type in ['group', 'supergroup']:
        if '!bot ' in text:
            response = chatbot.get_response(text.replace('!bot ', ''))
            # print(response)
            await message.answer(response)
        else:
            print(message)
    else:
        response = chatbot.get_response(text)
        await message.answer(response)


def register_chatterbot_handlers(dp: Dispatcher):
    """Регистрация обработчиков событий.

    Регистрирует все обработчики событий связанные с Chatterbot.
    """
    dp.register_message_handler(run_chatterbot)
