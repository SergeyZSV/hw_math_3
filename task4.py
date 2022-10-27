# В университет на факультеты A и B поступило равное количество студентов, а на факультет C студентов поступило столько же, сколько на A и B вместе. 
# Вероятность того, что студент факультета A сдаст первую сессию, равна 0.8. 
# Для студента факультета B эта вероятность равна 0.7, а для студента факультета C - 0.9. 
# Студент сдал первую сессию. Какова вероятность, что он учится: a). на факультете A б). на факультете B в). на факультете C?

# A - сдача сессии
# B - сдача сессии студентом (a, b, c)

p_ab_ab = 1/4
p_ab_c = 2/4
p_b1 = 0.8
p_b2 = 0.7
p_b3 = 0.9
p_a = p_ab_ab * (p_b1 + p_b2) + p_ab_c * p_b3

p1 = (p_ab_ab * p_b1) / p_a
p2 = (p_ab_ab * p_b2) / p_a
p3 = (p_ab_c * p_b3) / p_a

print('\nУсловие задачи: \
    \n В университет на факультеты A и B поступило равное количество студентов, а на факультет C студентов поступило столько же, сколько на A и B вместе. \
    \n Вероятность того, что студент факультета A сдаст первую сессию, равна 0.8. \
    \n Для студента факультета B эта вероятность равна 0.7, а для студента факультета C - 0.9. \
    \n Студент сдал первую сессию. Какова вероятность, что он учится: a). на факультете A б). на факультете B в). на факультете C? \n')


print(f'Ответ: \
    \n Вероятность того, что студент учится на факультете A = {p1} \
    \n Вероятность того, что студент учится на факультете B = {p2} \
    \n Вероятность того, что студент учится на факультете C = {p3} \n')