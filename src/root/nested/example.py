'''
Created on 6 feb. 2017

@author: Sophia
'''

midpoint = 5;
lower=[];
upper=[];

for i in range(10):
    if (i<midpoint):
        lower.append(i);
    else:
        upper.append(i);

print("lower:",lower);
print("upper",upper);

"""x = True;
x = 5j;
print(x.real, x.imag);
x = None;
print(type(x));"""

L = [2, 3, 5, 7];
print(len(L));
L.append(11);
L += [13, 17, 19];
L.sort();
print(L);


def fibonacci(N, a=0, b=0):
    if N<0:
        raise ValueError("N must be non-negative");
    L = []
    a, b = 0, 1
    while len(L) < N:
        a, b = b, a + b
        L.append(a)
    return L

print(fibonacci(10));

I = iter([2,4,6,8,10]);
a = True;
while a:
    try:
        a = next(I);
    except:
        break;
    print(a);
    
    
