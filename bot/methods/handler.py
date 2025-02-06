from telegram import Update
from telegram.ext import ContextTypes

from bot.logger import logger

""" General Methods """

class Handler:

    @staticmethod
    async def handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
        """
        This method incoming handles messages
        """
        logger.info(f"Message: {update.message.text} from {update.message.from_user.username}")