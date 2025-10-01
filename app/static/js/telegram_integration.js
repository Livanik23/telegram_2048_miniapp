// Интеграция игры 2048 с Telegram API

class TelegramIntegration {
    constructor() {
        this.userId = TelegramUtils.getUserId();
        this.apiBaseUrl = window.location.origin;
        this.isInitialized = false;
        this.init();
    }

    init() {
        if (!this.userId) {
            console.error("User ID не найден");
            return;
        }

        this.isInitialized = true;
        console.log("Telegram интеграция инициализирована для пользователя:", this.userId);

        // Подписываемся на события игры
        this.setupGameEventListeners();
    }

    setupGameEventListeners() {
        // Слушаем изменения счета
        document.addEventListener('scoreUpdated', (event) => {
            this.handleScoreUpdate(event.detail.score);
        });

        // Слушаем окончание игры
        document.addEventListener('gameOver', (event) => {
            this.handleGameOver(event.detail);
        });

        // Слушаем победу
        document.addEventListener('gameWon', (event) => {
            this.handleGameWon(event.detail);
        });
    }

    async handleScoreUpdate(score) {
        if (!this.isInitialized) return;

        try {
            // Отправляем счет на сервер
            await this.updateBestScore(score);
        } catch (error) {
            console.error("Ошибка при обновлении счета:", error);
        }
    }

    async updateBestScore(score) {
        const response = await fetch(`${this.apiBaseUrl}/api/bestScore/${this.userId}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ score: score })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        console.log("Счет обновлен:", data);
        return data;
    }

    async getUserRank() {
        try {
            const response = await fetch(`${this.apiBaseUrl}/api/user/${this.userId}/rank`);
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();
            return data;
        } catch (error) {
            console.error("Ошибка при получении ранга:", error);
            return null;
        }
    }

    async getTopScores() {
        try {
            const response = await fetch(`${this.apiBaseUrl}/api/top-scores`);
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();
            return data;
        } catch (error) {
            console.error("Ошибка при получении топ счетов:", error);
            return [];
        }
    }

    handleGameOver(gameData) {
        const finalScore = gameData.score;
        console.log("Игра окончена, финальный счет:", finalScore);

        // Показываем сообщение через Telegram API
        TelegramUtils.showAlert(`Игра окончена! Ваш счет: ${finalScore}`);

        // Показываем кнопку для новой игры
        TelegramUtils.showMainButton("🔄 Новая игра", () => {
            if (window.gameManager) {
                window.gameManager.restart();
            }
        });
    }

    handleGameWon(gameData) {
        const score = gameData.score;
        console.log("Игра выиграна! Счет:", score);

        // Показываем поздравление
        TelegramUtils.showAlert(`🎉 Поздравляем! Вы достигли 2048! Счет: ${score}`);

        // Можно продолжить игру или начать заново
        TelegramUtils.showMainButton("🎮 Продолжить", () => {
            TelegramUtils.hideMainButton();
        });
    }
}

// Инициализируем интеграцию когда страница загружена
document.addEventListener('DOMContentLoaded', function() {
    window.telegramIntegration = new TelegramIntegration();
});