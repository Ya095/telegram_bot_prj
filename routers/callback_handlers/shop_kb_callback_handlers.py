from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.utils import markdown

from keyboards.inline_keyboards.shop_kb import (
    ShopData,
    ShopActions,
    build_shop_kb,
    build_products_kb,
    ProductsData,
    ProductActions, product_detail_kb, build_update_product_kb,
)

router = Router(name=__name__)


@router.callback_query(
    ShopData.filter(F.action == ShopActions.products),
)
async def send_products_list(callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        text="Available products:",
        reply_markup=build_products_kb(),
    )


@router.callback_query(
    ShopData.filter(F.action == ShopActions.address),
)
async def handle_my_address_btn(callback_query: CallbackQuery):
    print(callback_query.data)
    await callback_query.answer(
        "Your address section is still in progress...",
        cache_time=30,
    )


@router.callback_query(
    ShopData.filter(F.action == ShopActions.root),
)
async def handle_my_address_btn(callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        text="Your shop actions:",
        reply_markup=build_shop_kb(),
    )


@router.callback_query(
    ProductsData.filter(F.action == ProductActions.detail),
)
async def handle_product_details_btn(
    callback_query: CallbackQuery,
    callback_data: ProductsData,
):
    message_text = markdown.text(
        markdown.hbold(f"Product №{callback_data.id}"),
        markdown.text(
            markdown.hbold(f"Title:"),
            callback_data.title,
        ),
        markdown.text(
            markdown.hbold(f"Price:"),
            callback_data.price,
        ),
        sep="\n",
    )
    await callback_query.message.edit_text(
        text=message_text,
        reply_markup=product_detail_kb(callback_data),
    )


@router.callback_query(
    ProductsData.filter(F.action == ProductActions.delete),
)
async def handle_product_delete_btn(
    callback_query: CallbackQuery,
):
    # по реализации одно и тоже, что и update
    await callback_query.answer(
        text="Delete is still in progress..."
    )


@router.callback_query(
    ProductsData.filter(F.action == ProductActions.update),
)
async def handle_product_update_btn(
    callback_query: CallbackQuery,
    callback_data: ProductsData,
):
    # редактируем только клавиатуру, но не сообщение
    await callback_query.message.edit_reply_markup(
        reply_markup=build_update_product_kb(callback_data),
    )
