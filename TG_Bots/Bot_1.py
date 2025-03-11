from telegram.ext import (Application, CommandHandler,
                           MessageHandler, filters)

TOKEN = ''

async def start(update, context):
    await update.message.reply_text('Привіт! Я твій новий бот')

async def echo(update, context):
    await update.message.reply_text(update.message.text)

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT, echo))

    app.run_polling()

if __name__ == "__main__":
    main()
