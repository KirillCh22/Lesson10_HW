import random
import pandas as pd

def OneHot(string: str):
    """Функция по созданию нового DataFrame вида One Hot"""
    array_robot = []
    array_human = []
    for i in string:
        if i == 'robot':
            array_robot.append(1)
            array_human.append(0)
        else:
            array_robot.append(0)
            array_human.append(1)

    df = pd.DataFrame({'Human': array_human,
                        'Robot': array_robot})

    return df


def main():
    """Функция управляющая программой"""

    lst = ['robot'] * 10
    lst += ['human'] * 10
    random.shuffle(lst)
    data = pd.DataFrame({'whoAmI': lst})

    one_hot = OneHot(lst)

    print(data)
    print(one_hot)

#==================  ВЫЗЫВАЕМ ОСНОВНУЮ ФУНКЦИЮ ДЛЯ ЗАПУСКА ПРОГРАММЫ  ===============================
main()