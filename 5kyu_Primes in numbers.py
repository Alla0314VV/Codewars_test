def prime_factors(n):
    """
    Decomposes a number into its prime factors and returns a string representation.

    Args:
        n: An integer greater than 1.

    Returns:
        A string representing the prime factorization in the format (p1)(p2**k)...,
        where p1, p2 are prime factors and k is their exponent if greater than 1.
    """
    i = 2
    res = {}
    while n > 1:  # Corrected loop condition
        if n % i == 0:
            if i in res:
                res[i] += 1
            else:
                res[i] = 1
            n //= i  # Use integer division
        else:
            i += 1

    t = ''
    res_sorted = sorted(res.items())  # Sort the dictionary items by key

    for factor, exponent in res_sorted:
        if exponent == 1:
            t += f'({factor})'
        else:
            t += f'({factor}**{exponent})'
    return t