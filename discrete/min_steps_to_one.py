
"""

On a positive integer, you can perform any one of the following 3 steps.

1.) Subtract 1 from it. ( n = n - 1 )
2.) If its divisible by 2, divide by 2. ( if n % 2 == 0 , then n = n / 2  )
3.) If its divisible by 3, divide by 3. ( if n % 3 == 0 , then n = n / 3  ).

Given a positive integer n, find the minimum number of steps that takes n to 1

"""

def min_steps_to_one_rec_memo(integer):
    memo = {}
    return min_steps_to_one_rec(integer, memo)

def min_steps_to_one_rec(integer, memo):

    if integer == 1:
        return 0

    if integer in memo:
        # print 'hit memo int={}'.format(integer)
        return memo[integer]

    steps = 1 + min_steps_to_one_rec(integer - 1, memo)

    if integer % 2 == 0:
        steps = min(steps, 1 + min_steps_to_one_rec(integer / 2, memo))

    if integer % 3 == 0:
        steps = min(steps, 1 + min_steps_to_one_rec(integer / 3, memo))

    memo[integer] = steps

    return steps

def min_steps_to_one_dp(integer):
    """
    Recurrence relation = F(n) = min ( f(n-1), f(n/2), f(n/3) ) + 1
    :param integer:
    :return:
    """

    table = [-1 for _ in xrange(0, integer+1)]
    table[0] = 0
    table[1] = 1
    table[2] = 1
    table[3] = 1

    for i in xrange(4, integer+1):

        min_steps = table[i-1]
        if i % 2 == 0:
            min_steps = min(table[i/2], min_steps)
        if i % 3 == 0:
            min_steps = min(table[i/3], min_steps)
        table[i] = min_steps + 1

    return table[integer]


if __name__ == "__main__":
    n = 500
    print min_steps_to_one_rec_memo(n)
    print min_steps_to_one_dp(n)
