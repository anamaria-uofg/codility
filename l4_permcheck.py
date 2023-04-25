# check whether array A is a permutation using formula of permutation
# P = n(n+1)//2

def solution(A):
    # Implement your solution here
    n=len(A)
    s = list(set(A))
    suma = sum(s)
    permsum = n*(n+1)//2

    if suma == permsum:
        return 1
    return 0
