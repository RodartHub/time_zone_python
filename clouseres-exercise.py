def make_division_by(n: float) -> float:
    
    '''This clousure returns a function that return the division of an x number by n'''
    
    def division(x: float) -> float:
        assert type(x) == int, 'Solo puedes usar numeros'
        assert n != 0, 'No puedes dividir el numero entre cero'
        return x/n

    return division 

def main():
    division_by_3 = make_division_by(-1.2)
    print(division_by_3(2))

    division_by_5 = make_division_by(5)
    print(division_by_5(100))

    division_by_18 = make_division_by(18)
    print(division_by_18(54))

if __name__ == '__main__':
    main()
    