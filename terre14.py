try:
    nbr_utl = list(
        map(
            int,
            input("Saisi des nombres et je te dirais si ils sont trié ou pas: ").split()
        )
    )
    y = sorted(nbr_utl)
    if nbr_utl == y:
        print("T'es nombres sont triée!")
    else:
        print("Tes nombres ne sont pas triée.")
except ValueError:
    print("Erreur, des nombres.")

# https://bobbyhadz.com/blog/python-input-space-separated-integers
# http://pascal.ortiz.free.fr/contents/python/tri/tri.html
