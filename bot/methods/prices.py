from telegram import Update
from telegram.ext import ContextTypes

from bot.config import config
from adapters.api import FrankencoinAPIWrapper
from adapters.blockchain import UniswapV3Wrapper
from bot.methods.utils import Utils

from bot.buttons import PRICES_MARKUP

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

        await Utils.send_msg(update, [message], PRICES_MARKUP, True)

    @staticmethod
    async def collateral(update: Update, context: ContextTypes.DEFAULT_TYPE):
        collateral_price = FrankencoinAPIWrapper.get_collateral_tokens_prices()

        message = "💎 *Collateral Token Prices*\n\n"
        sorted_tokens = sorted(collateral_price.items())

        for token, prices in sorted_tokens:
            message += (
                f"*{token}*\n"
                f"CHF: {str(round(prices['chf'], 2))}\n"
                f"USD: {str(round(prices['usd'], 2))}\n\n"
            )

        await Utils.send_msg(update, [message], PRICES_MARKUP, True)

    @staticmethod
    async def dex_zchf(update: Update, context: ContextTypes.DEFAULT_TYPE):
        pools: list = []
        network_names: list = []
        for network_identifier, pool_info in config.get_section("ZCHF_UNISWAP_V3_POOLS").items():
            pool_address = pool_info.split(",")[0]
            pools.append(UniswapV3Wrapper.get_pool(pool_address.lower()))
            network_names.append(config.get_section("NETWORK_NAMES")[network_identifier])

        message = "🇨🇭 *DEX ZCHF Prices*\n\n"
        for network_name, pool in zip(network_names, pools):
            price: float = round(pool.get_price(), 4)
            base_token: str = list(pool.tokens.keys())[pool.base_token_index]
            message += (
                f"*{network_name}*: {price} {base_token}\n"
            )

        await Utils.send_msg(update, [message], PRICES_MARKUP, True)

    @staticmethod
    async def dex_fps(update: Update, context: ContextTypes.DEFAULT_TYPE):
        pools: list = []
        network_names: list = []
        for network_identifier, pool_info in config.get_section("FPS_UNISWAP_V3_POOLS").items():
            pool_address = pool_info.split(",")[0]
            pools.append(UniswapV3Wrapper.get_pool(pool_address.lower()))
            network_names.append(config.get_section("NETWORK_NAMES")[network_identifier])

        message = "👥 *DEX FPS Prices*\n\n"
        for network_name, pool in zip(network_names, pools):
            price: float = round(pool.get_price(), 4)
            base_token: str = list(pool.tokens.keys())[pool.base_token_index]
            message += (
                f"*{network_name}*: {price} {base_token}\n"
            )

        await Utils.send_msg(update, [message], PRICES_MARKUP, True)