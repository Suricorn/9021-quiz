# Written by *** for COMP9021
#
# Generates a random integer dim strictly greater than 2
# and a list of random digits of length dim.
#
# Outputs some text and two "pictures".
# The text clarifies what "pictures" are expected.
#
# There are a few blank lines in the output,
# including one at the very end.


from random import seed, randrange
import sys

try: 
    for_seed, dim = (int(x) for x in input('Enter two integers, the second '
                                           'one being 3 or more: '
                                          ).split()
                    )
    if dim <= 2:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(for_seed)
digits = [randrange(10) for _ in range(dim)]
print()
print(f'The chosen dimension is {dim}.')
print(f'Also, I have this sequence of {dim} digits for you:')
print(' ', digits)
print()

# INSERT YOUR CODE HERE
print("Here is a first picture.")
print(f"There are {dim-1} spaces on each side of the star.")
print()
width = 2*dim-1
print("  |" + "-" * width + "|")
print("  |" + " " * width + "|")
print("  |" + " " * (dim-1) + "*" + " " * (dim-1) + "|")
print("  |" + " " * width + "|")
print("  |" + "-" * width + "|")
print()

print("Here is a second picture.")
print("Top and bottom borders are complementary, because:")
print("  0 is 9\'s \"complement\".")
print("  1 is 8\'s \"complement\".")
print("  2 is 7\'s \"complement\".")
print("  ...")
print( )

print("  |", end = "")
for number in digits[:dim-1]:
    print(number, end = "-")

print(digits[dim-1], end = "|\n" )

print("  |" + " " * width + "|")
print("  |" + " " * (dim-2) + "---" + " " * (dim-2) + "|")
print("  |" + " " * (dim-2) + "|*|" + " " * (dim-2) + "|")
print("  |" + " " * (dim-2) + "---" + " " * (dim-2) + "|")
print("  |" + " " * width + "|")

print("  |", end = "")
for number in digits[:dim-1]:
    print(9-number, end = "-")

print(9-digits[dim-1], end = "|\n" )
print()    
