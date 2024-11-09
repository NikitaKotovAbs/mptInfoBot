import aiogram
import logging
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import message

from app.handlers import start, schedule_view, show_replacements, exam_schedule
from config import TOKEN
from app.get_schedule_replacements import schedule_updates

bot = Bot(token=TOKEN)
dp = Dispatcher()

async def main():
    dp.include_router(start.router)
    dp.include_router(schedule_view.router)
    dp.include_router(show_replacements.router)
    dp.include_router(exam_schedule.router)
    # Запускаем периодическое обновление расписания
    asyncio.create_task(schedule_updates(bot))  # Запуск обновлений расписания

    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)  # Только при debug: on
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bot off')
