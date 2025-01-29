# number argument n the number of fibonacci sequence

# 0 
# if number =0 0 
    # return 0
# if number == 1 
# return 1 
# 1
def fibonacci(n):
    if n == 0 or n == 1: 
        return n
    return fibonacci(n-1) + fibonacci(n - 2)


print(fibonacci(3))
# print(fibonacci(55))
# print(fibonacci(89))