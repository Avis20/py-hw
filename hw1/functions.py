from time import time, sleep
from functools import wraps
from itertools import repeat


def to_power(number_list, power=2):
    """
    Возвести список чисел в переданную степень
    :param number_list: Список чисел
    :param power: Степень в которую нужно возвести
    :return:
    """
    return list(map(pow, number_list, repeat(power)))


def even(number_list):
    """
    :param number_list: Список чисел
    :return: Список четных чисел
    """
    return list(filter(lambda x: x % 2 == 0, number_list))


def odd(number_list):
    """
    :param number_list: Список чисел
    :return: Список не четных чисел
    """
    return list(filter(lambda x: x % 2 != 0, number_list))


def is_prime(number):
    """
    Проверка является ли число простым или нет
    :param number: Целое число
    :return: True - Число является простым, False - Число не является простым
    """
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def simple(number_list):
    """
    Для каждого числа проверяется простое оно или нет
    :param number_list: Список чисел
    :return: Список простых чисел
    """
    return list(filter(is_prime, number_list))


def filter_numbers(number_list, filter_type):
    """
    :param number_list: Список целых чисел
    :param filter_type: тип фильтра.
     even - четные числа, odd - не четные числа, simple - простые числа
    :return: Отфильтрованный список чисел
    """
    FILTERS = {
        'even': even,
        'odd': odd,
        'simple': simple
    }
    return FILTERS[filter_type](number_list)


def time_call(func):
    @wraps(func)
    def wrapper(p):
        start = time()
        result = func(p)
        end = time()
        print("result for", p, " = ", result)
        time_taken = end - start
        print(f"time taken: {time_taken:.13f}")
        return result
    return wrapper


@time_call
def test_sleep(s_time):
    sleep(s_time)


def trace(separator):
    def decorator(func):
        func.level = 0

        def wrapper(pos):
            print(separator * func.level + f" --> {func.__name__}({pos})")
            func.level += 1
            result = func(pos)
            func.level -= 1
            print(separator * func.level + f" <-- {func.__name__}({pos}) == {result}")
            return result
        return wrapper
    return decorator


@trace("____")
def fib(pos):
    if pos <= 1:
        return 1
    return fib(pos - 1) + fib(pos - 2)


if __name__ == "__main__":
    numbers = [0, 1, 4, 5, 2, 12, 7]
    power = 3
    print(f"Возвести список чисел = {numbers}, в степень = {power}")
    power_result = to_power(numbers, power=power)
    print(f"Результат = {power_result}\n")

    print(f"Вывести четные числа из списока = {numbers}")
    even_numbers = filter_numbers(numbers, filter_type='even')
    print(f"Результат = {even_numbers}\n")

    print(f"Вывести не четные числа из списока = {numbers}")
    odd_numbers = filter_numbers(numbers, filter_type='odd')
    print(f"Результат = {odd_numbers}\n")

    print(f"Вывести простые числа из списока = {numbers}")
    simple_numbers = filter_numbers(numbers, filter_type='simple')
    print(f"Результат = {simple_numbers}\n")

    print("Проверка декоратора замера времени выполнения функции")
    print("Запуск test_sleep", test_sleep(.4), "\n")

    print("Вычисление числа Фибоначчи")
    number = 3
    print(f"Число Фибоначчи от {number} = {fib(number)}")
