import sys
for k in sys.stdin:
    
    a,b=map(int,k.split())
    if a!=0 and b!=0:
        print(a+b)