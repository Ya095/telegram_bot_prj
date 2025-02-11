import io

import aiohttp
from aiogram import Router, types
from aiogram.enums import ParseMode, ChatAction
from aiogram.filters import Command
from aiogram.utils import markdown
from aiogram.utils.chat_action import ChatActionSender

router = Router(name=__name__)


@router.message(Command("code", prefix="!"))
async def handle_command_code(message: types.Message):
    text = markdown.text(
        "Here's Python code:",
        "",
        markdown.markdown_decoration.pre_language(
            "print('Hello World!')",
            language="python",
        ),
        sep="\n",
    )
    await message.answer(
        text=text,
        parse_mode=ParseMode.MARKDOWN_V2,
    )


@router.message(Command("pic"))
async def handle_pic_msg(message: types.Message):
    big_file = "media/220325case013.jpg"

    # показываем, что происходит какое-то действие
    # (пока готовится большой файл)
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.UPLOAD_DOCUMENT,
    )

    # если изображение большое - отправить как файл
    await message.reply_document(
        document=types.FSInputFile(
            path=big_file,
            filename="cat_2.jpg"
        )
    )


@router.message(Command("text"))
async def text_file_handler(message: types.Message):
    file = io.StringIO()
    file.write("Hello world!\n")
    file.write("This is text file\n")
    await message.reply_document(
        document=types.BufferedInputFile(
            file=file.getvalue().encode(),  # вернет строку в байтах
            filename="text.txt",
        )
    )


@router.message(Command("pic_file"))
async def send_pic_file_buffered(message: types.Message):
    # долгий чат экшен
    file_sender = ChatActionSender(
        bot=message.bot,
        chat_id=message.chat.id,
        action=ChatAction.UPLOAD_DOCUMENT,
    )
    url = "https://www.cats.org.uk/media/13139/220325case013.jpg"

    async with file_sender:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, ssl=False) as response:
                result_bytes = await response.read()

        await message.reply_document(
            document=types.BufferedInputFile(
                file=result_bytes,
                filename="big-cat-f.jpeg",
            )
        )
