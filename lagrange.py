from sympy import *
xl=(raw_input("x: ")).split(",")
yl=(raw_input("y: ")).split(",")
for i in range(len(xl)):
    xl[i]=int(xl[i])
    yl[i]=int(yl[i])
lagrange=0
x = symbols('x')
for j in range(len(yl)):
    lx=1
    for i in range(len(xl)):
        if j!=i:
            lx=lx*((x-xl[i])/(xl[j]-xl[i]))
    p=together(apart(lx,x),x)
    pprint(p,use_unicode=True)
    print "->>>>>>>> multiplicando por",yl[j]
    lx=lx*yl[j]
    p=together(apart(lx,x),x)
    pprint(p,use_unicode=True)
    print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
    lagrange=lagrange+lx
print "La funcion resultado es:"
p=together(apart(lagrange,x),x)
pprint(p,use_unicode=True)
print ""
print apart(p,x)

salida=1
while salida!=0:
    print "0 -> salida"
    print "1 -> probar x"
    print "2 -> graficar"
    leer=int(raw_input())
    if leer==0:
        salida = 0
    elif leer == 1:
        dato=int(raw_input("x: "))
        r=lagrange.subs(x,dato)
        print "Si X es",dato,"el resultado en Y es",r
    elif leer==2:
        Plot(lagrange)

