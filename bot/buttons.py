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

ZCHF_FPS_BUTTON = "ZCHF / FPS"
COLLATERAL_BUTTON = "Collateral"

PRICES_MARKUP = ReplyKeyboardMarkup(
    [
        [KeyboardButton(ZCHF_FPS_BUTTON), KeyboardButton(COLLATERAL_BUTTON)],
        [KeyboardButton(BACK_BUTTON)]
    ],
    resize_keyboard=True
)