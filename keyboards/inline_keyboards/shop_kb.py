from enum import IntEnum, auto
from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


class ShopActions(IntEnum):
    products = auto()
    address = auto()
    root = auto()


class ShopData(CallbackData, prefix="shop"):
    action: ShopActions


class ProductActions(IntEnum):
    detail = auto()
    update = auto()
    delete = auto()


class ProductsData(CallbackData, prefix="product"):
    action: ProductActions
    id: int
    title: str
    price: int


def build_shop_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(
        text="Show products",
        callback_data=ShopData(action=ShopActions.products).pack(),
    )
    builder.button(
        text="My address",
        callback_data=ShopData(action=ShopActions.address).pack(),
    )

    builder.adjust(1)
    return builder.as_markup()


def build_products_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(
        text="Back to root",
        callback_data=ShopData(action=ShopActions.root).pack(),
    )

    for idx, (name, price) in enumerate(
        [
            ("Laptop", 1299),
            ("Desktop", 4023),
            ("TV", 21000),
        ],
        start=1,
    ):
        builder.button(
            text=name,
            callback_data=ProductsData(
                action=ProductActions.detail,
                id=idx,
                title=name,
                price=price,
            ),
        )

    builder.adjust(1)
    return builder.as_markup()


def product_detail_kb(product_cb_data: ProductsData) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(
        text="⬅️ Back to products",
        callback_data=ShopData(action=ShopActions.products).pack(),
    )
    for label, action in [("Update", ProductActions.update), ("Delete", ProductActions.delete),]:
        builder.button(
            text=label,
            callback_data=ProductsData(
                action=action,
                **product_cb_data.model_dump(include={"id", "title", "price"}),
                # id=product_cb_data.id,
                # title=product_cb_data.title,
                # price=product_cb_data.price,
            )
        )

    builder.adjust(1, 2)
    return builder.as_markup()


def build_update_product_kb(product_cb_data: ProductsData) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(
        text=f"⬅️ Back to {product_cb_data.title!r}",
        callback_data=ProductsData(
            action=ProductActions.detail,
            **product_cb_data.model_dump(include={"id", "title", "price"}),
        ),
    )
    builder.button(
        text="🔄 Update",
        callback_data="...",  # сейчас нет логики update
    )

    return builder.as_markup()
