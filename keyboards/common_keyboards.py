from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    KeyboardButtonPollType,
)


class ButtonText:
    HELLO = "Hello"
    WHATS_NEXT = "What's next?"
    BYE = "Bye-bye"


def get_on_start_keyboard() -> ReplyKeyboardMarkup:
    """Добавление кнопок"""

    button_hello = KeyboardButton(text=ButtonText.HELLO)
    button_help = KeyboardButton(text=ButtonText.WHATS_NEXT)
    button_bye = KeyboardButton(text=ButtonText.BYE)
    first_row = [button_hello, button_help]
    second_row = [button_bye]
    # buttons_row = [button_hello, button_help]  # Кнопки друг за другом
    # markup = ReplyKeyboardMarkup(keyboard=[buttons_row])
    markup = ReplyKeyboardMarkup(
        keyboard=[first_row, second_row],
        resize_keyboard=True,
        # one_time_keyboard=True,
    )
    return markup


def get_actions_keyboard() -> ReplyKeyboardMarkup:
    location_btn = KeyboardButton(text="Send location", request_location=True)
    contact_btn = KeyboardButton(text="Send my phone", request_contact=True)
    poll_btn = KeyboardButton(text="Send poll", request_poll=KeyboardButtonPollType())
    bye_btn = KeyboardButton(text=ButtonText.BYE)

    markup = ReplyKeyboardMarkup(
        keyboard=[
            [location_btn, contact_btn],
            [poll_btn],
            [bye_btn],
        ],
        resize_keyboard=True,
    )

    return markup
