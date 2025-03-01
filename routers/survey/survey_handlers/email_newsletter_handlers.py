from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.utils import markdown

from routers.survey.states import Survey

router = Router(name=__name__)


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
