import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../")))

# Load config
from bot.config import config
current_dir: str = os.path.dirname(__file__)
config.init(f"{current_dir}/config.ini")

# Load logger
from bot.logger import logger

# Load ENV
from dotenv import load_dotenv
load_dotenv(verbose=True)

logger.info("Initialized config dependencies...")

# Init and start FrankencoinTelegramBot
from bot.frankencoin_telegram_bot import FrankencoinTelegramBot
logger.info("Starting telegram bot...")
bot = FrankencoinTelegramBot(os.environ.get("TELEGRAM_TOKEN"))
bot.run()