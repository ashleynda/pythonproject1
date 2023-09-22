def big_list(num: int):
    double = []
    for i in range(num):
        double.append(1 * 2)
    return double


def generator_func(n):
    for x in range(n):
        yield x


g = generator_func(100)
for c in g:
    pass

# print((big_list(1000000)))

a = generator_func(1000)
# sa
print(next(a))
# print(generator_func(10000))

def design(fn):
    print("*************************")
    fn()
    print("*************************")
    return fn


@design
def show():
    print("Welcome to ace clowns")


def performance_check(fn):
    def wrap(*args, **kwargs):
        time1 = time()
        result = 
        time2 = time()
        print(f"It took {time2 - time1} to execute")
        return result
    return wrap


@performance_check
def big_list(num: int):
    double = []
    for i in range(num):
        double.append(1 * 2)
    return double





