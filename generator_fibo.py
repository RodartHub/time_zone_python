import time
import os

def fibo_gen(max=None):
    n1 = 0
    n2 = 1
    counter = 0
    
    while True:
        if counter > max:
            break

        if counter == 0:
            counter += 1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2
        else:
            aux =n1 + n2
            n1, n2 = n2, aux
            counter += 1
            yield aux

if __name__ == '__main__':
    fibonacci  = fibo_gen
    os.system('clear')
    num = int(input('Introduce hasta què posiciòn de la sucesiòn de fibonacci deseas recorrer: '))
    for element in fibonacci(num):
        print(element)
        time.sleep(1)  
    print('Termino la ejecuciòn.')