#создаем игру
import numpy as np
number = np.random.randint(1, 101)#загадываем числа
count = 0
while True:
    count += 1
    predict_number = int(input('угадай число от 1 до 100: '))
    if predict_number > number:
        print('число меньше')
    elif predict_number < number:
        print('число больше')
    else:
        print(f'Вы угадали число! Это число = {number}, за {count} попыток')
        break
    
