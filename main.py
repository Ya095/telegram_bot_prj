from config import settings
import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command
from aiogram.utils import markdown
from aiogram.enums import ParseMode, ChatAction
from aiogram.client.default import DefaultBotProperties


dp = Dispatcher()


@dp.message(CommandStart())
async def handle_start(message: types.Message):
    url = "https://e7.pngegg.com/pngimages/234/79/png-clipart-black-robot-face-illustration-robotics-technology-computer-icons-internet-bot-robotics-humanoid-robot-industrial-robot-thumbnail.png"
    await message.answer(
        text=f"{markdown.hide_link(url=url)}Hello, {markdown.hbold(message.from_user.full_name)}!",
    )


@dp.message(Command("help"))
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


@dp.message(Command("code", prefix="!"))
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


# def is_photo(message: types.Message):
#     return message.photo

filters_media = F.photo | F.video | F.document


# @dp.message(is_photo)
# @dp.message(F.photo, ~F.caption)
@dp.message(filters_media, ~F.caption)
async def handle_photo_wo_caption(message: types.Message):
    await message.bot.send_photo(
        chat_id=message.chat.id,
        photo=message.photo[-1].file_id,
    )
    # await message.reply("I can't understand msg!")
    caption = "I can't understand msg!"
    await message.reply_photo(
        photo=message.photo[-1].file_id,
        caption=caption,
    )


@dp.message(Command("pic"))
async def handle_pic_msg(message: types.Message):
    # url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTenp49lG3DDWsWxhb2eiwRcDXva9Cs1aG7hA&s"
    big_file = "media/220325case013.jpg"
    # file_path = "media/img_1.png"

    # await message.reply_photo(
    #     # photo=url,
    #     photo=types.FSInputFile(
    #         path=file_path,
    #         filename="cat_file.png",
    #     ),
    #     caption="Cat photo.",
    # )

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


@dp.message(F.from_user.id.in_({693795034}), F.text == "secret")
async def admin_msg(message: types.Message):
    await message.bot.send_message(
        text="Admin",
        chat_id=message.chat.id,
    )


@dp.message()
async def echo_msg(message: types.Message):
    await message.bot.send_message(
        chat_id=message.chat.id,
        text="Wait a second...",
        parse_mode=None,
    )
    await message.answer(
        text="Wait pls...",
        parse_mode=None,
    )
    if message.text:
        await message.answer(
            text=message.text,
            entities=message.entities,
            parse_mode=None,
        )

    try:
        # await message.send_copy(chat_id=message.chat.id)
        await message.forward(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text="Something new :)")


async def main():
    bot = Bot(
        token=settings.bot_token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    logging.basicConfig(level=logging.INFO)
    # проверка на новые события (в бесконечном цикле)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
