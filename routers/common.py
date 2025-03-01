from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove

from keyboards.common_keyboards import ButtonText

router = Router(name=__name__)


@router.message(F.text == ButtonText.BYE)
async def handle_bye_msg(message: types.Message):
    await message.answer(
        text="See you later!",
        reply_markup=ReplyKeyboardRemove(),
    )


@router.message(Command("cancel"))
@router.message(F.text.casefold() == "cancel")
async def cancel_handler(
    message: types.Message,
    state: FSMContext,
) -> None:
    """Allow user to cancel any action"""
    current_state = await state.get_state()
    if current_state is None:
        await message.reply(text="OK, but nothing was going on.")
        return

    await state.clear()
    await message.answer(
        text=f"Cancelled state: {current_state}.",
        reply_markup=ReplyKeyboardRemove(),
    )


@router.message()
async def echo_msg(message: types.Message):
    if message.poll:
        await message.forward(chat_id=message.chat.id)
        return

    await message.bot.send_message(
        chat_id=message.chat.id,
        text="Wait a second...",
        parse_mode=None,
    )

    # if message.text:
    #     await message.answer(
    #         text=message.text,
    #         entities=message.entities,
    #         parse_mode=None,
    #     )

    try:
        # await message.forward(chat_id=message.chat.id)
        await message.copy_to(
            chat_id=message.chat.id,
        )
    except TypeError:
        await message.reply(text="Something new :)")
