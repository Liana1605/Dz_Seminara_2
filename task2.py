#Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
#Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. 
#Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
#Пример:
#4 4 -> 2 2
#5 6 -> 2 *

import math

sum = int(input('Введите сумма двух чисел: '))
proizv = int(input('Введите произведение двух чисел: '))

for x in range(sum):
    for y in range(proizv):
        if (x + y == sum) and (x * y == proizv):
            print('Петя загадал: ' + str(x) + ' ' + str(y))
            break
    if (x + y == sum) and (x * y == proizv):
        break
