def czy_sa_rowne(numbers_y):
    print(f"module name funkcji: {__name__}")
    # First, check if the first and last elements are integers
    if isinstance(numbers_y[0], int) and isinstance(numbers_y[-1], int):
        if numbers_y[0] == numbers_y[-1]:
            print(f'{numbers_y[0]} , {numbers_y[-1]} - są równe')
            return True
        else:
            print(f'{numbers_y[0]} , {numbers_y[-1]} - NIE są równe')
            return False
    else:
        try:
            # Try to convert the first and last elements to integers if they aren't already
            a = int(numbers_y[0])
            b = int(numbers_y[-1])

            if a == b:
                print(f'{a} , {b} - sa rowne a jedna z liczb, albo obydwie, sa zapisana jako string')
                return True
            else:
                print(f'{a} , {b} - NIE sa rowne a jedna z liczb, albo obie, sa zapisana jako string')
                return False
        except ValueError:
            # Handle cases where the first or last element is not a valid integer
            if isinstance(numbers_y[0], str) and numbers_y[0].isalpha():
                print(f'{numbers_y[0]} - to nie jest liczba')
            if isinstance(numbers_y[-1], str) and numbers_y[-1].isalpha():
                print(f'{numbers_y[-1]} - to nie jest liczba')
                return False

