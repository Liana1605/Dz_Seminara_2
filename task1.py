#На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, 
#которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, 
#которые нужно перевернуть
#*Пример:
#5 -> 1 0 1 1 0
#2

import random

kol_monet = int(input('Введите количество монеток: '))
monet = ''

for i in range(kol_monet):
    monet += str(random.randint(0, 1))
print(monet)

tails = 0
for i in range(kol_monet):
    if int(monet[i]) == 0:
        tails += 1
        
if tails == kol_monet/2 or tails < kol_monet - tails:
    print(str(tails) + ' раз')
if tails > kol_monet - tails:
    print(str(kol_monet - tails) + ' раз')