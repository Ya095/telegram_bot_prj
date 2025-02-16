from aiogram import Router
from .info_kb_callback_handlers import router as info_callback_router
from .action_kb_callback_handlers import router as action_callback_router
from .shop_kb_callback_handlers import router as shop_callback_router


router = Router(name=__name__)

router.include_router(action_callback_router)
router.include_router(info_callback_router)
router.include_router(shop_callback_router)
