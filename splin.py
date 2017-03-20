from sympy import *
#xl=[0.1,0.2,0.5,1,2]
#yl=[10,5,2,1,0.5]
xl=(raw_input("x: ")).split(",")
yl=(raw_input("y: ")).split(",")
for i in range(len(xl)):
    xl[i]=float(xl[i])
    yl[i]=float(yl[i])
x = symbols('x')
a = []
b = []
c = []
d = []
splines=[]
print "*** PASO 1 ****"
print "----------------------------------"
for i in range(1,len(xl)): 
    a.append(symbols('a'+str(i)))
    b.append(symbols('b'+str(i)))
    c.append(symbols('c'+str(i)))
    d.append(symbols('d'+str(i)))
    splines.append(a[i-1]*x**3+b[i-1]*x**2+c[i-1]*x+d[i-1])
    p=together(splines[i-1],x)
    pprint(p,use_unicode=True)
    print " S%d(x) -> x E [%.2f,%.2f]"%(i,xl[i-1],xl[i])
    print "----------------------------------"
print "\n*** PASO 2 ****"
print "----------------------------------"
print "S1(%.2f) = %.2f"%(xl[0],yl[0])
p=together(splines[0].subs(x,xl[0]),x)
pprint(p,use_unicode=True)
print " = %.2f"%yl[0]
print "----------------------------------"
for i in range(1,len(xl)-1):
    print "S%d(%.2f) = %.2f"%(i,xl[i],yl[i])
    p=together(splines[i-1].subs(x,xl[i]),x)
    pprint(p,use_unicode=True)
    print " = %.2f"%yl[i]
    print "----------------------------------"
    print "S%d(%.2f) = %.2f"%(i+1,xl[i],yl[i])
    p=together(splines[i].subs(x,xl[i]),x)
    pprint(p,use_unicode=True)
    print " = %.2f"%yl[i]
    print "----------------------------------"
print "S%d(%.2f) = %.2f"%(len(xl),xl[len(xl)-1],yl[len(yl)-1])
p=together(splines[len(splines)-1].subs(x,xl[len(xl)-1]),x)
pprint(p,use_unicode=True)
print " = %.2f"%yl[len(yl)-1]
print "----------------------------------\n"
print "*** PASO 3 ****"
primera_derivada=[]
print "----------------------------------"
for i in range(len(splines)):
    d=diff(splines[i],x)
    p=together(d,x)
    pprint(p,use_unicode=True)
    primera_derivada.append(d)
    print " S'%d(x) -> x E [%.2f,%.2f]"%(i+1,xl[i],xl[i+1])
    print "----------------------------------"
print "\n*** PASO 4 ****"
print "----------------------------------"
for i in range(1,len(primera_derivada)):
    p=together(primera_derivada[i-1].subs(x,xl[i]),x)
    pprint(p,use_unicode=True)
    print "       ="
    p=together(primera_derivada[i].subs(x,xl[i]),x)
    pprint(p,use_unicode=True)
    print "----------------------------------"
print "\n*** PASO 5 ****"
segunda_derivada=[]
print "----------------------------------"
for i in range(len(primera_derivada)):
    d=diff(primera_derivada[i],x)
    p=together(d,x)
    pprint(p,use_unicode=True)
    segunda_derivada.append(d)
    print ' S"%d(x) -> x E [%.2f,%.2f]'%(i+1,xl[i],xl[i+1])
    print "----------------------------------"
print "\n*** PASO 6 ****"
print "----------------------------------"
for i in range(1,len(segunda_derivada)):
    p=together(segunda_derivada[i-1].subs(x,xl[i]),x)
    pprint(p,use_unicode=True)
    print "       ="
    p=together(segunda_derivada[i].subs(x,xl[i]),x)
    pprint(p,use_unicode=True)
    print "----------------------------------"
print "\n*** PASO 7 ****"
print "----------------------------------"
print ' S"(x0)=0 si x=%.2f'%(xl[0])
p=together(segunda_derivada[0].subs(x,xl[0]),x)
pprint(p,use_unicode=True)
print " = 0"
print "----------------------------------"
print ' S"(xn)=0 si x=%.2f'%(xl[len(xl)-1])
p=together(segunda_derivada[len(segunda_derivada)-1].subs(x,xl[len(xl)-1]),x)
pprint(p,use_unicode=True)
print " = 0"
print "----------------------------------"