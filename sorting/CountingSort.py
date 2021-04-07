from collections import defaultdict

def countingSortRecursive(A, key=lamda x: x):
    B, C = [], defaultdict(list)
    def countingSortPriv(A)
        if len(A) < 1: return B
        else:
            C[key[A[0]]].append(A[0])
            for k in range(min(C), max(C)+1):
                B.extend(C[k])
            countingSortPriv(A[1:])
    return countingSortPriv(A)
        