# Count number of bits to be flipped
# to convert A into B

# Function that count set bits
def countSetBits(n):
    count = 0
    while n:
        count += 1
        n &= (n-1)
    return count

# Function that return count of
# flipped number


def FlippedCount(a, b):

    # Return count of set bits in
    # a XOR b
    return countSetBits(a ^ b)


# Driver code
a = int(input('a='))
b = int(input('b='))
print(FlippedCount(a, b))
