a = 10
b = 20


def fonction():
    x = 30
    y = 40
    print("locals() = {0}".format(locals()))
    print("*" * 80)


print("locals() = {0}".format(locals()))
print("*" * 80)
print("globals() = {0}".format(globals()))
print("*" * 80)

print("locals() == globals()?", locals() == globals())
print("*" * 80)

fonction()
