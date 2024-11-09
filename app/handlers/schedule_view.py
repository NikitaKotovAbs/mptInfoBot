import os
from aiogram import Router, types, F
from aiogram.types import FSInputFile, Message
import app.keyboard as kb
from run import bot

router = Router()


@router.message(F.text == "Расписание")
async def schedule_view(message: Message):
    schedule_photo_path = os.path.join("app", "img", "schedule.jpg")
    photo = FSInputFile(schedule_photo_path)
    await bot.send_photo(chat_id=message.chat.id, photo=photo, caption="Учебное расписание",
                         reply_markup=kb.keyboard_reply)
