
import random

from collections import defaultdict


def reservoir_sampling(arr):

    reservoir = [arr[0]]

    for i in xrange(1, len(arr)):

        # Pick every element with i / i + 1 probability, if so, replace reservoir and continue

        picked = random.choice(range(0, i+1))
        if picked == i:
            reservoir[0] = arr[i]

    return reservoir[0]


if __name__ == "__main__":
    arr = range(0, 6)
    counts = defaultdict(int)
    n = 1000000
    for i in xrange(0, n):
        counts[reservoir_sampling(arr)] += 1

    for val in arr:
        print "Randomly sampled: {} with frequency {}".format(val, counts[val] / float(n))



