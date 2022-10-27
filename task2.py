# В первом ящике находится 8 мячей, из которых 5 - белые. 
# Во втором ящике - 12 мячей, из которых 5 белых. 
# Из первого ящика вытаскивают случайным образом два мяча, из второго - 4. Какова вероятность того, что 3 мяча белые?

from math import factorial

def combinations(n: int, k: int) -> int:
    c = factorial(n) / (factorial(k)*factorial(n-k))
    return c

p1 = (combinations(5, 2) / combinations(8, 2)) * (combinations(5, 1) / combinations(12, 1))
p2 = (combinations(5, 1) / combinations(8, 1)) * (combinations(5, 2) / combinations(12, 2))
p3 = (combinations(5, 0) / combinations(8, 0)) * (combinations(5, 3) / combinations(12, 3))

p = p1 + p2 + p3

print('\n Условие задачи: \n \
    В первом ящике находится 8 мячей, из которых 5 - белые. Во втором ящике - 12 мячей, из которых 5 белых. \n \
    Из первого ящика вытаскивают случайным образом два мяча, из второго - 4. Какова вероятность того, что 3 мяча белые? \n')


print(f'Ответ: \
    \n  Вероятность, что 3 мяча белые = {p} \n')