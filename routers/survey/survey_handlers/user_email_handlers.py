from aiogram import types, F, Router
from aiogram.fsm.context import FSMContext
from aiogram.utils import markdown

from keyboards.common_keyboards import build_select_keyboard
from routers.survey.states import Survey, KnownSports
from validators.email_validator import valid_email

router = Router(name=__name__)


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


@router.message(Survey.full_name)
async def handle_survey_user_full_name_invalid_content_type(
    message: types.Message,
):
    await message.answer(
        "Sorry I couldn't understand. Send your full name as text.",
    )


@router.message(
    Survey.email,
    # validate_email_filter,
    # F.func(valid_email_msg_text).as_("email"),
    F.text.cast(valid_email).as_("email"),
)
async def handle_survey_email_msg(
    message: types.Message,
    state: FSMContext,
    email: str,
):
    await state.update_data(email=message.text)
    await state.set_state(Survey.sport)
    await message.answer(
        text=f"Cool, your email {markdown.hbold(email)}\n" "Which sport do you prefer?",
        # reply_markup=ReplyKeyboardMarkup(
        #     keyboard=[
        #         [
        #             KeyboardButton(text="yes"),
        #             KeyboardButton(text="no"),
        #         ]
        #     ],
        #     resize_keyboard=True,
        # ),
        reply_markup=build_select_keyboard(KnownSports),
    )


@router.message(Survey.email)
async def handle_survey_email_msg(message: types.Message):
    await message.answer(
        text="Invalid email... Pls try again.",
    )
