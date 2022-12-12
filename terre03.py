def alph_range(debut, fin):
    return (chr(n) for n in range(ord(debut), ord(fin) + 1))


utl_ltr = input("Saisi une lettre de l'alphabet: ")
for alph_utl in alph_range(utl_ltr, "z"):
    print(alph_utl)

# https://www.codingem.com/python-range-of-letters/
