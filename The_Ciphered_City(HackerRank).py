'''
For each city name, move every uppercase letter to the front preserving relative order, then append lowercase letters preserving order.

Input Format

single string (one word; no spaces).

Constraints

letters only, length ≤ 100.

Output Format

transformed string.
'''

n=input()
upp=""
lo=""
for i in range(len(n)):
    if(n[i].isupper()):
      upp+=n[i]
    else:
        lo+=n[i]
print(upp+lo)
