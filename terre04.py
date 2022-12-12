try:
    import time
    print("Je vais te dire si le nombre que tu aura noté est pair ou impair.")
    time.sleep(2)
    nbr_utl = int(input("Saisi un nombre: "))
    if (nbr_utl % 2) == 0:
        print("Ce nombre est pair.")
    else:
        print("Ce nombre est impair.")
except ValueError:
    print("Pas à moi :)")
