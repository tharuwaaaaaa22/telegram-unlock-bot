import telebot
import os
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

VIDEO_CHANNEL_ID = -1002844800834
VIDEO_MESSAGE_ID = 10  # Replace with actual message ID
MAIN_CHANNEL_LINK = "https://t.me/+1NwgRomSPlNjYTNl"

user_shares = {}

@bot.message_handler(commands=['start'])
def start_handler(message):
    chat_id = message.chat.id

    if chat_id not in user_shares:
        user_shares[chat_id] = []

    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("🔁 Unlock Video (0/3)", callback_data="unlock"))
    bot.send_message(chat_id, "🔒 Unlock the video by sharing this post to 3 different groups!", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == "unlock":
        chat_id = call.message.chat.id
        bot.send_message(chat_id,
            f"📢 Please forward this message to 3 different Telegram groups:

"
            f"🔥 LEAKED VIDEO 🔥
Watch full video only here!
👉 https://t.me/yourbot?start=unlock")

@bot.message_handler(content_types=['text'])
def forward_check(message):
    if message.forward_from_chat:
        user_id = message.from_user.id
        group_id = message.forward_from_chat.id

        if user_id not in user_shares:
            user_shares[user_id] = []

        if group_id not in user_shares[user_id] and message.chat.type in ['group', 'supergroup']:
            user_shares[user_id].append(group_id)
            count = len(user_shares[user_id])

            if count >= 3:
                bot.send_message(user_id, "✅ You've shared to 3 groups! Unlocking your video now...")
                bot.forward_message(user_id, VIDEO_CHANNEL_ID, VIDEO_MESSAGE_ID)
            else:
                bot.send_message(user_id, f"✅ Shared to {count}/3 groups. Keep going!")
        else:
            bot.send_message(user_id, "⚠️ This group was already counted or not valid.")

bot.polling()
