# Problem 48:
#     Self Powers
#
# Description:
#     The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
#
#     Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

def ten_digits(x: int) -> int:
    """
    Returns the last 10 digits of x^x as an int.

    Args:
        x (int): Natural number

    Returns:
        (int): x^x mod 10^10
    """
    # Binary exponentiation in mod 10^10
    digits = 1
    x_pow = x % (10 ** 10)  # x^1
    while x > 0:
        if x % 2 == 1:
            digits = (digits * x_pow) % (10 ** 10)
        x //= 2
        x_pow = (x_pow ** 2) % (10 ** 10)
    return digits


def main(n: int) -> int:
    """
    Returns the last 10 digits of the series 1^1 + 2^2 + ... + `n`^`n`

    Args:
        n (int): Natural number

    Returns:
        (int): Last ten digits of 1^1 + 2^2 + ... + `n`^`n`

    Raises:
        AssertError: if incorrect args are given
    """
    assert type(n) == int and n > 0

    # Store last ten digits as an int, since it's not huge
    digits = 0
    for i in range(1, n+1):
        digits_i = ten_digits(i)
        digits = (digits + digits_i) % (10 ** 10)
    return digits


if __name__ == '__main__':
    num = int(input('Enter a natural number: '))
    self_powers_digits = main(num)
    print('Last ten digits of sum of i^i for 1 through {}:'.format(num))
    print('  {:010d}'.format(self_powers_digits))
