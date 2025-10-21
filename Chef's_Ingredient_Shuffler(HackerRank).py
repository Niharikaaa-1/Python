'''
Chef sorts characters of each ingredient name alphabetically, but keeps ingredient order.

Input Format

single line with ingredients separated by commas (,). Trim spaces.

Constraints

each ingredient length ≤ 50, n ≤ 20.

Output Format

comma-separated transformed ingredients.
'''

s=input()
a=s.split(',')
b=[]
for i in a:
    b.append(sorted(i))
print(','.join([''.join(i) for i in b]))
