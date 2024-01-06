import random

with open ('Division_Operations/Division_Level1', 'r') as file:
    LIST_DIVISION_LEVEL1 = [l.strip() for l in file]

with open('Division_Operations/Division_Level2', 'r') as fifo:
    LIST_DIVISION_LEVEL2= [l.strip()[:9]for l in fifo ]

with open('Division_Operations/Division_Level3', 'r') as mifo:
    LIST_DIVISION_LEVEL3= [l.strip()[:9]for l in mifo ]
def main():
    final= division(2)
    print(f'Score:{final}')

def add_sub_operands(level):
    min= 10 ** (level-1)
    max= (10 ** level) - 1
    x= random.randint(min,max)
    y= random.randint(min,max)
    return (x,y)

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

    return (x,y)

def addition(level):
    #result = 0
    #limit= 0

    value_1, value_2 = add_sub_operands(level)
    problem= f'{value_1} + {value_2} ='
    return problem


def substraction(level):
    value_1, value_2 = add_sub_operands(level)
    score= f'{value_1} - {value_2} = '
    return score

def multiplication(level):
    value_1, value_2 = mult_div_operands(level)
    score= f'{value_1} x {value_2} = '
    return score

def division(level):
    value_1, value_2 = mult_div_operands(level)
    if value_1 % value_2 == 0 and value_1 >= value_2:
        score= f'{value_1} / {value_2} = '
        return score
    else:
        if level == 1:
            return  random.choice(LIST_DIVISION_LEVEL1)
        elif level == 2:
            return  random.choice(LIST_DIVISION_LEVEL2)
        else:
            return random.choice(LIST_DIVISION_LEVEL3)



if __name__ == '__main__':
    main()
