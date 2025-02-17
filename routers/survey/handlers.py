from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import markdown

from routers.survey.states import Survey
from validators.email_validator import validate_email_filter

router = Router(name=__name__)


@router.message(Command("survey"))
async def handle_start_survey(
    message: types.Message,
    state: FSMContext,
):
    await state.set_state(Survey.full_name)  # ожидаем и записываем данные юзера
    await message.answer(
        "Welcome to our weekly survey!\n" "What's your name?",
        reply_markup=types.ReplyKeyboardRemove(),
    )


@router.message(Survey.full_name, F.text)
async def handle_survey_user_full_name(
    message: types.Message,
    state: FSMContext,
):
    await state.update_data(full_name=message.text)
    await state.set_state(Survey.email)
    await message.answer(
        f"Hello {markdown.hbold(message.text)}!\n" "Now pls share your email.",
    )


@router.message(Survey.full_name, F.text)
async def handle_survey_user_full_name_invalid_content_type(message: types.Message):
    await message.answer(
        "Sorry I couldn't understand. Send your full name as text.",
    )


@router.message(Survey.email, validate_email_filter)
async def handle_survey_email_msg(
    message: types.Message,
    state: FSMContext,
    email: str,
):
    await state.update_data(email=message.text)
    await state.set_state(Survey.email_newsletter)
    await message.answer(
        text=f"Cool, your email {markdown.hbold(email)}\n"
        "Would you like to be contacted in future?",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="yes"),
                    KeyboardButton(text="no"),
                ]
            ],
            resize_keyboard=True,
        ),
    )


@router.message(Survey.email)
async def handle_survey_email_msg(message: types.Message):
    await message.answer(
        text="Invalid email... Pls try again.",
    )


async def send_survey_results(message: types.Message, data: dict):
    """Получить данные из состояния"""

    print(data)

    text = markdown.text(
        "Your survey results:\n",
        markdown.text("Name:", markdown.hbold(data["full_name"])),
        markdown.text("Email:", markdown.hcode(data["email"])),
        (
            "Cool, we will send you our news!"
            if data["newsletter"]
            else "And we won't bother you again."
        ),
        sep="\n",
    )

    await message.answer(
        text,
        reply_markup=types.ReplyKeyboardRemove(),
    )


@router.message(Survey.email_newsletter, F.text.casefold() == "yes")
async def handle_survey_email_newsletter_ok(
    message: types.Message,
    state: FSMContext,
):
    data = await state.update_data(newsletter=True)
    await state.clear()
    await send_survey_results(message, data)


@router.message(Survey.email_newsletter, F.text.casefold() == "no")
async def handle_survey_email_newsletter_not_ok(
    message: types.Message,
    state: FSMContext,
):
    data = await state.update_data(newsletter=False)
    await state.clear()
    await send_survey_results(message, data)


@router.message(Survey.email_newsletter)
async def handle_survey_email_newsletter_dont_understand(message: types.Message):
    await message.answer(
        text="Sorry, I didn't understand... Pls send 'yes' or 'no'",
    )
