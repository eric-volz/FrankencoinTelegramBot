from telegram import Update
from telegram.ext import ContextTypes

from bot.logger import logger

""" General Methods """

class GeneralMethods:

    @staticmethod
    async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
        logger.info(f"Start from {update.message.from_user.username}")

        await update.message.reply_text('Welcome to the Frankencoin-Telegram-Bot')