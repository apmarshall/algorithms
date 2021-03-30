def elimination_match(M, A=None):
    if A is None:
        A = set(range(len(M)))
    def B_construct:
        B = [0*len(A)] # Rewrite
        for M[i] in A:
            B[i] += 1
    def B_reduction():
        # Reduce counts in B based on previous iteration
    def list_reduction(L, C):
        L.remove(C.pop())
    def elimination_match_priv(M, A, B):
        if len(A) == 1: return A
        else:
            C = indexOf(0 in B) # Rewrite
            B = B_reduction(B, C, M)
            A = list_reduction(A, C)
            B = list_reduction(B, C)
            return elimination_match_priv(M, A, B)
    return elimination_match_priv(M, A, B)