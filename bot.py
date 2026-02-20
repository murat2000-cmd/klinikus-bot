import telebot
from telebot import types
import os

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("🦴 Boyun", callback_data="boyun"),
        types.InlineKeyboardButton("🦾 Omuz", callback_data="omuz"),
        types.InlineKeyboardButton("🦵 Bel", callback_data="bel"),
        types.InlineKeyboardButton("🦿 Kalça", callback_data="kalca")
    )

    bot.send_message(
        message.chat.id,
        "👋 *Klinikus V2*\n\n"
        "Klinik testleri seçin:",
        reply_markup=markup,
        parse_mode="Markdown"
    )

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == "boyun":
        boyun_menu(call.message)
    else:
        bot.answer_callback_query(
            call.id,
            "Bu bölüm yakında eklenecek."
        )

def boyun_menu(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton("🔍 Klinik Testler", callback_data="boyun_testler"),
        types.InlineKeyboardButton("⚠️ Kırmızı Bayraklar", callback_data="boyun_kirmizi")
    )

    bot.edit_message_text(
        "🦴 *Boyun Bölgesi*",
        chat_id=message.chat.id,
        message_id=message.message_id,
        reply_markup=markup,
        parse_mode="Markdown"
    )

@bot.callback_query_handler(func=lambda call: call.data == "boyun_testler")
def boyun_testler(call):
    bot.send_message(
        call.message.chat.id,
        "📌 *Boyun Klinik Testleri*\n\n"
        "• Spurling Testi\n"
        "• Cervical Distraction\n"
        "• Cervical Rotation\n"
        "• Shoulder Abduction\n"
        "• Valsalva\n\n"
        "_Detaylar sırayla eklenecek._",
        parse_mode="Markdown"
    )

@bot.callback_query_handler(func=lambda call: call.data == "boyun_kirmizi")
def boyun_kirmizi(call):
    bot.send_message(
        call.message.chat.id,
        "⚠️ *Boyun – Kırmızı Bayraklar*\n\n"
        "• Travma öyküsü\n"
        "• Gece artan ağrı\n"
        "• Nörolojik defisit\n"
        "• Sistemik hastalık öyküsü",
        parse_mode="Markdown"
    )

bot.infinity_polling()
