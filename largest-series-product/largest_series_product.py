#!/usr/bin/env python

def slices(digits, n):
    if n > len(digits) or n == 0:
        raise ValueError("Slice value larger than digit string")
    return [map(int, list(digits[i:i+n])) for i in range(len(digits)-(n-1))]
    
def largest_product(digits, n):
    digits = map(int, sorted(digits))
    return reduce(lambda x, y: x * y, digits[-n:]) 
    
if __name__ == "__main__":
    print largest_product("0123456789", 2)

