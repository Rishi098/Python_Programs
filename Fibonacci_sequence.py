n = int(input("Enter the number of Fibonacci numbers to print: "))
a, b = 0, 1
count = 0
while count < n:
    print(a)
    a, b = b, a + b
    count += 1  
       
# Output:

# Enter the number of Fibonacci numbers to print: 7
# 0
# 1
# 1
# 2
# 3
# 5
# 8
