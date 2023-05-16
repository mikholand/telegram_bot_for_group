import logging

import asyncpg

from config import pg_dsn

logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)


async def create_db():
    """Создание БД.

    Присоединение к БД и создание таблиц для нормального функционирования бота.
    """
    create_db_command = open("utils/create_db.sql", "r").read()

    logging.info("Connecting to database...")
    conn: asyncpg.Connection = await asyncpg.connect(dsn=pg_dsn)
    await conn.execute(create_db_command)
    await conn.close()
    logging.info("Table users created")


async def create_pool():
    """Подключение к БД.

    Стандартный пул для работы с БД.
    """
    logging.info("Create pool. Connecting to database...")
    return await asyncpg.create_pool(dsn=pg_dsn)
