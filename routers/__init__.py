from aiogram import Router
from .commands import router as commands_router
from .common import router as common_router
from .media_handlers import router as media_router
from .admin_handlers import router as admin_router
from .callback_handlers import router as callback_router


router = Router(name=__name__)

router.include_router(callback_router)
router.include_router(commands_router)
router.include_router(media_router)
router.include_router(admin_router)

# this one has to be last router!
router.include_router(common_router)
