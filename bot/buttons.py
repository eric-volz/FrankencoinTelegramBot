from telegram import ReplyKeyboardMarkup, KeyboardButton


NEXT_BUTTON = "➡️ Next"
BACK_BUTTON = "⬅️ Back"

""" MAIN MENU """

PRICES_BUTTON = "Prices"
ALERTS_BUTTON = "Alerts"
STATISTICS_BUTTON = "Statistics"
SETTINGS_BUTTON = "Settings"

MAIN_MARKUP = ReplyKeyboardMarkup(
    [
        [KeyboardButton(PRICES_BUTTON), KeyboardButton(ALERTS_BUTTON)],
        [KeyboardButton(STATISTICS_BUTTON), KeyboardButton(SETTINGS_BUTTON)]
    ],
    resize_keyboard=True
)

""" PRICES """

ZCHF_FPS_BUTTON = "ZCHF | FPS Mainnet"
COLLATERAL_BUTTON = "Collateral Oracles"
DEX_ZCHF_BUTTON = "DEX ZCHF"
DEX_FPS_BUTTON = "DEX FPS"

PRICES_MARKUP = ReplyKeyboardMarkup(
    [
        [KeyboardButton(ZCHF_FPS_BUTTON), KeyboardButton(COLLATERAL_BUTTON)],
        [KeyboardButton(DEX_ZCHF_BUTTON), KeyboardButton(DEX_FPS_BUTTON)],
        [KeyboardButton(BACK_BUTTON)]
    ],
    resize_keyboard=True
)