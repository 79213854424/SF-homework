#игра угадай число
import numpy as np
def random_predict(number : int=1)-> int:
    """угадываем рандомно число

    Args:
        number (int, optional): загаданное число. Defaults to 1.

    Returns:
        int: число попыток
    """
    count = 0
    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # предполагаемое число
        if number == predict_number:
            break
    return count
print(f'Количество попыток: {random_predict(23)}')
def score_game(random_predict)->int:
    """за какое 1000 подходов угадывает число

    Args:
        random_predict (_type_): функция угадывания

    Returns:
        int:сколько попыток
    """
    count_ls = []
    np.random.seed(1)#фиксируем сид для производительности
    random_array = np.random.randint(1, 100, size = (1000))#задали список чисел
    for number in random_array:
        count_ls.append(random_predict(number))
    score = int(np.mean(count_ls))
    print(f'Ваш алгоритм в угадывает число загаданное в среднем за {score} попыток')
    return score
score_game(random_predict)
 
if __name__ == '__main__':
    score_game(random_predict) 
