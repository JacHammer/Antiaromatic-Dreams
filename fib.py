import time


def fib_n_space(n):
    dp = [0, 1]
    if n == 0:
        return dp[0]
    elif n == 1:
        return dp[1]
    else:
        counter = 2
        while counter <= n:
            dp.append(dp[-1] + dp[-2])
            counter += 1
        return dp[-1]


def fib_const_space(n):
    dp = {0: 0, 1: 1}
    if n == 0:
        return dp[0]
    elif n == 1:
        return dp[1]
    else:
        counter = 2
        while counter <= n:
            result = dp[counter - 1] + dp[counter - 2]
            dp[counter] = result
            del dp[counter - 2]
            counter += 1
        return dp[counter - 1]


start_time = time.time()
fib_n_space(200000)
print("O(n) space fib took %s seconds" % (time.time() - start_time))

start_time = time.time()
fib_const_space(200000)
print("O(1) space fib took %s seconds" % (time.time() - start_time))
