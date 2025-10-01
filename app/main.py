import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from aiogram.types import Update

from app.bot.create_bot import bot, dp, stop_bot, start_bot
from app.bot.handlers.router import router as bot_router
from app.config import settings
from app.game.router import router as game_router

# Настраиваем логирование
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Управление жизненным циклом приложения"""
    logging.info("Запуск бота...")

    # Подключаем роутер бота
    dp.include_router(bot_router)

    # Запускаем бота
    await start_bot()

    # Устанавливаем вебхук
    webhook_url = settings.get_webhook_url()
    await bot.set_webhook(
        url=webhook_url,
        allowed_updates=dp.resolve_used_update_types(),
        drop_pending_updates=True
    )
    logging.info(f"Webhook установлен: {webhook_url}")

    yield

    # Завершение работы
    logging.info("Остановка бота...")
    await bot.delete_webhook()
    await stop_bot()
    logging.info("Webhook удален")

# Создаем приложение FastAPI
app = FastAPI(
    title="2048 Telegram MiniApp",
    description="Игра 2048 интегрированная в Telegram MiniApp",
    version="1.0.0",
    lifespan=lifespan
)

# Подключаем статические файлы
app.mount('/static', StaticFiles(directory='app/static'), name='static')

# Подключаем роутеры
app.include_router(game_router)

@app.post("/webhook")
async def telegram_webhook(request: Request) -> None:
    """Обработка вебхуков от Telegram"""
    logging.info("Получен запрос вебхука")
    update = Update.model_validate(await request.json(), context={"bot": bot})
    await dp.feed_update(bot, update)
    logging.info("Обновление обработано")

@app.get("/health")
async def health_check():
    """Проверка здоровья приложения"""
    return {"status": "healthy", "app": "2048 Telegram MiniApp"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
