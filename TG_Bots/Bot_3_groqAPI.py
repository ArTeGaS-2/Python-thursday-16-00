import httpx
from telegram import Update
from telegram.ext import (Application, CommandHandler,
                           MessageHandler, ContextTypes,
                             filters)

# Ключ API для Groqcloud
GROCLOUD_API_KEY = ''
# URL API Groqcloud - приклад, адаптуємо згідно з документацією.
GROCLOUD_ENDPOINT = 'https://api.groqcloud.com/v1/chat'

async def start(update: Update, context:ContextTypes.DEFAULT_TYPE):
    """
    Обробник команди /start.
    Ініціалізує історію діалогу для користувача та відправляє
    вітальне повідомлення.
    """
    context.user_data["history"] = [{"role": "system",
        "content":"Ти корисний асистент. Відповідаєш Українською."}]
    await update.message.reply_text(
        "Привіт! Починаємо спілкування. Напиши щось.")
async def chat(update: Update, context:ContextTypes.DEFAULT_TYPE):
    """
    Обробник текстових повідомлень.
    Додає повідомлення користувача до історії, надсилає запит
    до API Groqcloud та повертає відповідь.
    """
