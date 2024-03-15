from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon_en import LEXICON_EN

# -------- Create keyboard with ReplyKeyboardBuilder --------

# Create Yes | No buttons
button_yes = KeyboardButton(text=LEXICON_EN["yes_button"])
button_no = KeyboardButton(text=LEXICON_EN["no_button"])

yes_no_kb_builder = ReplyKeyboardBuilder()

yes_no_kb_builder.row(button_yes, button_no, width=2)

yes_no_kb: ReplyKeyboardMarkup = yes_no_kb_builder.as_markup(
    one_time_keyboard=True, resize_keyboard=True
)

# -------- Create gameplay keyboard with ReplyKeyboardMarkup --------
button_1 = KeyboardButton(text=LEXICON_EN["rock"])
button_2 = KeyboardButton(text=LEXICON_EN["scissors"])
button_3 = KeyboardButton(text=LEXICON_EN["paper"])

game_kb = ReplyKeyboardMarkup(
    keyboard=[[button_1], [button_2], [button_3]], resize_keyboard=True
)
