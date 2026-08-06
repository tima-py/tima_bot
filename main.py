from decouple import config
from datetime import datetime
import random
from aiogram import Bot, Dispatcher, Router, F
import asyncio
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile
import logging

token = config('BOT_TOKEN')

router = Router()

@router.message(Command('start'))
async def start_command(message: Message, bot: Bot):
    await message.answer('Привет. Напиши своё имя ')

    await bot.send_message(chat_id=message.chat.id, text='Приветствую!')

@router.message(Command('help'))
async def help_command(message: Message):
    await message.answer('/start - старт бота\n/help - помощник\n/meme - фото мема\n/time - текущая дата и время\n/random - случайное число от 1 до 100\n/joke - случайная шутка\nИ если вы напишите "привет" то бот вам ответит "Hello"')

@router.message(F.text == 'привет')
async def hello_command(message: Message):
    await message.answer('Hello')

@router.message(Command('meme'))
async def meme_command(message: Message, bot: Bot):
    photo = FSInputFile('/home/alymbek/Desktop/group_68_2/media/photo_5447215620777777648_y.jpg')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)

@router.message(Command('time'))
async def time_command(message: Message):
    dt = datetime.now()
    text = f'Сейчас: {dt.day}.{dt.month}.{dt.year} {dt.hour}:{dt.minute}'
    await message.answer(text)

@router.message(Command('random'))
async def random_command(message: Message):
    await message.answer(f'Твоё случайное число: {random.randint(1, 100)}')

@router.message(Command('joke'))
async def random_command(message: Message):
    jokes = ['Как заставить змею плакать? — Отобрать у нее погремушку.', 'Зачем птицы летают в теплые края? — Потому что идти пешком долго.', 'Британские ученые выяснили: если долго смотреть на кота, он начнет смотреть в ответ… с осуждением.', 'Почему крокодил не пишет стихи? — Слез хватает, а рифм нет.', 'Почему рыбы живут в соленой воде? — Потому что перченая вода заставляет их чихать.']
    await message.answer(random.choice(jokes))

@router.message(F.text)
async def echo(message: Message):
    await message.answer(f'Такой команды нет - {message.text}')

async def main():
    logging.basicConfig(level=logging.INFO)

    bot = Bot(token=token)
    dp = Dispatcher()

    dp.include_router(router=router)

    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())