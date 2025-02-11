from aiogram import Router, F, types

router = Router(name=__name__)
filters_media = F.photo | F.video | F.document


@router.message(filters_media, ~F.caption)
async def handle_photo_wo_caption(message: types.Message):
    # await message.bot.send_photo(
    #     chat_id=message.chat.id,
    #     photo=message.photo[-1].file_id,
    # )

    caption = "I can't understand msg!"
    await message.reply_photo(
        photo=message.photo[-1].file_id,
        caption=caption,
    )
