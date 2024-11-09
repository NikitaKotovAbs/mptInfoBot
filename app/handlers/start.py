from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
import app.keyboard as kb

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        "Привет! Я — бот, который предоставляет актуальную информацию"
        " из учебного заведения ФГБОУ РЭУ МПТ им. Г.В. Плеханова. "
        "Ты можешь воспользоваться моими возможностями для получения нужной информации.",
        reply_markup=kb.keyboard_reply)
