def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    for number in numbers:
        try:
            result += number
        except TypeError:
            print(f'Некорректный тип данных для подсчёта суммы - {number}')
            incorrect_data += 1

    return result, incorrect_data


def calculate_average(numbers):
    try:
        if isinstance(numbers, (list, tuple)):
            total_sum, incorrect_count = personal_sum(numbers)
            count = len(numbers) - incorrect_count
            if count == 0:
                return 0  # Обработка ZeroDivisionError
            return total_sum / count
        else:
            print('В numbers записан некорректный тип данных')
            return None
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None


# Примеры вызовов функции calculate_average
print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Список с некорректными данными
print(f'Результат 3: {calculate_average(567)}')  # Не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Корректный список



