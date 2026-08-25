from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from db import main_db
from handlers import buttons

router_delete = Router()

class DeleteProduct(StatesGroup):
    confirm = State()
    confirm_all = State()

@router_delete.callback_query(F.data.startswith('delete:'))
async def delete_start(call: CallbackQuery, state: FSMContext):
    product_id = call.data.split(':')[1]
    await state.update_data(product_id=product_id)
    await state.set_state(DeleteProduct.confirm)
    await call.message.answer("Вы точно хотите удалить?", reply_markup=buttons.delete_fields) 
    await call.answer()

@router_delete.callback_query(DeleteProduct.confirm, F.data.startswith('delete_confirm'))
async def delete_confirm(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    product_id = data["product_id"]
    await main_db.delete_product_db(product_id)
    await call.message.answer("Товар успешно удален!")
    await state.clear()
    await call.answer()

@router_delete.callback_query(DeleteProduct.confirm, F.data.startswith('delete_cancel'))
async def delete_cancel(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Удаление отменено")
    await state.clear()
    await call.answer()

@router_delete.callback_query(F.data == 'delete_all')
async def delete_all_start(call: CallbackQuery, state: FSMContext):
    await state.set_state(DeleteProduct.confirm_all)
    await call.message.answer('Вы точно хотите удалить все товары?',reply_markup=buttons.delete_all_confirm)
    await call.answer()

@router_delete.callback_query(DeleteProduct.confirm_all, F.data == 'delete_all_confirm')
async def delete_all_confirm(call: CallbackQuery, state: FSMContext):
    await main_db.delete_all_products_db()
    await call.message.answer("Все товары успешно удалены!")
    await state.clear()
    await call.answer()

@router_delete.callback_query(DeleteProduct.confirm_all, F.data == 'delete_all_cancel')
async def delete_all_cancel(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Удаление отменено")
    await state.clear()
    await call.answer()