from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

from aiogram.utils.keyboard import ReplyKeyboardBuilder

main_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='/start'), KeyboardButton(text='/help'), 
         KeyboardButton(text='/mem'), KeyboardButton(text='Ничего')],
    ],
    resize_keyboard=True
)

# ------------------------------------------------------------------------------------------

main_buttons_builder = ReplyKeyboardBuilder()
main_buttons_builder.button(text='/start')
main_buttons_builder.button(text='/help')
main_buttons_builder.adjust(2)

main_builder = main_buttons_builder.as_markup(resize_keyboard=True)

# ------------------------------------------------------------------------------------------

# INLINE-BUTTONS

menu_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Мем', callback_data='mem')],
        [InlineKeyboardButton(text='Помощь', callback_data='help')]
    ]
)
yes_no_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='ДАА', callback_data='yes')],
        [InlineKeyboardButton(text='неет', callback_data='no')]
    ]
)
# edit:1001
# edit 1001

def product_actions(product_id):
    print(f"кнопки - {product_id}")
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='✏️ Редактировать', callback_data=f'edit:{product_id}'),
             InlineKeyboardButton(text='🗑 Удалить', callback_data=f'delete:{product_id}'),
             InlineKeyboardButton(text='Удалить всё', callback_data='delete_all')
             ]
        ]
    )

delete_fields = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Да, удалить', callback_data=f'delete_confirm'),
             InlineKeyboardButton(text='Отмена', callback_data=f'delete_cancel')]
    ]
)

edit_fields = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Название', callback_data='field_name_product'),
        InlineKeyboardButton(text='Цена', callback_data='field_price')],
        [InlineKeyboardButton(text='Описание', callback_data='field_description'),
        InlineKeyboardButton(text='Категория', callback_data='field_category')]
    ]
)

delete_all_confirm = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Да, удалить всё', callback_data='delete_all_confirm'),
        InlineKeyboardButton(text='Отмена', callback_data='delete_all_cancel')]
    ]
)