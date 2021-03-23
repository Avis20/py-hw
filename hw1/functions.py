
from time import time
from functools import wraps
from itertools import repeat


def to_involve(numbers, power=1):
    return list(map(pow, numbers, repeat(power)))


def even(number_list):
    return list(filter(lambda x: x % 2 == 0, number_list))


def odd(number_list):
    return list(filter(lambda x: x % 2 != 0, number_list))


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def simple(number_list):
    return list(filter(is_prime, numbers))


def filter_numbers(numbers, filter_type):
    FILTERS = {
        'even': even,
        'odd': odd,
        'simple': simple
    }
    return FILTERS[filter_type](numbers)


def time_call(func):
    @wraps(func)
    def wrapper(p):
        start = time()
        res = func(p)
        end = time()
        print("res for", p, " = ", res)
        time_taken = end - start
        print(f"time taken: {time_taken:.13f}")
        return res
    print(wrapper.__wrapped__)
    print(id(wrapper))
    print(id(func))
    print(id(wrapper.__wrapped__))
    return wrapper


def trace(separator):
    def decorator(func):
        level = 1

        def wrapper(pos):
            print(separator * level, end='')
            print(f" --> fib({pos})")
            result = func(pos)
            return result
        return wrapper

    return decorator


@trace("____")
def fib(pos):
    if pos <= 1:
        return 1
    return fib(pos - 1) + fib(pos - 2)


if __name__ == "__main__":
    fib(3)
    # numbers = [0, 1, 4, 5, 2, 12, 7]
    # power = 2
    # print("Возвести список чисел = {numbers}, в степень = {power}".format(
    #     numbers=numbers, power=power
    # ))
    # power_retult = to_involve(numbers, power=power)
    # print("Результат = {retult}".format(retult=power_retult))

    # print("Вывести четные числа из списока = {numbers}".format(numbers=numbers))
    # even_numbers = filter_numbers(numbers, filter_type='even')
    # print("Результат = {retult}".format(retult=even_numbers))

    # print("Вывести не четные числа из списока = {numbers}".format(numbers=numbers))
    # odd_numbers = filter_numbers(numbers, filter_type='odd')
    # print("Результат = {retult}".format(retult=odd_numbers))

    # print("Вывести простые числа из списока = {numbers}".format(numbers=numbers))
    # simple_numbers = filter_numbers(numbers, filter_type='simple')
    # print("Результат = {retult}".format(retult=simple_numbers))
