import os
from aiogram import Router, F
from aiogram.types import Message
import app.keyboard as kb

router = Router()


@router.message(F.text == "Расписание экзаменов")
async def exam_schedule(message: Message):
    await message.answer(
        "На данный момент расписание ещё не опубликовано, так как оно ещё не было выложено."
        " Ожидайте его появление в течение месяца.",
        reply_markup=kb.keyboard_reply)
