import os
from telegram import Update
from telegram.ext import Application, CommandHandler

TOKEN = os.environ["BOT_TOKEN"]

async def start(update: Update, context):
    await update.message.reply_text(
        "🔥 VIP MEMBERSHIP\n\n"
        "Price: KSh 100 / 7 days\n"
        "Pay via M-Pesa, then contact admin for approval.\n\n"
        "Commands:\n/status - Check membership"
    )

async def status(update: Update, context):
    await update.message.reply_text(
        "Contact admin to confirm your payment and VIP status."
    )

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("status", status))
app.run_polling()
