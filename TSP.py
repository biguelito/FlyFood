from distance import Distance
from bruteforce import BruteForce


if __name__ == '__main__':
    file = open("input.txt", "r")
    #flyfood
    ff = Distance(file)
    mtx = ff.matrix
    dist = ff.getDistances()

    print(ff.m, ff.n)
    for k, v in dist.items():
        print(k, ' = ', v)
    print('')

    BruteForce(dist)

    file.close()

