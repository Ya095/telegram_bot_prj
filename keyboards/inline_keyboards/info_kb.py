from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


random_site_cb_data = "random_site_cd_data"
random_num_dice_cb_data = "random_num_dice_data"


def build_info_kb() -> InlineKeyboardMarkup:
    tg_channel_btn = InlineKeyboardButton(
        text="📣 Канал",
        url="https://t.me",
    )
    source_code_btn = InlineKeyboardButton(
        text="🧑‍💻 Исходники бота",
        url="https://github.com/Ya095/telegram_bot_prj",
    )
    random_start_btn = InlineKeyboardButton(
        text="Random bot start",
        callback_data=random_site_cb_data,
    )
    random_num_btn = InlineKeyboardButton(
        text="🎲 Random Num",
        callback_data=random_num_dice_cb_data,
    )

    rows = [
        [tg_channel_btn],
        [source_code_btn],
        [random_start_btn, random_num_btn],
    ]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    return markup
