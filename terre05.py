try:
    import time
    print("Je vais faire une division euclidienne. ")
    time.sleep(2)
    a = int(input("Saisi un premier nombre: "))
    b = int(input("Saisi un deuxième nombre: "))
    reste = a
    quotient = 0
    while b <= reste:
        reste = reste-b
        quotient = quotient+1
    if quotient <= 0:
        print("Erreur.")
    else:
        print("Quotient =", quotient, "Reste =", reste)
except ValueError:
    print("Un nombre stp.")
# 0 ou un négatif au deuxieme nombre = soft lock.
# https://www.youtube.com/watch?v=xCBOvHL2seU
