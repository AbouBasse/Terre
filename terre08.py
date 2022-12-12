try:
    import time
    print("Je vais t'afficher les résultat d'une puissance")
    time.sleep(2)
    a = int(input("Saisi un premier nombre: "))
    b = int(input("Saisi un deuxieme nombre: "))
    result = a**b
    if result < 0:
        print("Le resultat ne peut pas être négatif.")
    else:
        print(result)
except ValueError:
    print("Tu veux pas grandir.")
except ZeroDivisionError:
    print("0 ne peut pas être calculé via une puissance négative.")
