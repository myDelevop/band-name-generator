# Unlimited POSITIONAL arguments (args[0) = 3, first argument)

def add(*args):
    # type iterable tuple
    res = 0
    for n in args:
        res += n
    return res


print(add(3, 4, 5, 2, 1, 7, 4, 3))
