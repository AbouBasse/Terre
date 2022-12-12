try:
    n1 = int(input("Saisi un premier nombre: "))
    n2 = int(input("Saisi un deuxième nombre: "))
    n3 = int(input("Saisi un troisième nombre: "))
    if (n1 <= n2) and (n1 >= n3):
        moy = n1
    elif (n2 <= n3) and (n2 >= n1):
        moy = n2
    elif (n3 <= n1) and (n3 >= n2):
        moy = n3
    elif (n1 <= n3) and (n1 >= n2):
        moy = n1
    elif (n2 <= n1) and (n2 >= n3):
        moy = n2
    elif (n3 <= n2) and (n3 >= n1):
        moy = n3
    print("La valeur du mileu est :", moy, "!")
except ValueError:
    print("Erreur. Un nombre")
