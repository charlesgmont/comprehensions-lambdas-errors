def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
    #usando excepciones con try y except
    try:
        num = int(input("Ingresa numero"))
        print(divisors(num))
        print("Terminó mi programa")
    except ValueError:
        print("Debes ingresar un número")


if __name__ == '__main__':
    run()