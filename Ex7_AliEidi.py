def fib(arg):
    if arg <= 1:
        return arg
    else:
        return (fib(arg-1)+fib(arg-2))
    
