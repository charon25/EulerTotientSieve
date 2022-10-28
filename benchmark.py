import json
import sys
import time
from typing import Callable
from tqdm import trange

from phi import compute_phi

DEFAULT_LIMIT = 1000000
MAX_TEN_POWER = 8

def naive_method(LIMIT):
    from math import gcd

    # For every number n, count how many k (2 <= k < n) are prime with n
    # We can exclude n as it is never prime with itself if > 1
    # We also exclude 1 by always adding 1 to the count (as 1 is prime with every number)
    return [1 + len([1 for k in range(2, n) if gcd(k, n) == 1]) for n in range(1, LIMIT)]

def prime_factors_method(LIMIT):
    phi = []

    # Same principle as the sieve, but for only one number n
    # Go through all its prime factors p, and successively multiply n by (p - 1) / p
    for n in range(1, LIMIT):
        phi_n = n
        divisor = 2
        while n > 1:
            if n % divisor == 0:
                phi_n = (phi_n // divisor) * (divisor - 1)
                while n % divisor == 0:
                    n //= divisor
            divisor += 1
        phi.append(phi_n)
    
    return phi


def benchmark_one(LIMIT):
    times = []

    for _ in range(10):
        start_time = time.perf_counter()
        compute_phi(LIMIT)
        stop_time = time.perf_counter()
        times.append(stop_time - start_time)
    
    print(f"=== Solo benchmark result (LIMIT = {LIMIT})")
    print(f'- Minimum time : {1e3 * min(times):.1f} ms')
    print(f'- Average time : {1e3 * sum(times) / len(times):.1f} ms')


def benchmark_method(method: Callable):
    results = {}

    try:
        for ten_power in trange(MAX_TEN_POWER + 1):
            for multiplier in (1, 2, 5):
                LIMIT = multiplier * (10 ** ten_power)
                times = []
                for _ in trange(10, leave=False, desc=f"M,E=({multiplier},{ten_power})"):
                    start_time = time.perf_counter()
                    method(LIMIT)
                    stop_time = time.perf_counter()
                    times.append(stop_time - start_time)

                results[LIMIT] = times
    except KeyboardInterrupt:
        pass
    
    with open(f'not_git\\benchmark_{method.__name__}.json', 'w') as fo:
        json.dump(results, fo)



if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.argv.append('-s')
    
    if sys.argv[1] == '-o':
        benchmark_one(DEFAULT_LIMIT)
    elif sys.argv[1] == '-s':
        benchmark_method(compute_phi)
    elif sys.argv[1] == '-n':
        benchmark_method(naive_method)
    elif sys.argv[1] == '-p':
        benchmark_method(prime_factors_method)
