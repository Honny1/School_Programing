import time
import random
p=[]
def radnomP():
    p=[]
    start_time = time.time()
    for i in range(9999):
        p.append(random.randint(0,9999))

    print(p)
    print("--- %s seconds ---" % (time.time() - start_time))
    return p

def bubleSort():
    p=radnomP()
    start_time = time.time()
    print("Buble Sort")
    for i in range(len(p)-1):
            for j in range(len(p)-1):
                  if p[j] >  p[j+1]:
                      pom = p[j]
                      p[j] = p[j + 1]
                      p[j + 1] = pom
    print(p)
    print("--- %s seconds ---" % (time.time() - start_time))

def bubleSortOptimalizet():
    p=radnomP()
    start_time = time.time()
    print("Buble Sort- optimalizet")
    zmena = True
    while (zmena):
        zmena = False;
        for j in range(len(p)-1):
            if (p[j]>p[j+1]):
                    pom=p[j]
                    p[j]
                    p[j+1]=pom
                    zmena = True
    print(p)
    print("--- %s seconds ---" % (time.time() - start_time))


bubleSort()
bubleSortOptimalizet()