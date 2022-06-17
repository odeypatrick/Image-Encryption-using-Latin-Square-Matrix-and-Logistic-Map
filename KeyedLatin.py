#Define LCG and LSG
#from curses import qiflush
#function L = KeyedLatin(K,m)
#=============================================================
# FUNCTION: KeyedLatin
# -- Generates n Latin square of order d dependent on key K
# Output:
#       L = 256-by-256-by-m matrix, each of whose layer is a 256x256 Latin
#       square using the symbol set {1,2,...,256}
#=============================================================
# BSD licence 
#=============================================================

#import numpy as np
from numpy import *
from RandomKey import RandomKey

def blockproc(matrix,sec,fun):
    #print(shape(matrix))
    blocks = []
    matrix_bp = [[]]
    matrix_b = [[] for i in range(256)]
    if sec == 8:
        blocks = array_split(matrix,sec)
        for block in blocks:
            m = fun(block[0])
            matrix_bp[0].append(m)
        matrix_bp = array(matrix_bp)
        return matrix_bp
        
    if sec == 256:
        blocks = array_split(matrix,sec)
        for block in blocks:
            m = fun(block)
            for x in range(256): matrix_b[x].append(m[x][0])
        matrix_b = array(matrix_b)
        return matrix_b
    #print(shape(matrix_b))
    

def KeyedLatin(K,m):
    a = 1664525
    c = 1013904223 #LCG parameters suggested in Numerical Recipe
    #Linear Congruential Generator (LCG) PRNG
    lcg = lambda q: (a * q + c) %2**32 

    #Latin Square Generator (LSG) using Row-Shiftings
    lsg_r = lambda qSeed, v: (qSeed+v) %256
    lsg = lambda qSeed, qShift: blockproc(qShift, 256, lambda v: lsg_r(qSeed,v))

    ## Define Key Conversions 
    # Convert Hex Key string to dec sequence
    key_hex_bin = lambda K: blockproc(K,8,lambda k: int(str(k),16))

    
    ##Generate n Latin squares of order 256
    KDec = key_hex_bin(K) #KDec is a 1x8 array
    #print(KDec)
    L = []

    for n in range(m):
        q = []
        for i in range(64):
            if i == 0: q.append(lcg(KDec))
            else: q.append(lcg(q[i-1]))
        Q1 = []
        Q2 = []
        for x in range(32):
            for y in range(8): Q1.append(q[x][0][y])
        for x in range(32,64):
            for y in range(8): Q2.append(q[x][0][y])
        #a 256-element LCG squence
        #a 256-element LCG squence
        KDec = q[-1]    #update Key
        Qseed =  sort(Q1)
        Qshift = sort(Q2)
        '''
        Qseed = []
        Qshift = []

        Qseed = [Qseed_[i][0] for i in range(32)]
        Qshift = [Qshift_[i][0] for i in range(32)]
        '''
        Qseed = array([Qseed])
        Qshift = array(Qshift)

        #print('Qseed: ',shape(transpose(Qseed)))
        #print('Qsshift: ',shape(Qshift))

        L.append(lsg(transpose(Qseed),Qshift))
        #print(shape(L))
    
    return array(L)

#latin = KeyedLatin(RandomKey,9)
#print((latin))

