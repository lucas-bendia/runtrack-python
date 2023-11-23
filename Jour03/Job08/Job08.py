def Tsaison(type,saison):
    if type == "fruit" and saison == "hiver":
        print ("orange, mandarine et kiwi")
    elif type == "fruit" and saison == "ete":
        print ("Poire, fraise, cassis")
    elif type == "legume" and saison == "hiver":
        print ("carotte, topinambour, endive")
    elif type == "legume" and saison == "ete":
        print ("artichaut, aubergine,navet")
    else:
        print("error")

Tsaison("fruit", "hiver")
