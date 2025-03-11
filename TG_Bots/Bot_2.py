import openai
from telegram import Update
from telegram.ext import (Application, CommandHandler,
                           MessageHandler, ContextTypes,
                             filters)

openai.api_key = ''


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["history"] = [{
        "role": "system",
        "content":"You are a helpful assistant."}]
    await update.message.reply_text(
        "Привіт! Починаємо спілкування з моделлю від OpenAI. Напиши щось:")

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text.strip()
    history = context.user_data.get("history", [])
    history.append({"role": "user", "content": user_input})
    try:
        response = await openai.ChatCompletion.acreate(
            model="gpt-4o-mini",
            messages=history)
        reply = response.choices[0].message.content.strip()
        history.append({"role": "user", "content": reply})
    except Exception as e:
        await update.message.reply_text(f"Виникла помилка: {e}")

def main():
    TOKEN = ''
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))

    app.run_polling()

if __name__ == "__main__":
    main()
