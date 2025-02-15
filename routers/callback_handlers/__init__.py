from aiogram import Router
from .info_kb_callback_handlers import router as info_callback_router


router = Router(name=__name__)
router.include_router(info_callback_router)
