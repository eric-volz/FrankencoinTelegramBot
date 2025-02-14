from telegram import Update
from telegram.ext import ContextTypes

from adapters import FrankencoinAPIWrapper
from bot.methods.utils import Utils

""" Prices Methods """

class PricesMethods:

    @staticmethod
    async def zchf_fps(update: Update, context: ContextTypes.DEFAULT_TYPE):
        mint_token_price = FrankencoinAPIWrapper.get_mint_token_price()
        equity_token_price = FrankencoinAPIWrapper.get_equity_token_price()

        message = (
            "📊 *Current Token Prices*\n\n"
            f"*ZCHF*\n"
            f"CHF: {round(mint_token_price['chf'], 2)}\n"
            f"USD: {round(mint_token_price['usd'], 2)}\n\n"
            f"*FPS*\n"
            f"CHF: {round(equity_token_price['chf'], 2)}\n"
            f"USD: {round(equity_token_price['usd'], 2)}"
        )

        await Utils.send_msg(update, [message], None, True)

    @staticmethod
    async def collateral(update: Update, context: ContextTypes.DEFAULT_TYPE):
        collateral_price = FrankencoinAPIWrapper.get_collateral_tokens_prices()

        message = "💎 *Collateral Token Prices*\n\n"

        # Sortiere Tokens alphabetisch
        sorted_tokens = sorted(collateral_price.items())

        for token, prices in sorted_tokens:
            message += (
                f"*{token}*\n"
                f"CHF: {str(round(prices['chf'], 2))}\n"
                f"USD: {str(round(prices['usd'], 2))}\n\n"
            )

        await Utils.send_msg(update, [message], None, True)