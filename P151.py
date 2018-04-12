while (True):
 print("***cely soubor:***")
 try:
     f=open("VELKY.txt","r")
 except IOError:
     print("soubor neexistuje\n")
     break
 else:
     soubor = f.read()
     print(soubor)
     f.close()
     break



