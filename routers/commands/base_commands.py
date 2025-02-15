from aiogram import Router, types, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.utils import markdown

from keyboards.common_keyboards import (
    ButtonText,
    get_on_start_keyboard,
    get_actions_keyboard,
)
from keyboards.inline_keyboards.info_kb import build_info_kb

router = Router(name=__name__)


@router.message(CommandStart())
async def handle_start(message: types.Message):

    print("command text:", repr(message.text))
    url = "https://e7.pngegg.com/pngimages/234/79/png-clipart-black-robot-face-illustration-robotics-technology-computer-icons-internet-bot-robotics-humanoid-robot-industrial-robot-thumbnail.png"
    await message.answer(
        text=f"{markdown.hide_link(url=url)}Hello, {markdown.hbold(message.from_user.full_name)}!",
        reply_markup=get_on_start_keyboard(),
    )


@router.message(F.text == ButtonText.WHATS_NEXT)
@router.message(Command("help"))
async def handle_help(message: types.Message):
    text = markdown.text(
        markdown.markdown_decoration.quote("I'm an echo bot."),
        markdown.text(
            "Send me",
            markdown.underline("literally"),
            markdown.bold("any"),
            markdown.markdown_decoration.quote("message!"),
        ),
        sep="\n",
    )
    await message.answer(
        text=text,
        parse_mode=ParseMode.MARKDOWN_V2,
    )


@router.message(Command("more"))
async def handle_more(message: types.Message):
    markup = get_actions_keyboard()
    await message.answer(
        text="Choose action:",
        reply_markup=markup,
    )


@router.message(Command("info", prefix="!/"))
async def handle_info(message: types.Message):

    await message.answer(
        text="Ссылки и прочие ресурсы:",
        reply_markup=build_info_kb(),
    )
