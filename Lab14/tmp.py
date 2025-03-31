import inspect


def foo():
    func_name = inspect.stack()[0][3]
    caller_name = inspect.stack()[1][3]
    print(f"I'm {func_name}.\n{caller_name} called me!")


def bar(f):
    f()


bar(foo)

# I'm foo.
# bar called me!
