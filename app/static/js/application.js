// Точка входа в приложение 2048

// Запускаем игру когда DOM загружен
document.addEventListener("DOMContentLoaded", function() {
    window.requestAnimationFrame(function () {
        // Создаем экземпляр игры
        window.gameManager = new GameManager(4, KeyboardInputManager, HTMLActuator, LocalStorageManager);

        console.log("Игра 2048 запущена");
    });
});