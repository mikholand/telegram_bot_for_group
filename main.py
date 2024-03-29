import logging

from aiogram import Dispatcher, executor

import handlers
from load_all import dp
from utils import set_commands

logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)


def register_handlers(dp: Dispatcher):
    """Регистрация хендлеров.

    Функция, которая регистрирует все хендлеры.
    """
    handlers.register_common_handlers(dp)
    handlers.register_animals_handlers(dp)
    handlers.register_currency_handlers(dp)
    handlers.register_handsome_man_handlers(dp)
    handlers.register_polls_handlers(dp)
    handlers.register_weather_handlers(dp)

    handlers.register_chatterbot_handlers(dp)
    handlers.register_test_handlers(dp)


async def on_startup(dp):
    await set_commands()


# Регистрация всех обработчиков событий
register_handlers(dp)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
