'''
Create an abbreviation: take first letters of each word, uppercase them.
'''
n=input()
t=n.title()
a=t.split()
s=[]
for i in t:
    if (i.isupper()):
        s.append(i)
print(''.join(s))
