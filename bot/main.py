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
    from bot.logic import (
        cesar_cipher,
        generate_password,
        generate_pin,
        is_strong_password,
    )
except ImportError:
    from logic import cesar_cipher, generate_password, generate_pin, is_strong_password


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


async def password(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Genera una password basata sul numero di parole fornito dall'utente."""
    if not update.message:
        return

    if not context.args:
        await update.message.reply_text("Inserisci la lunghezza (es. /password 5).")
        return

    try:
        num_words = int(context.args[0])
        pwd = generate_password(num_words)
        await update.message.reply_text(f"Password generata:\n{pwd}")
    except ValueError:
        await update.message.reply_text("Lunghezza non valida (minimo 4).")


async def check_password(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Verifica se la password inserita dall'utente e' considerata forte."""
    if not update.message:
        return

    if not context.args:
        await update.message.reply_text("Uso: /check <password>")
        return

    user_pwd = context.args[0]
    if is_strong_password(user_pwd):
        await update.message.reply_text("La password e' forte")
    else:
        await update.message.reply_text("La password e' debole")


async def pin(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Genera un PIN numerico della lunghezza desiderata (default 4)."""
    if not update.message:
        return

    length = 4
    if context.args:
        try:
            length = int(context.args[0])
        except ValueError:
            await update.message.reply_text("Inserisci un numero valido.")
            return

    res = generate_pin(length)
    await update.message.reply_text(f"Il tuo PIN: `{res}`", parse_mode="MarkdownV2")


async def encrypt(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Applica il cifrario di Cesare alla stringa fornita."""
    if not update.message or not context.args:
        if update.message:
            await update.message.reply_text("Uso: /encrypt <testo> <spostamento>")
        return

    text_to_encrypt = context.args[0]
    try:
        shift = int(context.args[1]) if len(context.args) > 1 else 3
        encrypted = cesar_cipher(text_to_encrypt, shift)
        await update.message.reply_text(
            f"Testo cifrato: `{encrypted}`", parse_mode="MarkdownV2"
        )
    except ValueError:
        await update.message.reply_text("Lo spostamento deve essere un numero intero.")


def main() -> None:
    """Configura e avvia il bot Telegram."""
    if not TOKEN:
        print("Errore: TELEGRAM_BOT_TOKEN non impostato.")
        return

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("password", password))
    app.add_handler(CommandHandler("check", check_password))
    app.add_handler(CommandHandler("pin", pin))
    app.add_handler(CommandHandler("encrypt", encrypt))

    app.run_polling()


if __name__ == "__main__":
    main()
