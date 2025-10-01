# 🎮 Telegram 2048 MiniApp

Полнофункциональная игра 2048, интегрированная в Telegram MiniApp с использованием FastAPI и Aiogram 3.

## 🚀 Особенности

- ✨ Полноценная игра 2048 с анимациями
- 🤖 Telegram бот с inline клавиатурой  
- 📱 Адаптивный дизайн для мобильных устройств
- 🏆 Система рекордов и рейтинга игроков
- 💾 Автоматическое сохранение лучших результатов
- 🔄 Синхронизация с базой данных
- 📊 Страница лидеров

## 🛠 Технологии

- **Backend**: FastAPI + Aiogram 3
- **Database**: SQLAlchemy + Alembic + SQLite  
- **Frontend**: HTML5 + CSS3 + JavaScript
- **Integration**: Telegram WebApp API

## 📋 Установка

### 1. Клонирование и установка зависимостей

```bash
# Клонировать проект
git clone <repository-url>
cd telegram_2048_miniapp

# Создать виртуальное окружение
python -m venv venv

# Активировать виртуальное окружение
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Установить зависимости
pip install -r requirements.txt
```

### 2. Настройка Telegram бота

1. Создайте бота через [@BotFather](https://t.me/BotFather)
2. Получите токен бота
3. Настройте MiniApp:
   - Найдите вашего бота в Telegram
   - Перейдите в настройки бота
   - Configure MiniApp → Enable MiniApp
   - Укажите URL вашего приложения

### 3. Настройка окружения

Скопируйте `.env` и заполните переменные:

```bash
BOT_TOKEN=your_bot_token_here
ADMIN_IDS=[your_telegram_id]
BASE_SITE=https://your-domain.com
DB_URL=sqlite+aiosqlite:///./data/db.sqlite3
```

### 4. Инициализация базы данных

```bash
# Перейти в папку app
cd app

# Инициализировать Alembic
alembic init -t async migration

# Вернуться в корень
cd ..

# Переместить alembic.ini в корень и отредактировать
# Изменить: script_location = migration на script_location = app/migration

# Создать первую миграцию
cd app
alembic revision --autogenerate -m "Initial revision"

# Применить миграцию
alembic upgrade head
cd ..
```

### 5. Настройка туннеля для разработки

Для локальной разработки используйте ngrok:

```bash
# Установить ngrok
# Зарегистрироваться на https://ngrok.com

# Авторизоваться
ngrok config add-authtoken your_token

# Запустить туннель
ngrok http 8000
```

Скопируйте HTTPS URL из ngrok в переменную BASE_SITE в .env

### 6. Запуск приложения

```bash
# Запуск FastAPI сервера
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## 🎯 Использование

1. Запустите приложение
2. Откройте туннель ngrok
3. Настройте MiniApp в боте с URL из ngrok
4. Напишите `/start` вашему боту в Telegram
5. Используйте кнопки для запуска игры и просмотра рекордов

## 📱 Функциональность бота

- **🎮 Играть в 2048** - открывает игру в WebApp
- **🏆 Таблица лидеров** - показывает топ-20 игроков  
- **📈 Мой рекорд** - отображает ваш текущий ранг и счет

## 🔄 API Endpoints

- `GET /` - Главная страница с игрой
- `GET /records` - Страница с рекордами
- `PUT /api/bestScore/{user_id}` - Обновление лучшего счета
- `GET /api/user/{user_id}/rank` - Получение ранга пользователя
- `GET /api/top-scores` - Получение топ-20 игроков
- `POST /webhook` - Webhook для Telegram

## 🗃 Структура проекта

```
telegram_2048_miniapp/
├── .env                     # Переменные окружения
├── requirements.txt         # Python зависимости
├── app/
│   ├── bot/                 # Telegram бот
│   │   ├── create_bot.py    # Инициализация бота
│   │   ├── handlers/        # Обработчики команд
│   │   └── keyboards/       # Inline клавиатуры
│   ├── game/                # Логика игры и API
│   │   ├── models.py        # SQLAlchemy модели
│   │   ├── schemas.py       # Pydantic схемы
│   │   ├── dao.py           # Доступ к данным
│   │   └── router.py        # FastAPI роутеры
│   ├── static/              # Статические файлы
│   │   ├── js/             # JavaScript файлы
│   │   └── style/          # CSS файлы
│   ├── templates/           # HTML шаблоны
│   ├── config.py           # Конфигурация
│   ├── database.py         # Настройка БД
│   └── main.py             # Точка входа FastAPI
└── data/                   # SQLite база данных
```

## 🚀 Деплой на production

### Amvera Cloud

1. Зарегистрируйтесь на [Amvera Cloud](https://amvera.cloud)
2. Создайте новый проект
3. Загрузите код через Git или веб-интерфейс
4. Настройте переменные окружения
5. Запустите проект

### Docker (альтернатива)

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## 🤝 Разработка

### Добавление новых функций

1. Создайте новую ветку
2. Добавьте функционал
3. Создайте миграцию если нужно:
   ```bash
   cd app
   alembic revision --autogenerate -m "Description"
   alembic upgrade head
   ```
4. Протестируйте изменения
5. Создайте Pull Request

### Troubleshooting

**Проблема**: Бот не отвечает
- Проверьте токен бота в .env
- Убедитесь что webhook настроен правильно
- Проверьте логи приложения

**Проблема**: Не работает WebApp
- Проверьте BASE_SITE в .env  
- Убедитесь что ngrok туннель активен
- Проверьте настройки MiniApp в боте

**Проблема**: Ошибки базы данных
- Проверьте что миграции применены
- Убедитесь что папка data существует
- Проверьте права на запись

## 📄 Лицензия

MIT License - можете свободно использовать для личных и коммерческих проектов.

## 🙋‍♂️ Поддержка

Если у вас есть вопросы:
- Создайте Issue в GitHub
- Напишите в Telegram: @your_username

---

**Удачной игры! 🎮✨**
