import openai
from telegram import Update
from telegram.ext import (Application, CommandHandler,
                           MessageHandler, ContextTypes,
                             filters)
# Додаємо API та Токен
openai.api_key = ''
TOKEN = ''
# Історія чату у вигляді словника
chat_histories = {}
# Обмеження на кількість повідомлень в пам'яті
max_history = 20

def update_history(chat_id, role, content):
    if chat_id not in chat_histories:
        chat_histories[chat_id] = []
    chat_histories[chat_id].append({"role": role, "content":content})
    # Якщо історія перевищує max_history, обрізати її до останніх записів
    if len(chat_histories[chat_id]) > max_history:
        chat_histories[chat_id] = chat_histories[chat_id][-max_history:]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привіт! Починаємо спілкування з моделлю від OpenAI. Напиши щось:")
    
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    user_text = update.message.text
    # Оновлюємо історію
    update_history(chat_id, "user", user_text)
    # Базова інструкція
    system_message = {"role": "system",
                "content": "Ти допоміжний бот, відповідаєш коротко та зрозуміло"}
    # Формуємо історію запиту
    if chat_id not in chat_histories or len(chat_histories[chat_id]) == 1:
        messages = [system_message] + chat_histories[chat_id]
    else:
        messages = [system_message] + chat_histories[chat_id]
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini", # Назва моделі
            messages=messages, # повідомлення
            max_tokens=150, # Максисальна кількість токенів відповіді моделі
            temperature=0.7) # Точність/креативність відповіді
        reply = response.choices[0].message.content.strip()
    except Exception as e:
        reply = f"Виникла помилка:{e}"
    update_history(chat_id, "assistant", reply)
    await update.message.reply_text(reply)

def main():                                   
    app = Application.builder().token(TOKEN).build()    

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.run_polling()

if __name__ == "__main__":
    main()