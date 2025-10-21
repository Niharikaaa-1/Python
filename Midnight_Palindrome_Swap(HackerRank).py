'''
Two spies exchange messages. If entire string is a palindrome (ignoring spaces/case), print PAL, else print the string with first and last characters swapped.

Input Format

single line S.

Constraints

1 ≤ len ≤ 200.

Output Format

either PAL or transformed string.
'''

n=(input())
s=[]
a=n.replace(" ","").lower()
if a==a[::-1]:
    print("PAL")
else: 
    swap=a[-1]+a[1:-1]+a[0]
    print(swap)
