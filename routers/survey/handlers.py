from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import ReplyKeyboardRemove

from routers.survey.states import Survey
from .survey_handlers.email_newsletter_handlers import router as email_newsletter_router
from .survey_handlers.select_sport_handlers import router as sport_router
from .survey_handlers.user_email_handlers import router as user_email_router

router = Router(name=__name__)
router.include_router(email_newsletter_router)
router.include_router(user_email_router)
router.include_router(sport_router)


@router.message(
    Command("survey", prefix="!/"),
    default_state,
)
async def handle_start_survey(
    message: types.Message,
    state: FSMContext,
):
    await state.set_state(Survey.full_name)  # ожидаем и записываем данные юзера
    await message.answer(
        "Welcome to our weekly survey!\n" "What's your name?",
        reply_markup=ReplyKeyboardRemove(),
    )


@router.message(Command("cancel"), Survey())
@router.message(F.text.casefold() == "cancel", Survey())
async def cancel_handler(
    message: types.Message,
    state: FSMContext,
) -> None:
    """Allow user to cancel survey"""

    current_state = await state.get_state()
    if current_state is None:
        await message.reply(
            text="OK, but nothing was going on.\n" "Start survey: /survey",
            reply_markup=ReplyKeyboardRemove(),
        )
        return

    await state.clear()
    await message.answer(
        text=f"Cancelled survey on state {current_state!r}.\n" f"Start again: /survey",
        reply_markup=ReplyKeyboardRemove(),
    )
