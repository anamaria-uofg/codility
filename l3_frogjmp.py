# get the number of steps of distance D it takes 
# to cover the array with starting point X and ending point Y

def solution(X, Y, D):
    # Implement your solution here
    return (Y-X+D-1)//D

# https://app.codility.com/demo/results/trainingUEY8F5-VM3/
# time complexity: O(1)