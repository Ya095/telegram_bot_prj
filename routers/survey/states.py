from enum import StrEnum

from aiogram.fsm.state import StatesGroup, State


class Survey(StatesGroup):
    full_name = State()
    email = State()
    sport = State()
    email_newsletter = State()


class SurveySportDetails(StatesGroup):
    tennis = State()
    football = State()
    f1 = State()


class KnownSports(StrEnum):
    tennis = "Tennis"
    football = "Football"
    f1 = "F1"


class KnownF1Tracks(StrEnum):
    MONACO = "Monaco"
    SPA = "Spa"
    SUZUKA = "Suzuka"
    MONZA = "Monza"
