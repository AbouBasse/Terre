try:
    from datetime import datetime


    def f_conversion(t):
        var = datetime.strptime(t, "%I:%M %p")
        v_res = datetime.strftime(var, "%H:%M")

        print("Le format 24 heures de", t, "est", v_res, ".")


    v_heure = input("Saisi l'heure en format 12 heures (sans les secondes): ")
    f_conversion(v_heure)
except ValueError:
    print("Erreur.")
