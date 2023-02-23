import gspread
import random
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN, SHEET


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
gc = gspread.service_account(filename='gspread\service_account.json')
sh = gc.open_by_key(SHEET)

worksheet = sh.get_worksheet(0)


@dp.message_handler(commands=['reg'])
async def reg_player(message: types.Message):
    id = message.from_user.id
    first_name = message.from_user.first_name
    text = f'Спасибо за регистрацию, [{first_name}](tg://user?id={id})\!'
    text_answer = [f'[{first_name}](tg://user?id={id}), ты уже зарегистрировался\!', f'[{first_name}](tg://user?id={id}), сколько еще раз нажмешь?', f'[{first_name}](tg://user?id={id}), зачем два раза нажимать?']

    col1 = worksheet.col_values(1)
    chat_id = worksheet.col_values(2)
    match = 0

    for i in range(1, len(col1)):
        if col1[i] == str(message.from_user.id):
            if chat_id[i] == str(message.chat.id):
                match = 1
                row = i + 1
                break
    
    if match == 0:
        sh.values_update(
            'Лист1!A'+str(len(worksheet.get_all_values())+1),
            params={
                'valueInputOption': 'USER_ENTERED'
            },
            body={
                'values': [[message.from_user.id, message.chat.id, message.from_user.first_name, 0, 0, 1]]
            }
        )
        await message.reply(text=text, parse_mode='MarkdownV2')
    else:
        count_reg = int(worksheet.cell(row, 6).value) + 1
        worksheet.update_cell(row, 6, count_reg)
        text_reg = f'[{first_name}](tg://user?id={id}), ты ввел эту команду уже {count_reg} раз'
        await message.reply(text=text_answer[random.randint(0,2)], parse_mode='MarkdownV2')
        await message.reply(text=text_reg, parse_mode='MarkdownV2')


@dp.message_handler(commands=['handsome_man'])
async def handsome_man(message: types.Message):
    chat_id = worksheet.col_values(2)
    handsome_man_time = worksheet.col_values(5)
    count_members = chat_id.count(str(message.chat.id))
    count = 0
    row_members = []
    handsome_man_is = 0
    date = str(message.date)[0:10]

    for i in range(1, len(chat_id)):
        if chat_id[i] == str(message.chat.id):
            count += 1
            row_members.append(i)
            
    rnd = random.randint(1, count_members)
    
    for j in range(len(row_members)):
        if handsome_man_time[row_members[j]] == date:
            handsome_man_is = 1     # Сегодня уже был красавчик
            break
    
    if handsome_man_is == 1:
        id = worksheet.cell(row_members[j]+1, 1).value
        if worksheet.cell(row_members[j]+1, 3).value is None:
            name = 'Безымянный красавчик'
        else:
            name = worksheet.cell(row_members[j]+1, 3).value
        handsome_man = f'Сегодня у нас уже был красавчик \- [{name}](tg://user?id={id})\!'
        count_handsome_man = int(worksheet.cell(row_members[j]+1, 4).value)
        text_count = f'Он был красавчиком {count_handsome_man} раз!'
        await bot.send_message(chat_id=message.chat.id, text=handsome_man, parse_mode='MarkdownV2')
        await bot.send_message(chat_id=message.chat.id, text=text_count)
    else:
        winner = row_members[rnd-1]+1
        id = worksheet.cell(winner, 1).value
        if worksheet.cell(winner, 3).value is None:
            name = 'Безымянный красавчик'
        else:
            name = worksheet.cell(winner, 3).value
        handsome_man = f'Сегодня у нас красавчик \- [{name}](tg://user?id={id})\!'
        count_handsome_man = int(worksheet.cell(winner, 4).value) + 1
        worksheet.update_cell(winner, 4, count_handsome_man)
        text_count = f'Он был красавчиком {count_handsome_man} раз!'
        worksheet.update_cell(winner, 5, date)

        await bot.send_message(chat_id=message.chat.id, text='Крутим барабан!')
        await bot.send_message(chat_id=message.chat.id, text=handsome_man, parse_mode='MarkdownV2')
        await bot.send_message(chat_id=message.chat.id, text=text_count)




@dp.message_handler(commands=['test'])
async def test(message: types.Message):
    text = "Ооо, ты тоже тестировщик?"
    await bot.send_message(chat_id=message.chat.id, text=text)



if __name__ == '__main__':
    executor.start_polling(dp)