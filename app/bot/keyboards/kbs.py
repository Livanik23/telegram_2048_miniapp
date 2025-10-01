from aiogram.types import InlineKeyboardMarkup, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder
from app.config import settings

def main_keyboard() -> InlineKeyboardMarkup:
    """Главная клавиатура"""
    kb = InlineKeyboardBuilder()
    kb.button(text="🎮 Играть в 2048", web_app=WebAppInfo(url=settings.BASE_SITE))
    kb.button(text="🏆 Таблица лидеров", web_app=WebAppInfo(url=f"{settings.BASE_SITE}/records"))
    kb.button(text="📈 Мой рекорд", callback_data="show_my_record")
    kb.adjust(1)
    return kb.as_markup()

def record_keyboard() -> InlineKeyboardMarkup:
    """Клавиатура для экрана рекордов"""
    kb = InlineKeyboardBuilder()
    kb.button(text="🎮 Играть в 2048", web_app=WebAppInfo(url=settings.BASE_SITE))
    kb.button(text="🏆 Посмотреть лидеров", web_app=WebAppInfo(url=f"{settings.BASE_SITE}/records"))
    kb.button(text="🔄 Обновить рекорд", callback_data="show_my_record")
    kb.adjust(1)
    return kb.as_markup()
