# Question find the positive integer with the longest sequence
import time
saved_map = {1: 1}


def get_collatz_len(n):
    _n = n
    counter = 1
    while n != 1:
        if n % 2 == 0:
            n = n // 2
            if saved_map.get(n) is not None:
                counter += saved_map[n]
                # record coutner to map
                saved_map[_n] = counter
                return counter
            counter += 1
        else:
            n = 3 * n + 1
            if saved_map.get(n) is not None:
                counter += saved_map[n]
                # record coutner to map
                saved_map[_n] = counter
                return counter
            counter += 1
    saved_map[_n] = counter
    return counter


start = time.time()
q = 0
