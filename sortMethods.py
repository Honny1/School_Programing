import time
import random

p = []


def radnomP():
    p = []
    for i in range(9999):
        p.append(random.randint(0, 9999))
    return p


def bubleSort(p):
    start_time = time.time()
    print("Buble Sort")

    for i in range(len(p) - 1):
        for j in range(len(p) - 1):
            if p[j] > p[j + 1]:
                p[j], p[j + 1] = p[j + 1], p[j]

    print("--- %s seconds ---" % (time.time() - start_time))
    return p


def bubleSortOptimalizet(p):
    start_time = time.time()
    print("Buble Sort- optimalizet")

    zmena = True
    while (zmena):
        zmena = False
        for j in range(len(p) - 1):
            if (p[j] > p[j + 1]):
                p[j], p[j + 1] = p[j + 1], p[j]
                zmena = True

    print("--- %s seconds ---" % (time.time() - start_time))
    return p

def selectSort(p):
    start_time = time.time()
    print("Select Sort")

    for i in range(len(p)):
        mini = min(p[i:])
        min_index = p[i:].index(mini)
        p[i + min_index] = p[i]
        p[i] = mini

    print("--- %s seconds ---" % (time.time() - start_time))
    return p


def insertSort(p):
    start_time = time.time()
    print("Insert Sort")

    for i in range(1, len(p)):  #
        j = i
        temp = p[j]
        while j > 0 and temp < p[j - 1]:
            p[j] = p[j - 1]
            j = j - 1
        p[j] = temp

    print("--- %s seconds ---" % (time.time() - start_time))
    return p


def quickSort(p):
    def sort(array):
        less = []
        equal = []
        greater = []

        if len(array) > 1:
            pivot = array[0]
            for x in array:
                if x < pivot:
                    less.append(x)
                if x == pivot:
                    equal.append(x)
                if x > pivot:
                    greater.append(x)

            return sort(less) + equal + sort(greater)

        else:
            return array

    start_time = time.time()
    print("Quick Sort")
    w = sort(p)
    print("--- %s seconds ---" % (time.time() - start_time))
    return w


def toInt(pole):
    nPole = []
    x = pole[1:-1].split(", ")
    for i in range(len(x)):
        nPole.append(int(x[i]))
    return nPole


def save():
    f = open("pole.txt", "w")
    f.write(str(radnomP()))
    f.close()


def read():
    f = open("pole.txt", "r")
    soubor = f.read()
    f.close()
    return toInt(soubor)