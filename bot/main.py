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
    
async def password(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Inserisci la lunghezza.")
        return
    try:
        num_words=int(context.args[0])
        pwd=generate_password(num_words)
        await update.message.reply_text(f"Password generata:\n{pwd}")
    except ValueError:
        await update.message.reply_text("Lunghezza non valida (min 4).")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("password", password))
    app.run_polling()