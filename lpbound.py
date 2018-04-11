from scipy.optimize import linprog
from scipy.special import comb

def Krawtchouk(n, q, m, x):
    s = 0
    for i in range(m+1):
        s += comb(x, i)*comb(n-x, m-i)*(-1)**i*(q-1)**(m-i)
    return s

def LP_Bound(n, q, d):
    c = [-1 for i in range(n+1)]
    Q = [ [-Krawtchouk(n, q, i, j) for j in range(0,n+1)] \
           for i in range(0,n+1) ]    
    b_ub = [0 for i in range(n+1)]
    A_eq = [[0 for j in range(n+1)] for i in range(n+1)]
    for i in range(d):
        A_eq[i][i] = 1
    b_eq = [0 for i in range(n+1)]
    b_eq[0] = 1    
    print(Q)
    print(b_ub)
    res = linprog(c, Q, b_ub, A_eq, b_eq, options={"disp":True})
    return -res.fun
            
res = LP_Bound(12, 2, 6)