# dev-bot
## Встановлення

Для початку, треба [створити бота за допомогою Botfather](https://core.telegram.org/bots#3-how-do-i-create-a-bot)

Через Botfather дозволяємо боту використовувати інлайн-режим: в Botfather вибираємо бота, далі Bot Settings, Inline Mode, Turn inline mode on

### Ubuntu

1. Встановимо git, якщо він ще не встановлений

```console
$ sudo apt install git -y
```

2. Встановимо docker-compose

```console
$ sudo apt install docker-compose -y
```

3. Склонуємо репозиторій бота

```console
$ git clone https://github.com/rdfsx/schedule_bot.git
```

4. Переходимо в папку з ботом

```console
$ cd schedule_bot
```

5. Створюємо файл .env, куди пропишемо дані для запуску, в тому числі токен що ми отримали задопомогою BotFather

```console
$ nano .env
```
Прописуємо:
```
ADMIN_ID=ваш id в telegram
BOT_TOKEN=токен бота
REDIS_HOST=localhost
REDIS_PORT=6379
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=localhost
POSTGRES_USER=postgres
POSTGRES_PASSWORD=пароль потрібно вигадати свій
```

## Використання

Запускаємо бота

```console
$ cd schedule_bot

$ sudo docker-compose up
```

Щоб завершити роботу бота, натисніть Ctrl+C в терміналі.
