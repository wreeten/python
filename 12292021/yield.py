# # # def generatorY():
# # #     yield john 
# # #     yield 2
# # #     yield four

# # # for value in generatorY():
# # #     print(value)

# # from typing import Generator, overload


# # def simpGen():
# #     x = 1
# #     yield x
# #     yield 1
# #     yield x + 1
# #     yield x + 2
# # genObj = simpGen()
# # genObj

# # for i in genObj:
# #     print(i)
# # # next(genObj)
# # # what happens here is "stop iteration" error if you don't uncomment line 23


# # # we can only iterate through the generator object ONCE!!!!!!!!!!!!!!!
# # # the second time won't give anything because object is exhausted and needs to be reinitialized

# # # there are mutliple approaches:

# # # first: replenish the gen by recreating again and iterate it overload

# # # second: iterate it by calling the function that create the Generator

# # # third is to convert it to a class then an iterator is created every time so generator exhausted won't happy


# # #approach two!!

# # # you can iterate again by calling function that returned the generator:
# # for i in simpGen():
# #     print(i)


# # # third option is:

# # class Iterable(object):
# #     def __iter__(self):
# #         x = 1
# #         yield x
# #         yield x + 1
# #         yield x + 2
# # iterable = Iterable()

# # for i in iterable: # iterator is created here
# #     print(i)
# # for i in iterable: #iterator created again
# #     print(i)

# for n in [1, 2, 3, 4, 5, 6]:
#     square = n**2
#     print(n, 'squared' , square)
# print('loop completed')

# while n > 0:
#     print(n)
#     n = n-1


# this is for an example of the square of a given object


if __name__ == '__main__':
    n = int(input())

for i in range(n):
    print(i*i)