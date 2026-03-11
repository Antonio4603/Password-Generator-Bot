"""
Modulo principale per l'esecuzione del Bot Telegram.

Questo modulo gestisce l'interazione con l'utente tramite comandi Telegram,
utilizzando le funzioni definite nel modulo logic.py.
"""

import os

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

try:
    from bot.logic import (cesar_cipher, generate_password, generate_pin,
                           is_strong_password)
except ImportError:
    from logic import (cesar_cipher, generate_password, generate_pin,
                       is_strong_password)


load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")


async def start(update: Update, _context: ContextTypes.DEFAULT_TYPE) -> None:
    """Invia il messaggio di benvenuto e la lista dei comandi disponibili."""
    if not update.message:
        return

    await update.message.reply_text(
        "Bot Generatore di Password\n\n"
        "Comandi:\n"
        "/password <numero_parole>\n"
        "/check <tua_password> - Verifica se la password e' sicura\n"
        "/pin <numero_cifre> - Genera un pin\n"
        "/encrypt <password, shift> - Applica il cifrario di Cesare"
    )

def main() -> None:
    """Configura e avvia il bot Telegram."""
    if not TOKEN:
        print("Errore: TELEGRAM_BOT_TOKEN non impostato.")
        return

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.run_polling()


if __name__ == "__main__":
    main()