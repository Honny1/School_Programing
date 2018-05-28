import sortMethods

sortMethods.save()
idk = True
while idk == True:
    print("++++++  vyber radici operaci  ++++++++++\n")
    print("1 BubleSort")
    print("2 OptimalizetBubleSort")
    print("3 InsertSort")
    print("4 SelectSort")
    print("5 QuickSort")
    print("0 End")
    print("\n")
    x=input("vyber radici operaci : ")
    if x == "1":
        print(sortMethods.bubleSort(sortMethods.read()))
    elif x == "2":
        print(sortMethods.bubleSortOptimalizet(sortMethods.read()))
    elif x == "3":
        print(sortMethods.insertSort(sortMethods.read()))
    elif x == "4":
        print(sortMethods.selectSort(sortMethods.read()))
    elif x == "5":
        print(sortMethods.quickSort(sortMethods.read()))
    elif x == "0":
        idk = False
    else:
        print("chybne zadana radici operace")