import LatinSq_Whitening, LatinSq_Permutation, LatinSq_Substitution, KeyedLatin

def LatinSqDec2(C,K):
    #Generate Key-dependent 256x256 Latin Squares
    L = KeyedLatin(K,9)

    for i in range(7,-1,-1):
        #Extract a Keyed Latin Square
        tL = L[:][:][i]
        if i == 7: CW = LatinSq_Whitening(C,L[:][:][8],'decryption')

        #Latin Square Permutation
        CP = LatinSq_Permutation(CW,tL,'decryption')

        #Latin Square Substitution
        #if i%2 == 0: CS = LatinSq_Substitution(CP,tL,'row','decryption')
        #else: CS = LatinSq_Substitution(CP,tL,'col','decryption')
        
        #Latin Square Whitening
        CW = LatinSq_Whitening(CP,tL,'decryption')
    P = CW
    return P