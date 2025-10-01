// Конфигурация и инициализация Telegram WebApp
window.addEventListener('load', (event) => {
    const tg = window.Telegram.WebApp;

    // Инициализация WebApp
    tg.ready();
    tg.expand(); 
    tg.disableVerticalSwipes();

    // Применяем тему Telegram
    document.body.style.backgroundColor = tg.backgroundColor || '#faf8ef';

    // Сохраняем userId в localStorage
    const userId = tg.initDataUnsafe.user?.id;
    if (userId) {
        localStorage.setItem("userId", userId);
        console.log("User ID сохранен:", userId);

        // Сохраняем данные пользователя
        const user = tg.initDataUnsafe.user;
        localStorage.setItem("userInfo", JSON.stringify({
            id: user.id,
            first_name: user.first_name,
            last_name: user.last_name,
            username: user.username
        }));
    } else {
        console.error("User ID не найден в initDataUnsafe.");
    }

    // Настройка основной кнопки
    if (tg.MainButton) {
        tg.MainButton.setText("🎮 Новая игра");
        tg.MainButton.onClick(function() {
            if (window.gameManager) {
                window.gameManager.restart();
            }
        });
    }

    console.log("Telegram WebApp инициализован");
});

// Утилитарные функции для работы с Telegram
window.TelegramUtils = {
    // Получить ID пользователя
    getUserId: function() {
        return localStorage.getItem("userId");
    },

    // Получить информацию о пользователе
    getUserInfo: function() {
        const userInfo = localStorage.getItem("userInfo");
        return userInfo ? JSON.parse(userInfo) : null;
    },

    // Показать главную кнопку
    showMainButton: function(text, callback) {
        if (window.Telegram?.WebApp?.MainButton) {
            const mainButton = window.Telegram.WebApp.MainButton;
            mainButton.setText(text);
            mainButton.show();
            mainButton.onClick(callback);
        }
    },

    // Скрыть главную кнопку  
    hideMainButton: function() {
        if (window.Telegram?.WebApp?.MainButton) {
            window.Telegram.WebApp.MainButton.hide();
        }
    },

    // Показать уведомление
    showAlert: function(message) {
        if (window.Telegram?.WebApp?.showAlert) {
            window.Telegram.WebApp.showAlert(message);
        } else {
            alert(message);
        }
    },

    // Закрыть WebApp
    close: function() {
        if (window.Telegram?.WebApp?.close) {
            window.Telegram.WebApp.close();
        }
    }
};