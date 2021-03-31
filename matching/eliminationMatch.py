def elimination_match(M, A=None):
    if A is None:
        A = set(range(len(M)))
    B = [0]*len(A)
    for [i] in M:
        B[i] += 1
    def elimination_match_priv(M, A, B):
        if len(A) == 1: return A
        else:
            C = indexOf(0 in B) # rewrite
            j = M(C.pop())
            B[j] -= 1
            A.remove[C]
            B.remove[C]
            M.remove[C]
            return elimination_match_priv(M, A, B)
    return elimination_match_priv(M, A, B)