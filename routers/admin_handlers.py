from aiogram import Router, F, types
from config import settings

router = Router(name=__name__)


@router.message(
    F.from_user.id.in_(settings.admin_ids),
    F.text == "secret",
)
async def admin_msg(message: types.Message):
    await message.bot.send_message(
        text="Hi, admin",
        chat_id=message.chat.id,
    )
