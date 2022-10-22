import random
import os

# def remove_duplicates(some_list):
#     without_duplicates = []
#     for element in some_list:
#         if element not in without_duplicates:
#             without_duplicates.append(element)
#     return without_duplicates

def remove_duplicates(some_list):
    remove_set = set(some_list)
    return remove_set


def main():
    os.system('clear')
    random_list = [random.randint(1,5) for _ in range(0,10)]
    print(f'Lista inicial: {random_list}')
    print(f'Lista sin duplicados: {remove_duplicates(random_list)}')

if __name__ == '__main__':
    main()
    
    
