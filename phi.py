import sys

DEFAULT_LIMIT = 100000


def compute_phi(LIMIT: int) -> list[int]:
    """Compute phi(n) for all n in the interval [0, LIMIT) as a list, with the convention phi(0) = 0.

    Args:
        limit (_type_): Exclusive upper limit of the range.
    """
    LIMIT = int(LIMIT)

    # As we will work with successive multiplication, we need to initialize everything at 1
    sieve = [n for n in range(LIMIT)]

    for n in range(2, LIMIT):
        # If the sieve is still at its initial value, n is prime
        if sieve[n] != n:
            continue

        # Propriety of phi : phi(p) = p - 1 for all primes p
        sieve[n] = n - 1

        for multiple in range(2 * n, LIMIT, n):
            sieve[multiple] = (sieve[multiple] // n) * (n - 1)


    return sieve



if __name__ == '__main__':
    try:
        limit = int(sys.argv[1])
    except Exception:
        limit = DEFAULT_LIMIT
