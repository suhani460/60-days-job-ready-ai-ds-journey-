Q1. Find the Largest of Three Numbers

Write a function find_largest(a, b, c) that returns the largest of three numbers.

Example:

Input:
10
25
15

Output:
Largest number is: 25

 SOLUTION:-
a = int(input("Enter your first no: "))
b = int(input("Enter your second no: "))
c = int (input("Enter your third no: "))

def find_largest(a,b,c):
    if(a>b and a>c):
        print("a is greater")
    elif(b>c and  b>a):
        print("b is greater")
    else:
        print("c is greater")
        
find_largest(a,b,c)
