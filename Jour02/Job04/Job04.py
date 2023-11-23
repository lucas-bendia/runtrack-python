N = int(input("Veuillez saisir un entier N (supérieur à zéro) : "))

if N > 0:
    for i in range(1, N + 1):
        print(f"\nTable de multiplication pour {i} :")
        for j in range(1, 11):
            produit = i * j
            print(f"{i} x {j} = {produit}")
else:
    print("Veuillez saisir un entier supérieur à zéro.")
