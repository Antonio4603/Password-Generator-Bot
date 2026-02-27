from telegram import Update 
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from bot.logic import generate_password, is_strong_password, generate_pin, cesar_cipher

TOKEN="8658709912:AAG-OHzXA-tQfPXWHWXuOS-v1cMb-2fglrA"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Bot Generatore di Password\n\n"
        "Comandi:\n"
        "/password <numero_parole>\n"
        "/check <tua_password> - Verifica se la password è sicura\n"
        "/pin <numero_cifre> - Genera un pin\n"
        "/encrypt <password, shift> - Applica il cifrario di Cesare alla password"
    )

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()