import os
import re
from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("BOT_TOKEN")

async def delete_links(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.effective_message

    if not message or not message.text:
        return

    if re.search(r"https?://\S+|www\.\S+|t\.me/\S+", message.text, re.IGNORECASE):
        try:
            await message.delete()
        except Exception as e:
            print("Delete failed:", e)

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, delete_links))
    app.run_polling()

if __name__ == "__main__":
    main()
