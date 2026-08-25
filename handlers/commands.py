from aiogram.filters import Command
from aiogram import Router, F
from aiogram.types import Message, FSInputFile, CallbackQuery
from config import bot

from handlers.buttons import main_buttons, main_builder, menu_inline, product_actions

from db import main_db

router_commands = Router()

@router_commands.message(Command('start'))
async def start_command(message: Message, bot):
    await message.answer('Привет. Напиши своё имя ', reply_markup=menu_inline)

    await bot.send_message(chat_id=message.chat.id, text=f'Привет. Твой ID - {message.from_user.id}')


@router_commands.message(Command('help'))
async def help_command(message: Message):
    await message.answer('/start - старт бота \n/help - помощник ')


@router_commands.message(F.text == 'привет')
async def hello_command(message: Message):
    await message.answer('Hello')


@router_commands.message(Command('mem'))
async def mem_command(message: Message, bot):
    photo = FSInputFile('media/mem.png')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)


@router_commands.callback_query(F.data == 'mem')
async def mem_command(call: CallbackQuery, bot):
    photo = FSInputFile('media/mem.png')
    await bot.send_photo(chat_id=call.message.chat.id, photo=photo)


@router_commands.message(Command('products'))
async def get_products(message: Message):
    products = await main_db.get_product_db()

    if not products:
        await message.answer('В базе товаров нет!')
        return
    else:
        for name, price, category, description, product_id, photo_id  in products:
            # await message.answer(f'Название - {name}\nЦена - {price}\nОписание - {description}\nКатегория - {category}\nАртикул - {product_id}')
            await message.answer_photo(photo=photo_id,
                caption=(f'Название - {name}\nЦена - {price}\nОписание - {description}\nКатегория - {category}\nАртикул - {product_id}'), 
                reply_markup=product_actions(product_id=product_id))
@router_commands.message(Command('films'))
async def get_films(message: Message):
    films = await main_db.get_film_db()

    if not films:
        await message.answer('В базе фильмов нет!')
        return
    else:
        for name_film, genre, film_id, description, review in films:
            await message.answer(f"""
            Название - {name_film}
Жанр - {genre}
Описание - {description}
Оценка - {review}/10
Артикул - {film_id}
                """)           