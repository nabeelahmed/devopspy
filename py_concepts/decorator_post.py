
# # -------------- 1. simple decorator ---------------
# def hello_decorator(original_fn):
#     def decorator_fn():
#         print("Hello from new")
#         original_fn()
#     return decorator_fn
#
# @hello_decorator
# def hello():
#    print("Hello from original")


# # -------------- 2. Function with arguments ---------------
# def add_decorator(original_fn):
#     def decorator_fn(*args, **kwargs):
#         print("Hello from new")
#         original_fn(*args, **kwargs)
#     return decorator_fn
#
# @add_decorator
# def add(x, y):
#     print(x + y)


# # -------------- 3. Decorator with arguments ---------------
# def add_decorator(n):
#     def decorator_fn(original_fn):
#         def wrapper_fn(*args, **kwargs):
#             result = original_fn(*args, **kwargs)
#             print(result+n)
#             return result + n
#         return wrapper_fn
#     return decorator_fn
#
# @add_decorator(2)
# def add(x, y):
#     return x + y

# --------------- 4. Exception Handler --------
# def exception_handler(dafualt_message=None):
#     def decorator_fn(original_fn):
#         def applicator(*args, **kwargs):
#             try:
#                 return original_fn(*args, **kwargs)
#             except Exception as err:
#                 print(err)
#                 return dafualt_message
#         return applicator
#     return decorator_fn
#
# @exception_handler("Exception happened")
# def add(x, y):
#     sum = x + y
#     print(sum)
#     return sum

# # --------------- 4. Exception Handler --------
# def exception_handler(original_fn):
#     def decorator_fn(*args, **kwargs):
#         try:
#             return original_fn(*args, **kwargs)
#         except Exception as err:
#             print(err)
#     return decorator_fn
#
# @exception_handler
# def add(x, y):
#     sum = x + y
#     print(sum)
#     return sum


# # --------------- 5. Execution time --------
# import time
#
# def timeit(original_fn):
#     def decorator_fn(*args, **kwargs):
#         start = time.time()
#         original_fn(*args, **kwargs)
#         end = time.time()
#         print('func:%r args:[%r, %r] took: %2.6f sec' % (original_fn.__name__,
#                                                          args, kwargs, end - start))
#
#     return decorator_fn
#
# @timeit
# def add(x, y):
#     return x + y
#
# @timeit
# def multiply(x, y):
#     return x * y


# # --------------------- Multiple decorators ---------------
def add_decorator_one(original_fn):
    def decorator_fn(*args, **kwargs):
        original_fn(*args, **kwargs)
        print("Hello from one")
    return decorator_fn

def add_decorator_two(original_fn):
    def decorator_fn(*args, **kwargs):
        original_fn(*args, **kwargs)
        print("Hello from two")
    return decorator_fn


@add_decorator_one
@add_decorator_two
def add(x, y):
    print(x + y)


class A(object):
    def foo(self, x):
        print("foo - %s" % x)

    @staticmethod
    def static_foo(x):
        print("static foo - %s" % x)


# if __name__ == "__main__":
#     add(2, 2)
    # multiply(2, 2)
    # add(2, "i")



