# genomic range query
# get weights of genomic subsequences

def solution(S, P, Q):
    # Implement your solution here
    weights = [] 
    
    for p,q in zip(P,Q):
        subs = S[p:q+1]
        if 'A' in subs:
            weight = 1
        elif 'C' in subs:
            weight = 2
        elif 'G' in subs:
            weight = 3
        elif 'T' in subs:
            weight = 4
    
        weights.append(weight)
    
    return weights