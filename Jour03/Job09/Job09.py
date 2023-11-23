def moyenne(num1, num2, num3):
    result = (num1 + num2 + num3) / 3
    if 15 <= result <= 20:
        return "tres bon eleve"
    elif 11 <= result  <= 14:
        return "Bon eleve"
    elif 8 <= result <= 10:
        return "eleve moyen"
    elif 0 <= result <= 7:
        return "elève devant faire des efforts"
    else:
        return "error"

print(moyenne(12, 12, 12))
