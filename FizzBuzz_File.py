import numpy as np

def FizzBuzz(start, finish):
    numvec = np.arange(start, finish + 1)
    objvec = np.array(numvec, dtype=object)

    fizz = (numvec % 3 == 0)
    buzz = (numvec % 5 == 0)

    objvec[fizz] = "fizz"
    objvec[buzz] = "buzz"
    objvec[fizz & buzz] = "fizzbuzz"

    return objvec.tolist()
