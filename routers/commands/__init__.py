from aiogram import Router
from .base_commands import router as base_commands_router
from .user_commands import router as user_commands_router

router = Router(name=__name__)
router.include_router(base_commands_router)
router.include_router(user_commands_router)


__all__ = ("router", )
