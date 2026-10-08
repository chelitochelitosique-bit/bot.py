import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN", "PON_AQUI_TU_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID", "0"))
WALLETS = {"TRC20": "TYXmu5hwqHYagZXiiBgck6wQ2h5zy1orqh", "BEP20": "0x534B089022849C1a8664599050271F6e6DCf5A7e", "PAYPAL": "tu_paypal@email.com"}
COMMISSIONS = {1: 0.10, 2: 0.05, 3: 0.02}

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    referrer_id = None
    if context.args and context.args[0].isdigit():
        referrer_id = int(context.args[0])
        if referrer_id == user_id:
            referrer_id = None
    welcome = f"Hola {update.effective_user.first_name} 👋\n\n💎 MT ECOSYSTEM\n💳 Deposito: 1 USDT\nTRC20: {WALLETS['TRC20'][:6]}... \nBEP20: {WALLETS['BEP20'][:6]}... \n👥 Referidos: 10%/5%/2%\n\nTu link:\nhttps://t.me/{context.bot.username}?start={user_id}"
    keyboard = [[InlineKeyboardButton("🚀 Abrir MT App", web_app=WebAppInfo(url="https://mt-ecosystem.vercel.app"))]]
    await update.message.reply_text(welcome, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

async def wallets_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"💰 MT Wallets:\nTRC20:\n`{WALLETS['TRC20']}`\n\nBEP20:\n`{WALLETS['BEP20']}`", parse_mode="Markdown")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("wallets", wallets_cmd))
    print("MT iniciado")
    app.run_polling()
if __name__ == "__main__":
    main()
