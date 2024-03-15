from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from keyboards.keyboards import game_kb, yes_no_kb
from lexicon.lexicon_en import LEXICON_EN
from services.services import get_bot_choice, get_winner

router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    """Handler works on the command `/start`"""

    await message.answer(text=LEXICON_EN["/start"], reply_markup=yes_no_kb)


@router.message(Command(commands="help"))
async def process_help_command(message: Message):
    """Handler works on the command `/help`"""

    await message.answer(text=LEXICON_EN["/help"], reply_markup=yes_no_kb)


@router.message(F.text == LEXICON_EN["yes_button"])
async def process_yes_answer(message: Message):
    """Handle the user's approval to play the game"""

    await message.answer(text=LEXICON_EN["yes"], reply_markup=game_kb)


@router.message(F.text == LEXICON_EN["no_button"])
async def process_no_answer(message: Message):
    """Handle the user's refuse to play the game"""

    await message.answer(text=LEXICON_EN["no"])


@router.message(
    F.text.in_([LEXICON_EN["rock"], LEXICON_EN["paper"], LEXICON_EN["scissors"]])
)
async def process_game_button(message: Message):
    bot_choice = get_bot_choice()
    await message.answer(
        text=f'{LEXICON_EN["bot_choice"]}\n- {LEXICON_EN[bot_choice]} '
    )
    winner = get_winner(message.text, bot_choice)

    await message.answer(text=LEXICON_EN[winner], reply_markup=yes_no_kb)
