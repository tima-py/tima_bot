import logging
from config import bot, dp, Admin
import asyncio
from handlers import commands, echo, fsm, fsm_edit, fsm_delete
from db import main_db

from aiogram.types import BotCommand

async def set_commands():
    commands = [
        BotCommand(command='start', description='Старт бота'),
        BotCommand(command='help', description='Помощь'),
        BotCommand(command='mem', description='мем'),
        BotCommand(command='products', description='Получить товары из БД'),
        BotCommand(command='add_product', description='Записать товар'),
    ]
    await bot.set_my_commands(commands)

async def on_startup():
    await main_db.init_db()
    await main_db.create_table()
    await set_commands()
    for admin_id in Admin:
        await bot.send_message(chat_id=admin_id, text='Бот включен!')

dp.include_router(commands.router_commands)
dp.include_router(fsm.router_fsm)
dp.include_router(fsm_edit.router_edit)
dp.include_router(fsm_delete.router_delete)

# Эхо 
dp.include_router(echo.router_echo)

dp.startup.register(on_startup)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(dp.start_polling(bot))