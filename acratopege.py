import msvcrt
from pylab import *
import csv

def ReadDbandCount():
    ndict={}
    lines=0
    f = open("stripped.csv","r")
    for line in f:
      lines=lines+1
      # if lines>10:break
      if msvcrt.kbhit(): break
      serie = line.split(',')
      print(serie[0])
      for i in range(1,len(serie)-1):
        try:
          n=int(serie[i])
        except:
          print("?")
        ndict.setdefault(n,0)
        ndict[n] = ndict[n]+1
    f.close()
    
    f = open("acra.csv","w")
    for i in range(1,100000):
      ndict.setdefault(i,0)
      print >>f, i,';',ndict[i]
    f.close()
    
def isprime(n): #http://www.daniweb.com/code/snippet651.html
    n = abs(int(n))
    if n < 2: return False
    if n == 2: return True
    if not n & 1: return False
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0: return False
    return True

def Divisors(n):
    if n==1:return [1]
    r=[1,n]
    sr=int(sqrt(n))
    for x in range(2, sr+1):
        if n % x == 0:
            r.append(x)
            r.append(n/x)
    if n==sr*sr:r.pop()
    return r

def ispower(x):  
    for i in range(2,math.log2(x)+1):
        s=x**(1./i)
        n=round(s,0)
        s=max(s,n)-min(s,n)
        if s<1e-9:return True
    return False

file = csv.reader(open('acra.csv'), delimiter=';', quotechar='"')
xx=[]; yy=[]; #properties of number
px=[]; py=[]; #primes
fx=[]; fy=[]; #powers
hx=[]; hy=[]; #powers
x=0
f=0
for row in file:
    x=int(row[0]); y=int(row[1])
    if isprime(x):
        px.append(x);
        py.append(y);
    else: 
        h=len(Divisors(x))
        if h>f:
            f=h
            hx.append(x);
            hy.append(y);
        else:
            if ispower(x):
                fx.append(x);
                fy.append(y);
            else:
                xx.append(x);
                yy.append(y);
            
semilogy(px,py,'ro')
semilogy(fx,fy,'go')
semilogy(hx,hy,'yo')
semilogy(xx,yy,'.')
axis([1,10000,1,10000])
show()