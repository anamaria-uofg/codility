# missinginteger

def solution(A):
    # Implement your solution here
    sA = sorted(A)
    mina = 1
    for a in sA:
        if a == mina:
            mina+=1
    return mina
