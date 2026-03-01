import numpy as np

def getBondDuration(y, face, couponRate, m, ppy=1):
    pvcfsum = 0
    cf = face * couponRate / ppy
    
    n = int(m * ppy)
    t = np.array(range(1, n + 1))
    
    r = y / ppy
    pvm = (1 + r) ** (-t)

    cf = np.array([cf] * n, dtype=float)
    cf[-1] += face

    pvcf = pvm * cf
    pvcfsum += np.sum(pvcf)

    duration= np.sum(t*pvcf)/ pvcfsum

    return duration
