from aiogram import Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.utils import markdown


router = Router(name=__name__)


@router.message(CommandStart())
async def handle_start(message: types.Message):
    url = "https://e7.pngegg.com/pngimages/234/79/png-clipart-black-robot-face-illustration-robotics-technology-computer-icons-internet-bot-robotics-humanoid-robot-industrial-robot-thumbnail.png"
    await message.answer(
        text=f"{markdown.hide_link(url=url)}Hello, {markdown.hbold(message.from_user.full_name)}!",
    )


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
