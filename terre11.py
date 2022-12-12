try:
    from datetime import datetime


    def f_conversion(t):
        var = datetime.strptime(t, "%H:%M")  # Pour que ce soit en 12h->24h: "%I:%M %p"
        v_res = datetime.strftime(var, "%I:%M %p")  # Il faut aussi changer cette ligne en: "%H:%M"

        print("Le format 12 heures de", t, "est", v_res, ".")


    v_heure = input("Saisi l'heure en format 24 heures (sans les secondes): ")
    f_conversion(v_heure)
except ValueError:
    print("Erreur.")

# https://www.youtube.com/watch?v=VajYm5B4ytM&t=313s
# https://www.nbshare.io/notebook/510557327/Strftime-and-Strptime-In-Python/
