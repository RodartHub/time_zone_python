import random 
import os

def show(name_operation,operation):
    print(f'\n{name_operation}: ')
    print(f'\t {operation} ')


def run():
    os.system('clear')
    my_list1 = [random.randint(1,10) for _ in range(0,10)]
    my_list2 = [random.randint(1,10) for _ in range(0,10)]
    set_1= set(my_list1)
    set_2= set(my_list2)

    print(f'\n\tList 1: {my_list1}')
    print(f'\tList 2: {my_list2}')
    print(f'\n\tset 1: {set_1}')
    print(f'\tset 2: {set_2}')  

    show('Union',set_1 | set_2)
    show('Intersection',set_1 & set_2)
    show('Difference',set_1 - set_2)
    show('Symmetric difference',set_1 ^ set_2)

if __name__ == '__main__':
    run()
