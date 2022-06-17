def latinSq_Permutation(input, L, opt):
    output = [[] for i in range(256)]
    tmp = []
    if opt == None: opt = 'encryption'

    if opt == 'encryption':
        for i in range(256): tmp.append(input[i][(L[i]+1)]) #row permutations
        for x in range(256): 
            for y in range(256): output[y].append(tmp[(L[y][x]+1)][x]) #column permutations

    if opt == 'decryption':
        for x in range(256):
            for y in range(256): tmp[(L[y][x]+1)][x] = input[y][x]
        for i in range(256): output[i][(L[i]+1)] = tmp[i]
    return output