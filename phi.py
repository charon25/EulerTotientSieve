import sys

DEFAULT_LIMIT = 100000


def compute_phi(LIMIT: int):# -> list[int]:
    """Compute phi(n) for all n in the interval [0, LIMIT) as a list, with the convention phi(0) = 0.

    This works using the expression : phi(n) = n * Σ (1 - 1 / p) for every prime p dividing n
    This can be rewritten as phi(n) = n * Σ (p - 1) / p

    Then, instead of computing "n by n", we compute "p by p" : loop through every number n and if it is prime, loop through every multiple k*n (k > 1 and k*n < LIMIT) and multiply the sieve value by (n - 1) / n.
    To avoid dealing with float numbers, we int divide sieve[k*n] by n (as it is a multiple), and then multiply by (n - 1).

    Args:
        limit (_type_): Exclusive upper limit of the range.
    """
    LIMIT = int(LIMIT)

    # As we will work with successive "divisions", we need to initialize everything at n
    sieve = [n for n in range(LIMIT)]

    for n in range(2, LIMIT):
        # If the sieve is not at its initial value, n is not a prime
        if sieve[n] != n:
            continue

        # Property of phi : phi(p) = p - 1 for all primes p
        sieve[n] = n - 1

        for multiple in range(2 * n, LIMIT, n):
            sieve[multiple] = (sieve[multiple] // n) * (n - 1)

    return sieve


if __name__ == '__main__':
    try:
        limit = int(sys.argv[1])
    except Exception:
        limit = DEFAULT_LIMIT

    phi_values = compute_phi(limit)

    with open(f'phi_values_{limit}.txt', 'w') as fo:
        fo.write("\n".join(map(str, phi_values)))
