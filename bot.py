import telebot
import os

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(
        message,
        "👋 Kliniküs V2\n\n"
        "🦴 Boyun\n"
        "🦾 Omuz\n"
        "🦵 Bel\n"
        "🦿 Kalça\n\n"
        "Kanıta dayalı klinik testler yakında burada."
    )

bot.infinity_polling()