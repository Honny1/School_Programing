import subprocess
print("start")
file = open('C:\\HONYISGOD1.py', 'w')
file.write("import random\nA=[]\nS=[]\nf=0\nfile = open('D:\\HonyIsGod.txt','w')\na=2147483647\nfor j in range(a):\n	for i in range(a):\n		w=random.randint(0,2147483647)\n		x=str(w)\n		S.append(w)\n		file.write( ' '.join(str(x) for x in S));\n		A.append(S)\n	S=[]\n	file.write( ' '.join(str(x) for x in A));\nfile.close()\nfor i in range(a):\n	f+=A[i][i]\nprint('SoucetVDiagonale',f)")
file.close()
print("file done")
subprocess.call(["C:\\Users\\Honny\\AppData\\Local\\Programs\\Python\\Python36-32\\pythonw.exe", "HONYISGOD1.py"])
print("RIP")
input()
"""
import random
A=[]					
S=[]
f=0
file = open('D:\\HonyIsGod.txt','w')
a=2147483647 
for j in range(a): 				  
	for i in range(a): 
		w=random.randint(0,2147483647)
		x=str(w)
		S.append(w)  
		file.write( " ".join(str(x) for x in S));
		A.append(S)		
	S=[]
	file.write( " ".join(str(x) for x in A));
file.close()
for i in range(a):
	f+=A[i][i]
print("SoucetVDiagonale",f)    
"""
"""import os
os.startfile('textfile.txt')"""