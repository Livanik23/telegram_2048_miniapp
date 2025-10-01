@echo off
echo 🚀 Установка Telegram 2048 MiniApp...

REM Проверка Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python не найден. Пожалуйста, установите Python 3.8+
    pause
    exit /b 1
)

echo ✅ Python найден

REM Создание виртуального окружения
echo 📦 Создание виртуального окружения...
python -m venv venv

REM Активация окружения
echo 🔄 Активация виртуального окружения...
call venv\Scripts\activate.bat

REM Обновление pip
echo ⬆️ Обновление pip...
python -m pip install --upgrade pip

REM Установка зависимостей
echo 📚 Установка зависимостей...
pip install -r requirements.txt

REM Создание папки данных
echo 📁 Создание папки для базы данных...
if not exist data mkdir data

echo ✅ Установка завершена!
echo.
echo 📝 Следующие шаги:
echo 1. Настройте .env файл с вашими данными
echo 2. Инициализируйте базу данных:
echo    cd app
echo    alembic revision --autogenerate -m "Initial"
echo    alembic upgrade head
echo    cd ..
echo 3. Запустите приложение:
echo    uvicorn app.main:app --reload
echo.
echo 🎉 Удачной разработки!
pause
