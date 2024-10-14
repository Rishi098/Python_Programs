# question=Write a program that takes an integer n as input and prints a butterfly pattern.
# Input=First line will contain an integer n.
# Output= Print the butterfly pattern with height and width 2n-1. (Print them without space in-between)

# code for this question

n=int(input())    # take n input value
for i in range(1,n+1):
    for j in range(1,2*n):
        if j==1 or j==2*n-i or j>=2*n-i or j<=i:
            print("*",end="")
        else:
            print(" ",end="")
    print()
for m in range(n+1,2*n):
    for k in range(1,2*n):
        if k>=m or k==1 or k<=2*n-m :
            print("*",end="")
        else:
            print(" ",end="")
    print()

