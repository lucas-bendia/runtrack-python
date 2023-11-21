nom = "Tablette"

prix= 100

stock = 10

print(f"""Article : {nom}
    prix : {prix}
    stock : {stock}""")

saisie = int(input("Entrez la quantité que vous souhaitez acheter : "))

print (f"""Article : {nom}
    prix : {prix*1.1}
    stock : {stock-saisie}""")
