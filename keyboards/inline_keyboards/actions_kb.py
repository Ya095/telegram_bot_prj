from random import randint

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters.callback_data import CallbackData


random_num_upd_cb_data = "random_num_upd_cb_data"


class FixedRandomNumCbData(CallbackData, prefix="fixed_random_num"):
    number: int


def build_action_kb(
    random_num_btn_text="Random number",
) -> InlineKeyboardMarkup:
    random_num_btn = InlineKeyboardButton(
        text=random_num_btn_text,
        callback_data=random_num_upd_cb_data,
    )
    cb_data1 = FixedRandomNumCbData(number=randint(1, 100))
    randint_num_btn = InlineKeyboardButton(
        text=f"Random num: {cb_data1.number}",
        callback_data=cb_data1.pack(),
    )
    hidden_random_num_btn = InlineKeyboardButton(
        text="Random num: [HIDDEN]",
        callback_data=FixedRandomNumCbData(number=randint(1, 100)).pack(),
    )

    rows = [
        [random_num_btn],
        [randint_num_btn],
        [hidden_random_num_btn],
    ]
    markup = InlineKeyboardMarkup(
        inline_keyboard=rows,
    )

    return markup
