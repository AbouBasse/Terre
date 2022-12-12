try:
    import time
    print("Je vais te dire si le nombre que tu aura saisi est premier ou pas.")
    time.sleep(2)
    utl_nbr = int(input("Saisi un nombre: "))
    c = 0
    for i in range(1, utl_nbr+1):
        if utl_nbr % i == 0:
            c = c+1
    if c == 2:
        print("Oui,", str(utl_nbr), " est premier.")
    else:
        print("Non,", str(utl_nbr), " n'est pas premier.")
except ValueError:
    print("Erreur, je t'ai demandé un nombre.")
# https://www.youtube.com/watch?v=2YlvPHYuGho
