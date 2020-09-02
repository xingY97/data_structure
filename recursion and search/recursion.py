#!python

def factorial(n):
    """factorial(n) returns the product of the integers 1 through n for n >= 0,
    otherwise raises ValueError for n < 0 or non-integer n"""
    # check if n is negative or not an integer (invalid input)
    if not isinstance(n, int) or n < 0:
        raise ValueError('factorial is undefined for n = {}'.format(n))
    # implement factorial_iterative and factorial_recursive below, then
    # change this to call your implementation to verify it passes all tests
    #return factorial_iterative(n)
    return factorial_recursive(n)


def factorial_iterative(n):
    # TODO: implement the factorial function iteratively here
    # once implemented, change factorial (above) to call factorial_iterative
    # to verify that your iterative implementation passes all tests

    #initialize factorial to value 1
    factorial = 1
    #use for loop and range to iterate from initial value to target value
    # in orde to do that ,add 1 to every previous iteration until target value.
    for i in range(1,n + 1):
        #every iteration the variable factorial holds the product of initial value and all numbers after it
        # at the end of the loop, after target value meet, the variable factorial will have 
        #the product of all numbers.
        factorial = factorial * i
    return factorial


def factorial_recursive(n):
    # check if n is one of the base cases
    if n == 0 or n == 1:
        return 1
    # check if n is an integer larger than the base cases
    elif n > 1:
        # call function recursively
        return n * factorial_recursive(n - 1)


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 1:
        num = int(args[0])
        result = factorial(num)
        print('factorial({}) => {}'.format(num, result))
    else:
        print('Usage: {} number'.format(sys.argv[0]))


if __name__ == '__main__':
    main()
    #print(factorial_iterative(15))
