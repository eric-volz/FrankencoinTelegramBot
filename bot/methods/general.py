from telegram import Update
from telegram.ext import ContextTypes

from bot.logger import logger
from bot.buttons import MAIN_MARKUP

""" General Methods """

class GeneralMethods:

    @staticmethod
    async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
        logger.info(f"Start from {update.message.from_user.username}")

        welcome_message = """
🎉 Welcome to Frankencoin Bot! 🤖

- 🏦 Your gateway to the Frankencoin protocol:
- 📊 Monitor positions
- 💰 Check rates
- 🔔 Get notifications

Need help? Type /help 💡

Let's get started! 🚀
        """

        # Option 1: Send image from local file
        with open('../media/frankencoin_telegram_bot_logo_black.png', 'rb') as photo:
            await update.message.reply_photo(
                photo=photo,
                caption=welcome_message,
                reply_markup=MAIN_MARKUP
            )

    @staticmethod
    async def unknown_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        logger.info(f"Unknown command from {update.message.from_user.username}: {update.message.text}")

        unknown_message = """
❓ Oops! I don't know this command.

🔍 Try /help to see all available commands!

Or use the menu below 👇
        """

        await update.message.reply_text(
            text=unknown_message
        )