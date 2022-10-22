
import pyfiglet
import os

def ascii_name(func):
    def wrapper():
        print('Bienvenido a este generador de nombres ASCII')
        func()
        print('Hemos terminado. Espero que te guste')
    return wrapper

@ascii_name
def user_name():
    name = input('Por favor, ingresa un nombre: ')
    assert type(name) == str, 'Por favor ingresa un nombre vàlido'
    ascii_n = pyfiglet.figlet_format(name)
    print(ascii_n)


def main():
    os.system('clear')
    user_name()

if __name__ == '__main__':
    main()
    