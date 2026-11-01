import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Halo! Gue VolixxtBot aktif. Ketik /help")

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Perintah: /warn (reply), @admin buat panggil admin")

async def handle_mention(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and "@admin" in update.message.text.lower():
        admins = await context.bot.get_chat_administrators(update.effective_chat.id)
        txt = "🚨 Panggilan admin: "
        for a in admins:
            if not a.user.is_bot:
                txt += f"@{a.user.username} " if a.user.username else f"{a.user.first_name} "
        await update.message.reply_text(txt)

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_mention))
    app.run_polling()

if __name__ == "__main__":
    main()
