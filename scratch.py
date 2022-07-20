class Foo:
    @property
    def setter_func(self):
        return 0


foo = Foo()

print(help(foo))