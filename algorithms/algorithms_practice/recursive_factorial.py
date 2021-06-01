"""The module implements a recursive method
for calculating the factorial
Factorial of a number specifies a product of all integers from 1 to that number.
It is defined by the symbol explanation mark (!)
"""


class RecFac:
    """Releases the computation of the factorial of a number"""
    def factor(self, n: int) -> int:
        """
        Main function in class.
        Releases the computation of the factorial of a number.
        Parameters
        ----------
        n : int, optional
            Entered number

        Raises
        ------
        ValueError
            If number is not positive.

        TypeError
            If number is not int.
        """
        if isinstance(n, int):
            if n < 0:
                raise ValueError('Value must be positive')
            elif n == 1:
                return 1
            else:
                return n * self.factor(n-1)
        else:
            raise TypeError('Value must be type int')


def main():
    fac = RecFac()
    print(fac.factor(5))


if __name__ == '__main__':
    main()
