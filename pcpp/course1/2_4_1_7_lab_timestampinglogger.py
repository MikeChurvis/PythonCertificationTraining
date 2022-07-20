from datetime import datetime


def with_timestamp(function):
    def func_wrapper(*args, **kwargs):
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return function(*args, **kwargs)

    return func_wrapper


if __name__ == '__main__':
    @with_timestamp
    def add(a, b):
        return a + b


    @with_timestamp
    def mul(a, b):
        return a * b


    def main():
        print(add(3, 3))
        print(mul(3, 3))


    main()
