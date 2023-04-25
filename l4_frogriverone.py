# find the earliest time when the frog can jump to the other side of the river
# make a checklist where only unique elements are included

def solution(X, A):
    # Implement your solution here
    steps = list(range(1,X+1))
    
    checklist = set()

    for i in range(len(A)):
        checklist.add(A[i])
        if len(checklist) == X:
            return i 
    return -1