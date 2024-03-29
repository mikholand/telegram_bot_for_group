import os

from dotenv import load_dotenv

# Загрузка переменных и присвоение API-токена
load_dotenv('.env')
bot_token = os.getenv('BOT_API_TOKEN')
bot_username = os.getenv('BOT_USERNAME')
bot_admin_id = os.getenv('ADMIN_ID')

cur_token = os.getenv('CURRENCY_API_TOKEN')
weather_token = os.getenv('WEATHER_API_TOKEN')

pg_host = os.getenv('PG_HOST')
pg_user = os.getenv('PG_USER')
pg_pass = os.getenv('PG_PASS')
pg_db = os.getenv('PG_DB')

pg_dsn = f'postgresql://{pg_user}:{pg_pass}@{pg_host}/{pg_db}'

all_currency = ['AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG',
                'AZN', 'BAM', 'BBD', 'BDT', 'BGN', 'BHD', 'BIF', 'BMD', 'BND',
                'BOB', 'BRL', 'BSD', 'BTC', 'BTN', 'BWP', 'BYN', 'BYR', 'BZD',
                'CAD', 'CDF', 'CHF', 'CLF', 'CLP', 'CNY', 'COP', 'CRC', 'CUC',
                'CUP', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 'EGP', 'ERN',
                'ETB', 'EUR', 'FJD', 'FKP', 'GBP', 'GEL', 'GGP', 'GHS', 'GIP',
                'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 'HTG', 'HUF',
                'IDR', 'ILS', 'IMP', 'INR', 'IQD', 'IRR', 'ISK', 'JEP', 'JMD',
                'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KMF', 'KPW', 'KRW', 'KWD',
                'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LTL', 'LVL',
                'LYD', 'MAD', 'MDL', 'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MRO',
                'MUR', 'MVR', 'MWK', 'MXN', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO',
                'NOK', 'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR',
                'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RUB', 'RWF', 'SAR', 'SBD',
                'SCR', 'SDG', 'SEK', 'SGD', 'SHP', 'SLE', 'SLL', 'SOS', 'SRD',
                'STD', 'SVC', 'SYP', 'SZL', 'THB', 'TJS', 'TMT', 'TND', 'TOP',
                'TRY', 'TTD', 'TWD', 'TZS', 'UAH', 'UGX', 'USD', 'UYU', 'UZS',
                'VEF', 'VES', 'VND', 'VUV', 'WST', 'XAF', 'XAG', 'XAU', 'XCD',
                'XDR', 'XOF', 'XPF', 'YER', 'ZAR', 'ZMK', 'ZMW', 'ZWL']

questions = ['Какую музыку вы предпочитаете слушать на досуге?',
             'Какой вид спорта вам ближе всего?',
             'Какой цвет вам больше нравится?',
             'Какое время года вам нравится больше всего?',
             'Какой вид кухни вы предпочитаете?',
             'Какое животное вам больше всего нравится?',
             'Какую книгу вы читали недавно?',
             'Какое место вы предпочитаете посещать в свободное время?',
             'Какое время суток вам больше всего нравится?',
             'Какой вид транспорта вы предпочитаете?'
             ]

answers = [['Рок', 'Поп', 'Джаз', 'Классическая'],
           ['Футбол', 'Теннис', 'Хоккей', 'Баскетбол'],
           ['Красный', 'Синий', 'Зеленый', 'Желтый'],
           ['Весна', 'Лето', 'Осень', 'Зима'],
           ['Итальянская', 'Французская', 'Японская', 'Китайская'],
           ['Собака', 'Кошка', 'Лошадь', 'Рыба'],
           ['Детектив', 'Фантастика', 'Роман', 'Поэзия'],
           ['Кино', 'Театр', 'Клуб', 'Кафе'],
           ['Утро', 'День', 'Вечер', 'Ночь'],
           ['Машина', 'Велосипед', 'Пешком', 'Общественный транспорт']
           ]
