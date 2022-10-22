
def is_primo(num:int)->bool:
    result = [x for x in range(1, num+1) if num % x == 0]
    if len(result) == 2:
        print(f'El numero {num} es primo')
    else:
        print(f'El numero {num} NO es primo')
    

def main():
    num = int(input('Ingresa un nùmero: '))
    is_primo(num)

if __name__ == '__main__':
    main()
    