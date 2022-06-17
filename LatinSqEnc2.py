from numpy import *
from operator import xor
import LatinSq_Whitening, LatinSq_Permutation, LatinSq_Substitution, KeyedLatin
from RandomKey import RandomKey
from skimage import io

def bitget(x,y):
    bit = int(bin(x[0][y])[2:])
    return bit

def LatinSqEnc2(P,K=None):
    #Generate a random key
    if K == None:
        K_ = None
        K = RandomKey
        opt = 'NPE'

    #Probabilistic encryption
    #Generate a random 256x256 Latin
    M_ = random.rand(shape(P)[0],shape(P)[1])
    M = [[] for i in range(256)]
    for x in range(256):
        for y in range(256): M[x].append(int(round(M_[x][y])))
    M = array(M)
            
    #Random masking
    B = bitget(P,1)
    X = xor(B,M)
    PP = P-B+X
    #Generate 8-keyed Latin squares
    L = KeyedLatin(K,9)

    #Cipher rounds
    for i in range(8):
        #Extract a Keyed Latin Square
        tL = L[i]
        if i == 1: CP = PP
        #Latin Square Whitening
        CW = LatinSq_Whitening(CP,tL,'encryption')
        #Latin Square Substitution
        #if i%2 == 0: CS = LatinSq_Substitution(CW,tL,'row','encryption')
        #else: CS = LatinSq_Substitution(CW,tL,'col','encryption')
        #Latin Square Permutation
        CP = LatinSq_Permutation(CW,tL,'encryption')
    C =  LatinSq_Whitening(CP,L[8],'encryption')

    #Output Control
    if K_ == None: return C
    else: return (C,K)

img = r"C:\Users\HP\Downloads\Image-Encryption-using-Latin-Squares-master\upload\pep.png"
P = io.imread(img)
LE = LatinSqEnc2(P)
io.imsave('latinEnc.png',LE[0])
