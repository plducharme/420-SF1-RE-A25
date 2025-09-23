from pandas.core.dtypes.inference import is_number


def cube(nb):
    return nb**3


a = cube(3)
print(a)
b = cube(4)
print(b)
print(cube(9))


