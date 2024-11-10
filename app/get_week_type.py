from datetime import datetime, timedelta


def get_week_type():
    today = datetime.now()
    weekday = today.weekday()  # 0 - Понедельник, 6 - Воскресенье

    # Начальная точка отсчета знаменателя (например, предположим, что текущая неделя знаменатель)
    is_numerator_week = False  # False — знаменатель, True — числитель

    # # Если сегодня воскресенье, считаем текущую неделю как знаменатель
    # if weekday == 6:
    #     return "Знаменатель"

    # Подсчет недель с начальной точки
    week_number = today.isocalendar()[1]
    if is_numerator_week:
        return "Числитель" if week_number % 2 != 0 else "Знаменатель"
    else:
        return "Знаменатель" if week_number % 2 != 0 else "Числитель"