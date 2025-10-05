def cuenta_regresiva(n:int) -> None:
    while n>0:
        print(n)
        n -=1
    print("¡Despegue!")

if __name__ == "__main__":
    cuenta_regresiva(5)