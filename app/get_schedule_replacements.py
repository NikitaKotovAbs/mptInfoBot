import aiohttp
import asyncio
from bs4 import BeautifulSoup as BS
from config import URL

# Храним предыдущие данные о расписаниях для сравнения
previous_replacements = []

async def get_schedule_replacements():
    url = URL  # Используем URL из config
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status != 200:
                print(f"Ошибка доступа к сайту. Статус: {response.status}")
                return []

            content = await response.text()
            soup = BS(content, 'html.parser')

    # Находим все блоки с таблицами расписания
    replacement_blocks = soup.select('.table-responsive table.table-striped')
    if not replacement_blocks:
        print("Не найдено таблиц с расписанием.")
        return []

    replacements = []

    for block in replacement_blocks:
        group_info = block.select_one('caption b')
        group_name = group_info.text if group_info else "Информация о группе не найдена"

        # Фильтруем по интересующей группе (замените на нужную группу)
        if "П-5-21" in group_name:  # Пример фильтрации по группе
            group_message = f"Группа: {group_name}"
            replacements.append(group_message)

            # Перебираем строки таблицы (пропускаем первую строку с заголовками)
            for row in block.select('tr')[1:]:
                # Извлекаем данные по каждому столбцу
                lesson_number = row.select_one('.lesson-number').text.strip()
                replace_from = row.select_one('.replace-from').text.strip()
                replace_to = row.select_one('.replace-to').text.strip()
                updated_at_str = row.select_one('.updated-at').text.strip()

                # Формируем сообщение о замене
                replacement_message = (
                    f"Пара: {lesson_number}\n"
                    f"Что заменяют: {replace_from}\n"
                    f"На что заменяют: {replace_to}\n"
                    f"Замена добавлена: {updated_at_str}\n"
                )
                replacements.append(replacement_message)
                replacements.append("-" * 30)

    return replacements


# Функция для сравнения данных и отправки изменений
async def check_for_updates(bot, chat_id=1388135173):
    global previous_replacements
    current_replacements = await get_schedule_replacements()

    # Проверяем, изменилось ли расписание
    if current_replacements != previous_replacements:
        print("Обновления расписания найдены!")
        # Если данные изменились, отправляем их (например, через бота)
        await send_updates(bot, current_replacements, chat_id)
        previous_replacements = current_replacements  # Обновляем предыдущие данные
    else:
        print("Нет изменений в расписании.")


# Функция для отправки обновлений в бот
async def send_updates(bot, replacements, chat_id=1388135173):
    # Отправляем каждое сообщение о замене пользователю в чат
    for message in replacements:
        try:
            await bot.send_message(chat_id, message)  # Отправка сообщения в чат
        except Exception as e:
            print(f"Ошибка при отправке сообщения: {e}")


# Запуск проверки каждый минуту
async def schedule_updates(bot, chat_id=1388135173):
    while True:
        await check_for_updates(bot, chat_id)
        await asyncio.sleep(60)  # Пауза в 1 минуту перед следующей проверкой
