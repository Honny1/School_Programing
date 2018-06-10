#5
def opakovanyCifernySoucet(num):
    sNum=str(num)
    x=0
    for i in range(len(sNum)):
        x+=int(sNum[i])
    if (10<x):
       return opakovanyCifernySoucet(x)
    else:
        return x

print("123:", opakovanyCifernySoucet(123))
print("123456789:", opakovanyCifernySoucet(123456789))
print("99989788879879:", opakovanyCifernySoucet(99989788879879))

#6
def nejakasrackakterjeprimitivnianebavimealejeizijakdvaspizi(str1,str2):
    rString=""
    if len(str1)<len(str2):
        asdf=len(str1)
    else:
        asdf=len(str2)
    for i in range(asdf):
        if str1[i]==str2[i]:
            rString+=str1[i]
    return rString

print(nejakasrackakterjeprimitivnianebavimealejeizijakdvaspizi("picajedepomasle","picanejedepomasle"))

#7
def zasifruj(string,key):
    def sString(string, key):
        return [string[i:i + key] for i in range(0, len(string), key)]
    sStr=sString(string,key)
    nStr=""
    for i in range(len(sStr)):
        for j in reversed(sStr[i]):
            nStr+=j
    return nStr

print(zasifruj("HESLOJETAJEMNO",3))
print(zasifruj("123456789",2))