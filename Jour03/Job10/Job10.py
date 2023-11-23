def pair(num):
    if not isinstance(num,int) or num == 0:
        print("entre un nombre entier non nul")
    elif num % 2 == 0:
        print("nombre pair")
    else:
        print("nombre impair")

pair(17)