#=============================================================
# FUNCTION: LatinSq_Whitening
# -- Generates n Latin square of order d dependent on key K
# Input:
#      inputMatrix = a 256x256 matrix, 
#                L = a 256x256 Latin square with symbol set {0,1,...,255}
#                opt = encryption/decryption
# Output:
#      output = a 256x256 matrix
#=============================================================

from numpy import *

def LatinSq_Whitening(inputMatrix,L,opt):
    if opt == None: opt = 'encryption'

    if opt == 'encryption':
        if L[0]%3 == 1: inputMatrix = flipud(inputMatrix)
        if L[0]%3 == 2: inputMatrix = fliplr(inputMatrix)
        output = (inputMatrix+L)%256

    if opt == 'decryption':
        output = (inputMatrix-L)%256
        if L[0]%3 == 1: output = flipud(output)
        if L[0]%3 == 2: output = fliplr(output)
    return output