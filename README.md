# Проект Telegram Бот для автоматической покупки/продажи коммерческой недвижимости
### Этот проект представляет собой Telegram бота, который осуществляет автоматическую покупку/продажу коммерческой недвижимости. Бот разработан на языке программирования Python с использованием базы данных SQLite и фреймворка aiogram для работы с Telegram API.

## Установка и настройка
Для установки и настройки проекта, выполните следующие шаги:

### Клонируйте репозиторий с помощью команды:

```
git clone https://github.com/Reyquazar/pyTelegramBotCommercialProperty.git
```
### Использование
```
python telegram_bot.py
```

После успешного запуска бот будет готов к использованию. Добавьте его в свой Telegram аккаунт и начните общение с ним.

### Бот поддерживает следующие команды:

/start - Начать общение с ботом.
/help - Вывести список доступных команд и их описание.
/buy - Осуществить покупку коммерческой недвижимости.
/sell - Осуществить продажу коммерческой недвижимости.
При выполнении команд /buy и /sell, бот будет запрашивать необходимую информацию для осуществления операции. Результаты операций будут сохранены в базе данных SQLite.

### Структура проекта

telegram_bot.py - Главный файл, содержащий код для запуска и настройки бота.
create_bot.py - Основной модуль бота, содержащий обработчики команд и логику взаимодействия с пользователем.
sqlite_db.py - Модуль для работы с базой данных SQLite.

