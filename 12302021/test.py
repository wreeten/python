# IMPORTANT
# [expression FOR item IN iterable]



# iterable: range, list, tuple, or Sequence
# item: variable name whjich takes value in iterable
# expression: python expression which is calculated for each value in "item"


numbers =[ n for n in range(1,21)]
print(numbers)

squares = [n**2 for n in range(1,11)]
print(squares)

#periodic 0 1 2
zeroOneTwo = [n%3 for n in range(0,21)]
print(zeroOneTwo)

print(sum(zeroOneTwo))
print(max(zeroOneTwo))
print(min(zeroOneTwo))

print(sorted(zeroOneTwo))


def avg(x):

    sumX = sum(x)
    lenX = len(x)
    return sumX / lenX

print(avg([1,2,3,4]))
