velikost = int(input("Velikost?: "))
pocet = int(input("kolik?: "))
j = 1
mezery = velikost
while j != velikost:
    radek = mezery * " " + j * "* "
    for i in range(pocet-1):
        radek += 2 * mezery * " " + j * "* "
    j += 1
    mezery -= 1
    print(radek)
while j != 0:
    radek = mezery * " " + j * "* "
    for i in range(pocet-1):
        radek += 2 * mezery * " " + j * "* "
    j -= 1
    mezery +=1
    print(radek)