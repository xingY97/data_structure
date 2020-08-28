import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace

#Binary to decimal
def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)

    sum = 0
    #loop through the digits to find the match indx of input value
    for i in range(len(digits)):
        #check if digits contain letters
        if digits[i].isalpha():
            #if yes, use .index to find the position index of the match letter
            match_value = string.ascii_lowercase.index(digits[i].lower()) + 10  #added 10 because 0-9 before Hex string
        else:
            #if not, use int to convert number into decimal string.
            match_value = int(digits[i])
            #get sum by adding value * base to whatever power it is base on the length of the digits.
        sum += match_value * (base ** (len(digits) -i - 1)) #-1 to reverse the digits since read from righ to left.
        
    return sum

#decimal to binary or anyother bases
def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)

    #loop to do the repeated divison, where to stop?
    #get the remainders and divisors
    #save theremainders
    #return the final numbe result as a string
    #somehow deal with hex digits

    #all digits and letters 0-9 a-z 
    digits_and_letters = string.digits + string.ascii_letters
    
    final_digits = "" #empty string to fill final vaule

    #loop will stop to a point where it cant not be divided by base anymore
    while number > 0: 
        # use remainder method 
        remainder = number % base
        number = number - remainder
        number = number // base

        if remainder > 9:
            remainder = string.ascii_lowercase[remainder-10] # -10 get rid off 10 integer numbers
        final_digits += str(remainder)
    
    return final_digits[::-1]
    
        


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    # TODO: Convert digits from base 2 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from base 2 to base 10 (and vice versa)
    # ...
    # TODO: Convert digits from base 10 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from any base to any base (2 up to 36)
    string = decode(digits, base1)
    return encode(string, base2)


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    #main()
   
    print(encode(5,10)) #5
    #print(encode(10,16)) #a
    #print(encode(9781876,25)) #101101
    print (encode(1234, 32))#16i

