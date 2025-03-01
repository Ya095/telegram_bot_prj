from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State

from keyboards.common_keyboards import build_select_keyboard
from routers.survey.states import Survey, KnownSports, SurveySportDetails, KnownF1Tracks

router = Router(name=__name__)


known_sports_to_next: dict[str, tuple[State, str]] = {
    KnownSports.tennis: (
        SurveySportDetails.tennis,
        "Who is your favourite tennis player?",
    ),
    KnownSports.football: (
        SurveySportDetails.football,
        "What is your favourite football team?",
    ),
    KnownSports.f1: (
        SurveySportDetails.f1,
        "What is your favourite F1 tracks?",
    ),
}

known_sports_to_kb: dict = {
    KnownSports.f1: build_select_keyboard(KnownF1Tracks),
}


@router.message(
    Survey.sport,
    F.text.cast(KnownSports),
)
async def select_sport(
    message: types.Message,
    state: FSMContext,
):
    await state.update_data(sport=message.text)
    next_state, question_text = known_sports_to_next[message.text]
    await state.set_state(next_state)
    kb = types.ReplyKeyboardRemove()
    if message.text == KnownSports.f1:
        kb = known_sports_to_kb[KnownSports.f1]
    await message.answer(
        text=question_text,
        reply_markup=kb,
    )


@router.message(Survey.sport)
async def select_sport(message: types.Message):
    print(message.text, Survey.sport)
    await message.answer(
        text="Unknown sport, pls select one of the following:",
        reply_markup=build_select_keyboard(KnownSports),
    )
