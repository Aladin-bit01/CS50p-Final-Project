import random
import pygame


def main():
    final = division(2)
    print(f'Score:{final}')


def add_sub_operands(level):
    min = 10 ** (level - 1)
    max = 10 ** level
    x = random.randint(min, max)
    y = random.randint(min, max)
    return (x, y)


def mult_div_operands(level):
    if level == 1:
        x = random.randint(1, 9)
        y = random.randint(1, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(1, 9)
    else:
        x = random.randint(10, 99)
        y = random.randint(10, 99)

    return (x, y)


def addition(level):
    result = 0
    limit = 0
    for _ in range(10):
        value_1, value_2 = add_sub_operands(level)
        score = input(f'{value_1} + {value_2} = ')

        if int(score) == value_1 + value_2:
            result += 1
        else:
            limit += 1
            print('EEE')
            if limit == 3:
                print(f'{value_1} + {value_2}= {value_1 + value_2}')
                limit = 0
    return result


def substraction(level):
    result = 0
    limit = 0
    for _ in range(10):
        value_1, value_2 = add_sub_operands(level)
        score = input(f'{value_1} - {value_2} = ')
        if int(score) == value_1 - value_2:
            result += 1
        else:
            limit += 1
            print('EEE')
            if limit == 3:
                print(f'{value_1} - {value_2}= {value_1 - value_2}')
                limit = 0
    return result


def multiplication(level):
    result = 0
    limit = 0
    for _ in range(10):
        value_1, value_2 = mult_div_operands(level)
        score = input(f'{value_1} * {value_2} = ')
        if int(score) == value_1 * value_2:
            result += 1
        else:
            limit += 1
            print('EEE')
            if limit == 3:
                print(f'{value_1} * {value_2}= {value_1 * value_2}')
                limit = 0
    return result


def division(level):
    operation = 0
    result = 0
    limit = 0
    while operation < 10:
        value_1, value_2 = mult_div_operands(level)
        if value_1 % value_2 != 0:
            continue
        else:
            operation += 1
            score = input(f'{value_1} / {value_2} = ')
            if int(score) == value_1 / value_2:
                result += 1
            else:
                limit += 1
                print('EEE')
                if limit == 3:
                    print(f'{value_1} / {value_2}= {int(value_1 / value_2)}')
                    limit = 0
    return result


if __name__ == '__main__':
    main()