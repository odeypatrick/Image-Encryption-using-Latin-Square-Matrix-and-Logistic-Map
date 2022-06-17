# FUNCTION: RandomKey
# -- Generates a 256-bit random key (in HEX) using MATLAB RNG
# Output:
#       K = a 256-bit random key in HEX

from numpy import shape,random,array

def dec2hex(string, length):
    hex_string = ''
    if len(hex(string)) < length: hex_string = hex(string)[:2]+'0'*(8-len(hex(string)))+hex(string)[3:]
    else: hex_string = hex(string)
    return hex_string

def RandomKey():
    K = []
    r = []
    sr = ''
    r_ = random.rand(1,256)
    for i in range(256): r.append(round(r_[0][i]))
    for i in range(256): r[i] = str(r[i])[0]
    for i in range(1,9):
        K.append(dec2hex(int(sr.join(r[((i-1)*32):i*32]),2),8))
    return array(K)
RandomKey = RandomKey()
#print(shape(RandomKey))
