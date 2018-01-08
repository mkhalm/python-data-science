#Python Review
print("Hello World")

def add(num1, num2):
    return num1+num2

print(add(2,3))


def volrect(length, width, height):
    return length*width*height

print(volrect(1,2,3))

def mean(numbers):
    return sum(numbers)/len(numbers)

print(mean([1,3,5,7,9]))

#Find median of 3,9,1,2,7
    # sort --> 1,2,3,7,9
    # find middle --> 3

# Find median of 3,9,1,2,7,4
        #sort --> 1,2,3,4,7,9
        #avg of middle --> (3+4)/2 --> 3.5
def median_mh(numbers):
    x=sorted(numbers)
    n=len(numbers)
    if n == 0:
        return None
    if n%2 == 1:
        return x[n//2]
    else:
        y=n//2 #double /  - makes python do whole number division
        return(x[y-1]+x[y])/2

def median(numbers):
    """
    Computes the median of a list of numbers
    argument: numbers=list of numbers
    return median

    Below is a the doc test to show how to call the code and what the answer would be
    >>> median([2,1,6])
    2
    >>> median([3,5,4,9])
    4.5

    """
    numbers=sorted(numbers)
    middle=len(numbers)//2
    if len(numbers) % 2 == 0:
        #even list
        return sum(numbers[middle-1:middle+1])/2
    else:
        #odd list
        return numbers[middle]

def mode(numbers):
    """
    Find the most common value in the list

    argument: list of numbers
    return: the mode

    >>> mode([1,2,2,2,3,3,4])
    2
    """
    from collections import defaultdict
    d=defaultdict(int)
    for n in numbers:
        d[n] += 1
    return sorted(d,key=lambda key: d[key])[-1]
