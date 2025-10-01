#!/bin/bash

echo "🚀 Установка Telegram 2048 MiniApp..."

# Проверка Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 не найден. Пожалуйста, установите Python 3.8+"
    exit 1
fi

echo "✅ Python найден"

# Создание виртуального окружения
echo "📦 Создание виртуального окружения..."
python3 -m venv venv

# Активация окружения
echo "🔄 Активация виртуального окружения..."
source venv/bin/activate

# Обновление pip
echo "⬆️ Обновление pip..."
pip install --upgrade pip

# Установка зависимостей
echo "📚 Установка зависимостей..."
pip install -r requirements.txt

# Создание папки данных
echo "📁 Создание папки для базы данных..."
mkdir -p data

echo "✅ Установка завершена!"
echo ""
echo "📝 Следующие шаги:"
echo "1. Настройте .env файл с вашими данными"
echo "2. Инициализируйте базу данных:"
echo "   cd app"
echo "   alembic revision --autogenerate -m 'Initial'"
echo "   alembic upgrade head"
echo "   cd .."
echo "3. Запустите приложение:"
echo "   uvicorn app.main:app --reload"
echo ""
echo "🎉 Удачной разработки!"
