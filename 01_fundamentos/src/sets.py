def demo_sets():
    frutas = {"manzana", "pera", "manzana", "plátano"}
    print("Set (sin duplicados):", frutas)

    frutas.add("uva")
    print("Después de add:", frutas)

    frutas.remove("pera")
    print("Despues de remove:", frutas)

    otras = {"kiwi", "manzana"}
    print ("Unión:", frutas | otras)
    print ("Intersección:", frutas & otras)
    print ("Diferencias:", frutas - otras)

if __name__ == "__main__":
    demo_sets(

    )