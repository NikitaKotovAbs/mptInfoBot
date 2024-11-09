import os
from aiogram import Router, types, F
from aiogram.types import FSInputFile, Message
import app.keyboard as kb
from app.get_schedule_replacements import get_schedule_replacements

router = Router()


@router.message(F.text == "Посмотреть замены")
async def show_replacements(message: types.Message):
    replacements = await get_schedule_replacements()
    if replacements:
        for replacement in replacements:
            await message.answer(replacement)
    else:
        await message.answer("Сегодня замен нет.")
