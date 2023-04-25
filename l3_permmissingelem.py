# get the missing element from a list with consecutive numbers
# solution based on the fact that 
# the sum of the consecutive numbers (permutation) - the sum of the given array 
# = exactly the missing number

def solution(A):
    # Implement your solution here
    n = len(A)+1
    actual_sum = n*(n+1)//2

    return actual_sum - sum(A)

# https://app.codility.com/demo/results/trainingAABRMV-2P3/