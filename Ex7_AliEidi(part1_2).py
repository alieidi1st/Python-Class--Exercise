#Ex7-1st part
def fib1(n):
    if n <= 1:
        return n
    else:
        return (fib1(n-1)+fib1(n-2))
#Ex7-2nd part
def gen_seq(length):
    if(length <= 1):
        return length
    else:
        return (gen_seq(length-1) + gen_seq(length-2))

length = int(input("Enter number of terms:"))
l1= []
print("Fibonacci sequence using Recursion :")
for iter in range(length):
    l1 += [gen_seq(iter)]  
print(l1)

