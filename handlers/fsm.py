from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from db import main_db
from handlers.buttons import yes_no_inline


router_fsm = Router()

class AddProduct(StatesGroup):
    name = State()
    price = State()
    description = State()
    product_id = State() #артикул
    category = State()


@router_fsm.message(Command('add_product'))
async def add_start_fsm(message: Message, state: FSMContext):
    await message.answer('Введите название товара:')
    await state.set_state(AddProduct.name)

@router_fsm.message(AddProduct.name)
async def add_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer('Введите цену товара')
    await state.set_state(AddProduct.price)

@router_fsm.message(AddProduct.price)
async def add_price(message: Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer('Цена должна быть числом. Попробуйте еще раз')
    else:
        await state.update_data(price=message.text)
        await message.answer('Введите описание для данного товара:')
        await state.set_state(AddProduct.description)

@router_fsm.message(AddProduct.description)
async def add_description(message: Message, state: FSMContext):
    await state.update_data(description=message.text)
    await message.answer('Введите артикул для товара. Он должен быть уникальным!')
    await state.set_state(AddProduct.product_id)

@router_fsm.message(AddProduct.product_id)
async def add_product_id(message: Message, state: FSMContext):
    await state.update_data(product_id=message.text)
    await message.answer('Введите категорию')
    await state.set_state(AddProduct.category)

@router_fsm.message(AddProduct.category)
async def add_category(message: Message, state: FSMContext):

    data = await state.update_data(category=message.text)

    await message.answer(
        f"Товар добавлен!\n"
        f"Название товара - {data['name']}\n"
        f"Цена: {data['price']}\n"
        f"Описание: {data['description']}\n"
        f"Артикул: {data['product_id']}\n"
        f"Категория: {data['category']}"
    )

    await main_db.add_product_db(name_product=data['name'], price=data['price'], product_id=data['product_id'])
    await main_db.add_product_detail_db(product_id=data['product_id'], category=data['category'], description=data['description'])

    await state.clear()


class Add_Film(StatesGroup):
    name = State()
    genre = State()
    review = State()
    description = State()
    film_id = State()


@router_fsm.message(Command('add_film'))
async def add_start_fsm(message: Message, state: FSMContext):
    await message.answer('Введите название фильма:')
    await state.set_state(Add_Film.name)

@router_fsm.message(Command('cancel'))
async def cancel(message: Message, state: FSMContext):
    await message.answer('Создание фильма отменено :(')
    await state.clear()

@router_fsm.message(Add_Film.name)
async def add_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer('Введите жанр фильма')
    await state.set_state(Add_Film.genre)

@router_fsm.message(Add_Film.genre)
async def add_genre(message: Message, state: FSMContext):
    await state.update_data(genre=message.text)
    await message.answer('Введите артикул для данного фильма:')
    await state.set_state(Add_Film.film_id)

@router_fsm.message(Add_Film.film_id)
async def add_film_id(message: Message, state: FSMContext):
    await state.update_data(film_id=message.text)
    await message.answer('Введите описание для данного фильма:')
    await state.set_state(Add_Film.description)

@router_fsm.message(Add_Film.description)
async def add_description(message: Message, state: FSMContext):
    await state.update_data(description=message.text)
    await message.answer('Введите оценку от 1 до 10 для данного фильма:')
    await state.set_state(Add_Film.review)

@router_fsm.message(Add_Film.review)
async def add_review(message: Message, state: FSMContext):
    if not message.text.isdigit() or not 1 <= int(message.text) <= 10:
        await message.answer('Оценка должна быть числом от 1 до 10. Попробуйте еще раз')
    else:
        await state.update_data(review=message.text)
        await message.answer('Добавить данный фильм?', reply_markup=yes_no_inline)

@router_fsm.callback_query(F.data == 'yes')
async def agree(call: CallbackQuery, bot, state: FSMContext):
    data = await state.get_data()
    
    await bot.send_message(
        chat_id=call.message.chat.id,
        text=
            f"Фильм добавлен!\n"
            f"Название фильма: {data['name']}\n"
            f"Жанр: {data['genre']}\n"
            f"Оценка: {data['review']}/10\n"
            f"Артикул: {data['film_id']}\n"
            f"Описание: {data['description']}"
        )
    await main_db.add_film_db(name_film=data['name'], genre=data['genre'], film_id=data['film_id'])
    await main_db.add_film_detail_db(description=data['description'], film_id=data['film_id'], review=data['review'])

    
    await state.clear()

@router_fsm.callback_query(F.data == 'no')
async def cancel(call: CallbackQuery, bot, state: FSMContext):
    await bot.send_message(
        chat_id=call.message.chat.id,
        text='Создание фильма отменено :('
    )
    await state.clear()