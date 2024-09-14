import os
from dotenv import load_dotenv

load_dotenv()  # .env dosyasını yükler
token = os.getenv("7329291590:AAEB4lIPsI5wDHpv6c5SkvY5yeKJlifyF6g")
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Kullanıcı bilgilerini alıyoruz
    user = update.effective_user
    username = user.username if user.username else user.first_name

    # Kişisel karşılama mesajı
    welcome_message = f"Welcome {username}!"

    # Butonları tanımlıyoruz
    keyboard = [
        [
            InlineKeyboardButton("🚀Join Community 🚀",
                                 url='https://t.me/xton_community')
        ],
        [
            InlineKeyboardButton("💰 Payout Channel",
                                 url='https://t.me/xtonpayout')
        ],
        [InlineKeyboardButton("👤 Account", callback_data='button3')],
        [InlineKeyboardButton("👥 Refferals", callback_data='button4')],
        [InlineKeyboardButton("⚡ Upgrade", callback_data='button5')],
        [InlineKeyboardButton("💸 Withdraw", callback_data='button6')],
        [InlineKeyboardButton("🎉 History", callback_data='button7')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    # Kişisel karşılama mesajını ve butonları gönderiyoruz
    await update.message.reply_text(
        "Welcome to XTON. 🎉 It is a cloud mining where you can earn tons by inviting friends, upgrading and mining tons. XTON Isn't it time to earn?💎",
        reply_markup=reply_markup)


async def button_handler(update: Update,
                         context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()  # Kullanıcının butona tıklama işlemini onaylıyoruz

    # Butonların callback_data değerlerine göre mesajlar
    if query.data == 'button3':
        await query.message.reply_text("Buton 3'e bastınız. Bu bir mesajdır.")
    elif query.data == 'button4':
        await query.message.reply_text(
            "Buton 4'e bastınız. Bu bir başka mesajdır.")
    elif query.data == 'button5':
        await query.message.reply_text("Buton 5'e bastınız. Farklı bir mesaj.")
    elif query.data == 'button6':
        await query.message.reply_text("Buton 6'ya bastınız. Yeni bir mesaj.")
    elif query.data == 'button7':
        await query.message.reply_text("Buton 7'ye bastınız. Ekstra bir mesaj!"
                                       )
    else:
        await query.message.reply_text("Bilinmeyen bir komut!")


if __name__ == "__main__":
    app = ApplicationBuilder().token(
        "7329291590:AAEB4lIPsI5wDHpv6c5SkvY5yeKJlifyF6g").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    app.run_polling()
