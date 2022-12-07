from math import * # kohal muudaja
print("Ruudu karakteristikud")
a=float(input("Sisesta ruudu külje pikkus => ")) # lisa float ja sulgid, muutaja "
S=a**2
print("Ruudu pindala", round(S,1))
P=4*a
print("Ruudu ümbermõõt",round(P,1)) # ei suletud " ja lisa round
di=a*sqrt(2) # kiruta sqrt
print("Ruudu diagonaal", round(di,2))
print()
print("Ristküliku karakteristikud") # üleliigne sulg
b=float(input("Sisesta ristküliku 1. külje pikkus => ")) # lisa float
c=float(input("Sisesta ristküliku 2. külje pikkus => ")) # lisa float
S=b*c
print("Ristküliku pindala", round(S,1)) # ei suletud "
P=2*(b+c) # lisa *
print("Ristküliku ümbermõõt", round(P,1)) # lisa round
di=sqrt(b*2+c*2)# math kustutada
print("Ristküliku diagonaal", round(di,1)) # suletud sulg
print()
print("Ringi karakteristikud")
r=float(input("Sisesta ringi raadiusi pikkus =>")) # lisa float
d=2*r # lisa *
print("Ringi läbimõõt", d) # lisa komma
S=pi*r**2 # lisa r**2 ja kustutada()
print("Ringi pindala", round(S,1))
C=2*pi*r # 
print("Ringjoone pikkus", round(C,2))
