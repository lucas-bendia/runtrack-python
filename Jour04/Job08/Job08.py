def paires():
    L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]
    return sum(num for num in L if num %2 == 0)

print(paires())
