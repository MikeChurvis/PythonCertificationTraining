import time
from datetime import datetime


class InstantiationTimeMeta(type):
    classes_instantiated = []

    def __new__(mcs, name, bases, dictionary):
        dictionary['instantiation_time'] = datetime.utcnow().isoformat()
        dictionary['get_instantiation_time'] = lambda self: self.instantiation_time

        cls = super().__new__(mcs, name, bases, dictionary)
        InstantiationTimeMeta.classes_instantiated.append(name)
        return cls


class Foo(metaclass=InstantiationTimeMeta):
    pass


time.sleep(0.5)


class Bar(metaclass=InstantiationTimeMeta):
    pass


foo = Foo()
bar = Bar()

print(InstantiationTimeMeta.classes_instantiated)