import os
from datetime import datetime, timedelta
from telegram import Update
from telegram.ext import (Application, MessageHandler,
                          ContextTypes, filters)
from Bad_words_collection import BAD_WORDS as bd

# Токен бота - і змінної оточення на Replit
# TOKEN = os.environ['TOKEN']
# Набір "поганих" слів, за які банимо
BAD_WORDS = bd
# Тривалість бану
BAN_DURATION = timedelta(seconds=60)

def is_violation(text: str) -> bool:
    # Перевіряємо, чи містить повідомлення заборонене слово
    lower = text.lower()
    return any(bad in lower for bad in BAD_WORDS)

async def moderate(update: Update,
                    context:ContextTypes.DEFAULT_TYPE):
    msg = update.effective_message
    text = msg.text or ""
    # Якщо порушень немає - нічого не робимо
    if not is_violation(text):
        return
    
    user = msg.from_user
    # Попереджувальний коментар у чаті
    await msg.reply_text(
        f"⛔ @{user.username or user.first_name}, порушили правила. Бан на 60 секунд!")
    # Банимо користувача
    await context.bot.ban_chat_member(
        chat_id=msg.chat_id,
        user_id=user.id,
        until_date=datetime.now() + BAN_DURATION
    )
def main():
    app = Application.builder().token(
        ""
    ).build()

    # Лише групи - фільтр ChatType.GROUPS
    app.add_handler(
        MessageHandler(
            filters.ChatType.GROUPS & filters.TEXT, moderate))
    app.run_polling()

if __name__ == "__main__":
    main()
