def es_primo(n:int) -> bool:
    if n<=1:
        return False
    for i in range(2, int(n** 0.5) + 1):
        if n% i == 0:
            return False
    return True

if __name__ == "__main__":
    for num in [1, 2, 3, 4, 17, 20]:
        print(num, "->", es_primo(num))