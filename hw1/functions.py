
from itertools import repeat

EVEN = 'even'
ODD = 'odd'
SIMPLE_NUMBER = 'simple_number'


def to_involve(numbers, power=1):
    return list(map(pow, numbers, repeat(power)))


def filter_numbers(numbers, filter_type):
    if filter_type == EVEN:
        return [filter(numbers)]


if __name__ == "__main__":
    numbers = [4, 5, 2]
    power = 2
    print("Возвести список чисел = {numbers}, в степень = {power}".format(
        numbers=numbers, power=power
    ))
    print("Результат = {retult}".format(
        retult=to_involve(numbers, power=power)
    ))
    
    filter_numbers(numbers, filter_type=EVEN)
