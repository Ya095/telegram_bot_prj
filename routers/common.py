from aiogram import Router, types

router = Router(name=__name__)


@router.message()
async def echo_msg(message: types.Message):
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
