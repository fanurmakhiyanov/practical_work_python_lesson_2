# Реализуйте алгоритм перемешивания списка

import random

lst = list(range(1, 11))
print(f'Изначальный список: {lst}')
random.shuffle(lst)
print(f'Перемешанный список: {lst}')