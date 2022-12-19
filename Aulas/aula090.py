# Generator expression, Iterables e iterators em Python

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable) # tem __iter__ e __next__

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

generator = [n for n in range(10)]
print(generator)
