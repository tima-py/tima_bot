from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from handlers.buttons import yes_no_inline
from config import bot

router_fsm = Router()

class AddProduct(StatesGroup):
    name = State()
    price = State()
    description = State()


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
    data = await state.update_data(description=message.text)

    await message.answer(
        f"Товар добавлен!\n"
        f"Название товара - {data['name']}\n"
        f"Цена: {data['price']}\n"
        f"Описание: {data['description']}"
    )

    await state.clear()

class Add_Film(StatesGroup):
    name = State()
    genre = State()
    review = State()


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
            f"Оценка: {data['review']}/10"
        )
    await state.clear()

@router_fsm.callback_query(F.data == 'no')
async def cancel(call: CallbackQuery, bot, state: FSMContext):
    await bot.send_message(
        chat_id=call.message.chat.id,
        text='Создание фильма отменено :('
    )
    await state.clear()