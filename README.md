# handsome_man
Telegram Bot for random identification of a handsome man in a chat. <br><br>
Телеграм бот для рандомного определения красавчика в чате. <br>
Сделан исключительно 4fun. Можно дополнять другими номинациями.

## Запуск бота
- установить Python 3.9 с [официального сайта](https://www.python.org/)
- установить Aiogram и gspread с помощью команд:
```
pip install -U aiogram
pip install gspread
```
- изменить файл `config.py`
  - подставить в `TOKEN` свое значение Bot API, которое нужно получить у бота @BotFather
  - подставить в `SHEET` свою таблицу
- запустить самого бота 
```
python bot_handsome_man.py
```

## Подключение таблицы Google(БД) к боту
1. Перейдите в [Google Developers Console](https://console.developers.google.com/) и создайте новый проект (или выберите тот, который у вас уже есть).
2. В поле [«Search for APIs and Services»](https://console.cloud.google.com/apis/library) найдите «Google Drive API» и включите его.
3. В поле [«Search for APIs and Services»](https://console.cloud.google.com/apis/library) найдите «Google Sheets API» и включите его.
4. Перейдите в «APIs & Services > Credentials» и выберите «Create credentials > Service account key».
5. Заполните форму
6. Нажмите «Create» и «Done».
7. Нажмите «Manage service accounts» в строке «Service Accounts».
8. Нажмите на ⋮ рядом с недавно созданной учетной записью службы и выберите «Manage keys», а затем нажмите «ADD KEY > Create new key».
9. Выберите тип ключа JSON и нажмите «Create».
10. Будет скачан файл следующего вида:
```
{
    "type": "service_account",
    "project_id": "api-project-XXX",
    "private_key_id": "2cd … ba4",
    "private_key": "-----BEGIN PRIVATE KEY-----\nNrDyLw … jINQh/9\n-----END PRIVATE KEY-----\n",
    "client_email": "473000000000-yoursisdifferent@developer.gserviceaccount.com",
    "client_id": "473 … hd.apps.googleusercontent.com",
    ...
}
```
11. Перейдите к своей электронной таблице и поделитесь ею с "client_email" из шага выше. Точно так же, как и с любой другой учетной записью Google. Если вы этого не сделаете, вы получите исключение "gspread.exceptions.SpreadsheetNotFound" при попытке доступа к этой электронной таблице из вашего приложения или скрипта.
12. Переместите загруженный файл в ./gspread/service_account.json.
