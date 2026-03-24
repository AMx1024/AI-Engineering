import numpy as np
from scipy.linalg import hessenberg


def Gauss_Elimination(A, b):
    A = A.astype(float).copy()
    b = b.astype(float).copy()
    n = A.shape[0]

    if A.shape[0] != A.shape[1] or A.shape[0] != b.shape[0]:
        return None

    for i in range(n):
        pivot_row = np.argmax(np.abs(A[i:, i])) + i

        if abs(A[pivot_row, i]) < 1e-12:
            return None

        A[[i, pivot_row], :] = A[[pivot_row, i], :]
        b[[i, pivot_row]] = b[[pivot_row, i]]
        
        for j in range(i + 1, n):
            factor = A[j, i] / A[i, i]
            A[j, i:] -= factor * A[i, i:]
            b[j] -= factor * b[i]

    x = np.zeros(n)

    for i in range(n - 1, -1, -1):
            b_i = b[i]
            x[i] = (b_i - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]

    return x

def LU_decomposition(A, b):
    A = A.astype(float).copy()
    b = b.astype(float).copy()
    n = A.shape[0]
    if A.shape[0] != A.shape[1]:
        return None

    L = np.eye(n)
    U = A.copy()
    P = np.eye(n)

    for i in range(n):
        pivot = np.argmax(np.abs(U[i:, i])) + i

        if abs(U[pivot, i]) < 1e-12:
            return None

        if pivot != i:
            U[[i, pivot], :] = U[[pivot, i], :]
            P[[i, pivot], :] = P[[pivot, i], :]
            if i > 0:
                L[[i, pivot], :i] = L[[pivot, i], :i]

        for j in range(i + 1, n):
            factor = U[j, i] / U[i, i]
            L[j, i] = factor
            U[j, i:] -= factor * U[i, i:]
    
    b = P @ b
    y = np.zeros(n)    
    for i in range(n):
        y[i] = b[i] - np.dot(L[i, :i], y[:i])

    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i+1:], x[i+1:])) / U[i, i]
    return x

def eigenvalues(A):
    A=hessenberg(A.astype(float).copy())
    tol=1e-10
    max_iter=200
    n=A.shape[0]
    eigs=[]
    while n>1:
        for _ in range(max_iter):
            d=(A[n-2,n-2]-A[n-1,n-1])/2
            sign=1 if d>=0 else -1
            mu=A[n-1,n-1]-sign*(A[n-1,n-2]**2)/(abs(d)+np.sqrt(d**2+A[n-1,n-2]**2))
            Q,R=np.linalg.qr(A[:n,:n]-mu*np.eye(n))
            A[:n,:n]=R@Q+mu*np.eye(n)
            if abs(A[n-1,n-2])<tol*(abs(A[n-2,n-2])+abs(A[n-1,n-1])):
                eigs.append(A[n-1,n-1])
                n-=1
                break
        else:
            eigs.append(A[n-1,n-1])
            n-=1
    eigs.append(A[0,0])
    return np.array(eigs)

def eigenvectors(A):
    A = A.astype(complex)
    n = A.shape[0]

    eigvals = np.roots(np.poly(A))
    eigvals = np.unique(np.round(eigvals, decimals=8))  
    eigenvectors_list = []

    for lam in eigvals:
        M = A - lam * np.eye(n)
        M = M.copy()

        pivot_cols = []
        row = 0

        for col in range(n):
            if row >= n:
                break
            pivot = np.argmax(np.abs(M[row:, col])) + row
            if abs(M[pivot, col]) < 1e-10:
                continue
            if pivot != row:
                M[[row, pivot], :] = M[[pivot, row], :]

            pivot_cols.append(col)
            M[row] = M[row] / M[row, col]

            for r in range(row + 1, n):
                M[r] -= M[r, col] * M[row]
            row += 1

        for i in range(len(pivot_cols) - 1, -1, -1):
            col = pivot_cols[i]
            for r in range(i):
                M[r] -= M[r, col] * M[i]

        rank = len(pivot_cols)
        nullity = n - rank
        if nullity == 0:
            continue
        free_vars = [i for i in range(n) if i not in pivot_cols]

        for free_var in free_vars:
            v = np.zeros(n, dtype=complex)
            v[free_var] = 1

            for i, col in enumerate(pivot_cols):
                v[col] = -np.dot(M[i, free_vars], v[free_vars])
            norm = np.linalg.norm(v)
            if norm > 1e-12:
                v /= norm

            eigenvectors_list.append(v)

    if eigenvectors_list:
        return np.column_stack(eigenvectors_list)
    return None
    
def inverse(A):
    n = A.shape[0]
    if A.shape[0] != A.shape[1]:
        return None

    aug = np.hstack([A.astype(float), np.eye(n)])

    for i in range(n):
        pivot = np.argmax(np.abs(aug[i:, i])) + i
        if abs(aug[pivot, i]) < 1e-12:
            return None

        if pivot != i:
            aug[[i, pivot], :] = aug[[pivot, i], :]

        aug[i, :] /= aug[i, i]

        for j in range(n):
            if j != i:
                factor = aug[j, i]
                aug[j, :] -= factor * aug[i, :]
                aug[j, i] = 0.0
    return aug[:, n:]
