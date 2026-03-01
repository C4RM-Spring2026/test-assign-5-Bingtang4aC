import numpy as np

def getBondPrice(y, face, couponRate, m, ppy=1):
    pvcfsum = 0
    cf = face * couponRate / ppy
    
    n = int(m * ppy)
    t = np.array(range(1, n + 1))
    
    r = y / ppy
    pvm = (1 + r) ** (-t)

    cf = np.array([cf] * n)
    cf[-1] += face

    pvcf = pvm * cf
    pvcfsum += np.sum(pvcf)

    return pvcfsum
