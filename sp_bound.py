from sympy import binomial

n = 14
k = 8
q = 2
d = 5
s = 0
for i in range((d-1)//2+1):
    s += binomial(n, i)*(q-1)**i

C = q**n/s
print(q**k)
print(float(C))