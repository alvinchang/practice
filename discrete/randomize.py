import random

from collections import defaultdict


def reservoir_sampling(arr):
    reservoir = [arr[0]]

    for i in xrange(1, len(arr)):

        # Pick every element with i / i + 1 probability, if so, replace reservoir and continue

        picked = random.choice(range(0, i + 1))
        if picked == i:
            reservoir[0] = arr[i]

    return reservoir[0]


def fisher_yates_shuffle(arr):
    length = len(arr)
    for _i in xrange(length):
        random_int = random.randint(_i, length - 1)
        arr[_i], arr[random_int] = arr[random_int], arr[_i]


if __name__ == "__main__":
    upper = 10
    arr = range(0, upper)

    counts = defaultdict(lambda: defaultdict(int))

    n = 100000
    for _ in xrange(0, n):
        fisher_yates_shuffle(arr)
        for _i in xrange(len(arr)):
            counts[_i][arr[_i]] += 1

    for index in sorted(counts):
        print "index={}".format(index)
        for random_int, random_count in counts[index].iteritems():
            print "\ti={}, pr={}".format(random_int, random_count / float(n))

    # print arr

    # counts = defaultdict(int)
    # n = 1000000
    # for i in xrange(0, n):
    #     counts[reservoir_sampling(arr)] += 1
    #
    # for val in arr:
    #     print "Randomly sampled: {} with frequency {}".format(val, counts[val] / float(n))
