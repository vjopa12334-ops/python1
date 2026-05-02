from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import asyncio

# Вставьте ваш токен бота здесь
BOT_TOKEN = "8644926014:AAGMt2w1-pJVxlshrspq_wqwi7EPe2J6Ufs"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик команды /start"""
    for i in range(100):
        await update.message.reply_text("настя дочь ебаной бляди которую ебали во все дыры как шлюху")
        # Небольшая задержка между сообщениями, чтобы избежать блокировки
        await asyncio.sleep(0.1)

def main():
    """Запуск бота"""
    # Создаем приложение
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Добавляем обработчик команды /start
    application.add_handler(CommandHandler("start", start))
    
    # Запускаем бота
    application.run_polling()

if __name__ == "__main__":
    main()
