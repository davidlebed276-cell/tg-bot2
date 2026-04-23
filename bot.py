from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

# =========================================
# НАСТРОЙКИ
# =========================================

TOKEN = "8699125376:AAFkgEplkoxNNACGH7xNRLT1TZxIb_i8fQ8"

# =========================================
# КНОПКИ
# =========================================

main_keyboard = ReplyKeyboardMarkup(
    [
        [KeyboardButton("📚 Курси"), KeyboardButton("💰 Ціна")],
        [KeyboardButton("✂️ З нуля"), KeyboardButton("❓ Підвищення")],
        [KeyboardButton("📞 Адміністратор")]
    ],
    resize_keyboard=True
)

courses_keyboard = ReplyKeyboardMarkup(
    [
        [KeyboardButton("✂️ Повний курс")],
        [KeyboardButton("🎨 Колористика"), KeyboardButton("✂️ Стрижки")],
        [KeyboardButton("⬅️ Назад")]
    ],
    resize_keyboard=True
)

# =========================================
# START
# =========================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привіт 💛 Обери що тебе цікавить 👇",
        reply_markup=main_keyboard
    )

# =========================================
# ТОЛЬКО КНОПКИ
# =========================================

async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "📚 Курси":
        await update.message.reply_text(
            "Оберіть курс 👇",
            reply_markup=courses_keyboard
        )

    elif text == "💰 Ціна":
        await update.message.reply_text(
            "💰 Ціни:\n\n"
            "✂️ Повний курс — 20 000 грн\n"
            "🎨 Колористика — 10 000 грн\n"
            "✂️ Стрижки — 10 000 грн",
            reply_markup=main_keyboard
        )

    elif text == "✂️ З нуля":
        await update.message.reply_text(
            "✂️ Повний курс з нуля\n18 занять + практика 💛",
            reply_markup=main_keyboard
        )

    elif text == "❓ Підвищення":
        await update.message.reply_text(
            "🔥 Підвищення кваліфікації\nAirTouch, складні техніки",
            reply_markup=main_keyboard
        )

    elif text == "📞 Адміністратор":
        await update.message.reply_text(
            "📞 Адміністратор з вами зв’яжеться 💛",
            reply_markup=main_keyboard
        )

    elif text == "✂️ Повний курс":
        await update.message.reply_text(
            "✂️ Повний курс:\n18 занять\n20 000 грн",
            reply_markup=main_keyboard
        )

    elif text == "🎨 Колористика":
        await update.message.reply_text(
            "🎨 Колористика:\n9 занять\n10 000 грн",
            reply_markup=main_keyboard
        )

    elif text == "✂️ Стрижки":
        await update.message.reply_text(
            "✂️ Стрижки:\n8 занять\n10 000 грн",
            reply_markup=main_keyboard
        )

    elif text == "⬅️ Назад":
        await update.message.reply_text(
            "Головне меню 👇",
            reply_markup=main_keyboard
        )

# =========================================
# ЗАПУСК
# =========================================

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_buttons))

    print("Бот запущений...")
    app.run_polling()

if __name__ == "__main__":
    main()