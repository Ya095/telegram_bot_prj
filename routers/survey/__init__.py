from aiogram import Router
from .handlers import router as handlers_router


router = Router(name=__name__)

router.include_router(handlers_router)
