import random
from random import randint
def get_unique_list_numbers() -> list[int]:
    ...  # TODO написать функцию для получения списка уникальных целых чисел
    list = []
    while len(list) < 15:
        digit_ = random.randint(-10,10)
        if digit_ not in list:
            list.append(digit_)
    return list

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
