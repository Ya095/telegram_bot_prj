import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command


bot_token = "6882998012:AAHkbFQsfwOZviV4OKX9GftN9IJmj54Qk7w"

dp = Dispatcher()


@dp.message(CommandStart())
async def handle_start(message: types.Message):
    await message.answer(text=f"Hello, {message.from_user.full_name}!")


@dp.message(Command("help"))
async def handle_help(message: types.Message):
    text = "I'm an echo bot.\nSend me any message!"
    await message.answer(text=text)


@dp.message()
async def echo_msg(message: types.Message):
    await message.bot.send_message(
        chat_id=message.chat.id,
        text="Wait a second..."
    )
    await message.answer(text="Wait pls...")

    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text="Something new :)")

    # if message.text:
    #     await message.reply(text=message.text)  # отвечает на конкретное сообщение
    # elif message.sticker:
    #     await message.bot.send_sticker(
    #         chat_id=message.chat.id,
    #         sticker=message.sticker.file_id,
    #     )
    # else:
    #     await message.reply(text="Something new :)")


async def main():
    bot = Bot(token=bot_token)
    logging.basicConfig(level=logging.INFO)
    # проверка на новые события (в бесконечном цикле)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
