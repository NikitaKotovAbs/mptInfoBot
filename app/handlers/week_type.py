# Использование в боте
from aiogram import F, Router
from aiogram.types import Message
import app.keyboard as kb
from app.get_week_type import get_week_type

router = Router()


@router.message(F.text == "Определение текущей недели")
async def week_type_handler(message: Message):
    week_type = get_week_type()
    await message.answer(f"Сейчас неделя: {week_type}", reply_markup=kb.keyboard_reply)
