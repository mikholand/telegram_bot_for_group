import random
from datetime import datetime

from aiogram import types
from asyncpg import Connection
from asyncpg.exceptions import UniqueViolationError

from load_all import db


class DBCommands:
    pool: Connection = db

    # SQL запросы
    ADD_NEW_USER_REFERRAL = 'INSERT INTO users(user_id, username, full_name, referral) ' \
                            'VALUES ($1, $2, $3, $4) RETURNING user_id'
    ADD_NEW_USER = 'INSERT INTO users(user_id, username, full_name) VALUES ($1, $2, $3) RETURNING user_id'
    ADD_NEW_CHAT = 'INSERT INTO chats(chat_id, title) VALUES ($1, $2) RETURNING chat_id'

    COUNT_USERS = 'SELECT COUNT(*) FROM users'
    # GET_ID = 'SELECT user_id FROM users WHERE user_id = $1'
    # CURRENT_DATE = 'SELECT current_date'

    REG_HANDSOME_MAN = "INSERT INTO handsome_man(user_id, chat_id, score, last_scored) VALUES ($1, $2, 0, '1970-01-01')"
    COUNT_HANDSOME_MAN = 'SELECT COUNT(*) FROM handsome_man WHERE chat_id=$1'
    GET_HANDSOME_MAN = '''
                        SELECT h.user_id, u.full_name, h.score
                        FROM handsome_man AS h
                        LEFT JOIN users AS u
                        ON u.user_id=h.user_id
                        WHERE h.chat_id=$1 AND h.last_scored=current_date
                       '''
    RND_HANDSOME_MAN = '''
                        SELECT h.user_id, u.full_name
                        FROM handsome_man AS h
                        LEFT JOIN users AS u
                        ON u.user_id=h.user_id
                        WHERE chat_id=$1
                        ORDER BY user_id OFFSET $2 LIMIT 1
                       '''
    SCORE_ADD = 'UPDATE handsome_man SET score=score+1, last_scored=current_date WHERE user_id=$1 AND chat_id=$2'
    SCORE_COUNT = 'SELECT score, last_scored FROM handsome_man WHERE user_id=$1 AND chat_id=$2'
    SCORE_DATE_LAST = 'SELECT last_scored FROM handsome_man WHERE chat_id=$1' \
                      'ORDER BY last_scored DESC LIMIT 1'
    SCORE_TEST = 'SELECT * FROM handsome_man'
    SCORE_TABLE = 'SELECT user_id, score FROM handsome_man WHERE chat_id=$1 ORDER BY score DESC LIMIT 5'

    async def add_new_user(self, referral=None):
        """Добавление нового пользователя в БД.

        Добавляет пользователя в БД.
        """
        user = types.User.get_current()

        user_id = user.id
        username = user.username
        full_name = user.full_name
        args = user_id, username, full_name

        if referral:
            args += (int(referral),)
            command = self.ADD_NEW_USER_REFERRAL
        else:
            command = self.ADD_NEW_USER

        try:
            user_id = await self.pool.fetchval(command, *args)
            return user_id
        except UniqueViolationError:
            pass

    async def add_new_chat(self):
        """Добавление нового чата в БД.

        Добавляет чат в БД.
        """
        chat = types.Chat.get_current()

        chat_id = chat.id
        chat_title = chat.title
        args = chat_id, chat_title

        command = self.ADD_NEW_CHAT

        try:
            chat_id = await self.pool.fetchval(command, *args)
            return chat_id
        except UniqueViolationError:
            pass

    async def count_users(self):
        """Подсчет пользователей в БД.

        Показывает сколько всего пользователей зарегистрированы в боте.
        """
        record = await self.pool.fetchval(self.COUNT_USERS)
        return record

    # async def get_id(self):
    #     command = self.GET_ID
    #     user_id = types.User.get_current().id
    #     return await self.pool.fetchval(command, user_id)

    async def reg_handsome_man(self):
        """Регистрация нового пользователя в игре.

        Добавляет пользователя в таблицу игры.
        """
        user = types.User.get_current()
        chat = types.Chat.get_current()

        user_id = user.id
        chat_id = chat.id
        args = user_id, chat_id

        command = self.REG_HANDSOME_MAN

        try:
            await self.pool.fetchval(command, *args)
            return 'Поздравляю! Ты добавлен в игру!'
        except UniqueViolationError:
            return 'Ты уже был добавлен'

    async def score_add(self):
        """Выбор красавчика дня.

        Проверяет, был ли сегодня красавчик дня и если нет, то выбирает его.
        """
        chat_id = types.Chat.get_current().id

        current_date = datetime.now().strftime("%Y-%m-%d")
        score_date_last = await self.pool.fetchval(self.SCORE_DATE_LAST, chat_id)

        if current_date != str(score_date_last):
            count_handsome_man = await self.pool.fetchval(self.COUNT_HANDSOME_MAN, chat_id)
            rnd = random.randint(0, count_handsome_man - 1)
            rnd_handsome_man = await self.pool.fetch(self.RND_HANDSOME_MAN, chat_id, rnd)
            rnd_hm_user_id = rnd_handsome_man[0][0]
            rnd_hm_full_name = rnd_handsome_man[0][1]
            command = self.SCORE_ADD
            await self.pool.fetchval(command, rnd_hm_user_id, chat_id)
            return 'Поздравляю, [{0}](tg://user?id={1})\\! Сегодня ты красавчик\\!'.format(rnd_hm_full_name, rnd_hm_user_id)
        handsome_man_now = await self.pool.fetch(self.GET_HANDSOME_MAN, chat_id)
        hm_user_id = handsome_man_now[0][0]
        hm_full_name = handsome_man_now[0][1]
        hm_score = handsome_man_now[0][2]
        return 'Сегодня уже был у нас красавчик и это \\- [{0}](tg://user?id={1})\\!\n' \
               'Это его {2} победа\\!'.format(hm_full_name, hm_user_id, hm_score)

    async def score_count(self):
        """Личная статистика красавчика дня.

        Отправляет сообщение в чат с личной статистикой - сколько раз был красавчиком дня и когда последний раз
        """
        user_id = types.User.get_current().id
        chat_id = types.Chat.get_current().id
        score_count = await self.pool.fetch(self.SCORE_COUNT, user_id, chat_id)
        score = score_count[0][0]
        last_score = score_count[0][1]
        return f'Ты был красавчиком {score} раз. В последний раз это было {last_score}'

    async def score_test(self):
        """Тестовая функция.

        Для разного рода тестов по игре.
        """
        # user_id = types.User.get_current().id
        chat_id = types.Chat.get_current().id
        test = await self.pool.fetch(self.SCORE_TABLE, chat_id)
        # score_count = await self.pool.fetchval(self.SCORE_COUNT, user_id, chat_id)
        # score_select = await self.pool.fetchval(self.SCORE_DATE_LAST, chat_id)
        print(test)
        # print(score_count)
        # print(score_select)
