# Even numbers generator using yield
# def even_numbers(max_num):
#     num = 0
#     while num < max_num:
#         yield num
#         num += 2
        
# for i in even_numbers(10):
#     print(i)
# Fibonacci generator using yield and next
def fibonacci(limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b

fib_gen = fibonacci(10)
print(next(fib_gen))
