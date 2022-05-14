
num=int(input("DIGITE UM NUMERO:"))
s= 0
for n in range(1, num+1):
    if num % n == 0:
         s += 1
if s == 2 :
    print("Esse numero é primo")
else:
    print("Esse numero não é primo ")