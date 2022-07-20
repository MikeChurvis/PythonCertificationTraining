class Foo:
    var = 0


foo = Foo()
print(f"{foo.var == Foo.var = }")

Foo.var += 1
print(f"{foo.var == Foo.var = }")

foo.var += 1
print(f"{foo.var == Foo.var = }")
