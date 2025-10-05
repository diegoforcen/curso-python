def clasificar_edad(edad: int) ->str:
    if edad < 0:
        return "Edad no válida"
    elif edad < 12:
        return "Niño"
    elif edad < 18:
        return "Adolescente"
    elif edad < 65:
        return "Adulto"
    else:
        return "Senior"

if __name__ == "__main__":
    for e in [-1, 8, 15, 30, 80]:
        print(f"{e} años -> {clasificar_edad(e)}")