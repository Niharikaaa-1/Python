'''
In a high-tech fortress, the chief guard was responsible for ensuring that all passwords were extra secure. He discovered a magical way to strengthen any password: by replacing each vowel with the next vowel in a special sequence.

The rule was simple but clever:

The vowels follow a cycle: a → e → i → o → u → a.
Uppercase vowels follow the same cycle but preserve their case: A → E → I → O → U → A.
Consonants remain unchanged.
Whenever someone tried to set a password, the guard would automatically transform it according to this rule, making it harder for intruders to guess while keeping it memorable for the rightful owner.

Input Format

single string S (password).

Constraints

1 ≤ len ≤ 200.

Output Format

resulting string.
'''

s=input()
map={'a':'e','e':'i','i':'o','o':'u','u':'a','A':'E','E':'I','I':'O','O':'U','U':'A'}
result=""
for i in s:
    if i in map:
        result+=map[i]
    else:
        result+=i
print(result)
