#=============================================================
# FUNCTION: LatinSq_Subsititution
# -- Subsititute bytes with bytes in a chain-like way
# Input:
#       inputMatrix = a 256x256 matrix, 
#           L = a 256x256 Latin square with symbol set {0,1,...,255}
#        opt1 = 'row'/'column' substitutions
#        opt2 = 'encryption'/'decryption'
# Ouptut:
#      output = a 256x256 matrix
#=============================================================
# BSD licence 
#=============================================================
# By Yue (Rex) Wu (ywu03@tufts.ece.edu)
# ECE Department, Tufts University
# Mar 10, 2012
#=============================================================
from numpy import *
def sub2ind(x,y,z): pass
def LatinSq_Substitution(inputMatrix,L,opt1,opt2):
    output = array()
    if opt2 == None: opt2 = 'encryption'
    
    if opt2 == 'encryption':
        if opt1 == 'row':
                for i in range(256):
                    if i == 0: output[i] = L[1,inputMatrix[i]+1]
                    else:
                        idx = sub2ind([256,256],output[i-1]+1,inputMatrix[i]+1)
                        output[i] = L(idx)
        if opt1 == 'col':
                for i in range(256):
                    if i == 1: output[:][i] = L[inputMatrix[:][i]+1][1]
                    else:
                        idx = sub2ind([256,256],inputMatrix[:][i]+1,output[:][[i-1]+1])
                        output[:][i] = L[idx]
    if opt2 == 'decryption':
        if opt1 == 'row':
                LR = zeros(256)
                for i in range(256):
                    LR[i][L[i]+1] = [255]
                for i in range(256,1,-1):
                    if i == 1:
                        idx = sub2ind([256,256],ones(1,256),inputMatrix[i]+1)
                        output[i] = LR(idx)
                    else:
                        idx = sub2ind([256,256],inputMatrix[i-1]+1,inputMatrix[i]+1)
                        output[i] = LR(idx)

        if opt1 == 'col':
                LC = zeros(256)
                for i in range(256):
                    LC[i][L[i]+1] = [255]

                for i in range(256,1,-1):
                    if i == 1:
                        idx = sub2ind([256,256],inputMatrix[:i]+1,ones(256,1))
                        output[:i] = LC(idx)
                    else:
                        idx = sub2ind([256,256],inputMatrix[:i]+1,inputMatrix[:][i-1]+1)
                        output[:i] = LC(idx)
    return output