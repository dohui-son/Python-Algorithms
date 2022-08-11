def Solution(A):
    if len(A) <= 1: return len(A)
    return len(set(A))