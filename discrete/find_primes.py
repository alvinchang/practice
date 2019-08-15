from math import sqrt, floor


def find_primes_naive(lower, upper):
    """
    Finds prime numbers within a range [lower, upper]

    Note: by definition 1 is not a prime number.

    Runtime: O(N*sqrt(N))
    Space: O(N) # need to store at most N primes.


    :param lower: the lower boundary
    :type lower: int

    :param upper: the upper boundary
    :type upper: int

    :return: a list of primes
    :rtype: List[int]
    """
    results = []
    for potential_prime in xrange(max(2, lower), upper + 1):

        is_prime = True
        for potential_factor in xrange(2, int(floor(sqrt(potential_prime))) + 1):
            if potential_prime % potential_factor == 0:
                is_prime = False
                break
        if is_prime:
            results.append(potential_prime)
    return results


def find_primes_sieve(lower, upper):
    """
    Finds prime numbers within a range [lower, upper].

    Creates a list of integers from [lower, upper], representing the flags whether or not it has been marked.

    Iterates over multiples of integers from lower, upper, and marks them as False (upper bounded by the
    range).


    Note: by definition 1 is not a prime number. And that by definition all even numbers with the exception of 2
    cannot be prime (as 2 will be one of its divisors).

    :param lower: the lower boundary
    :type lower: int

    :param upper: the upper boundary
    :type upper: int

    :return: a list of primes
    :rtype: List[int]
    """
    # used to more easily index into the flags.
    temp = [False for _ in xrange(0, max(2, lower))]

    flags = temp + [True for _ in xrange(max(2, lower), upper + 1)]

    result = []
    for _i in xrange(max(2, lower), upper + 1):
        multiple = 2
        multiple_of_i = _i * multiple
        while multiple_of_i <= upper:
            # print multiple_of_i
            flags[multiple_of_i] = False

            multiple += 1
            multiple_of_i = _i * multiple
        if flags[_i]:
            result.append(_i)
    return result
    # return [_i for _i in xrange(max(2, lower), upper+1) if flags[_i]]


if __name__ == "__main__":
    lower = 1
    upper = 100
    naive = find_primes_naive(lower, 100)
    sieve = find_primes_sieve(1, 100)
    assert naive == sieve
