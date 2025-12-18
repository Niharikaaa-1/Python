'''
The Sorting Hat is a magical talking hat at Hogwarts School of Witchcraft and Wizardry. The hat decides which of the four "Houses" each first-year student goes to:

🦁 Gryffindor
🦅 Ravenclaw
🦡 Hufflepuff
🐍 Slytherin


Write a program that asks the user some questions with the int() and input() functions:

Q1) Do you like Dawn or Dusk?
    1) Dawn
    2) Dusk

If answer is equal to 1, Gryffindor and Ravenclaw both get a +1.
Else if answer is equal to 2, Hufflepuff and Slytherin both get a +1.
Else, output the message "Wrong input."
Q2) When I’m dead, I want people to remember me as:
    1) The Good
    2) The Great
    3) The Wise
    4) The Bold

If the answer is 1, Hufflepuff +2.
Else if answer is 2, Slytherin +2.
Else if answer is 3, Ravenclaw +2.
Else if answer is 4, Gryffindor +2.
Else, output the message "Wrong input."
Q3) Which kind of instrument most pleases your ear?
    1) The violin
    2) The trumpet
    3) The piano
    4) The drum

If the answer is 1, Slytherin +4.
Else if the answer is 2, Hufflepuff +4.
Else if the answer is 3, Ravenclaw +4.
Else if the answer is 4, Gryffindor +4.
Else, output "Wrong input."
Lastly, print out the score for each house.

Bonus: If you want to go further, see if you can figure out how to print out the house with the most points!
'''

gryffindor=0
ravenclaw=0
hufflepuff=0
slytherin=0

q1=int(input("Q1. Do you like Dawn or Dusk? \n1) Dawn\n2) Dusk\n"))
q2=int(input("Q2. When I'm dead, I want people to remember me as: \n1) The Good\n2) The Great\n3) The Wise\n4) The Bold\n"))
q3=int(input("Q3. Which kind of instrument most pleases your ear?\n1) The violin\n2) The trumpet\n3) The piano\n4) The drum\n"))

if q1==1:
  gryffindor+=1
  ravenclaw+=1
elif q1==2:
  hufflepuff+=1
  slytherin+=1
else:
  print("Wrong input.")

if q2==1:
  hufflepuff+=2
elif q2==2:
  slytherin+=2
elif q2==3:
  ravenclaw+2
elif q2==4:
  gryffindor+=2
else:
  print("Wrong input.")

if q3==1:
  slytherin+=4
elif q3==2:
  hufflepuff+=4
elif q3==3:
  ravenclaw+=4
elif q3==4:
  gryffindor+=4

print(f"Final Scores: \n🦁 Gryffindor = {gryffindor}\n🦅 Ravenclaw = {ravenclaw}\n🦡 Hufflepuff = {hufflepuff}\n🐍 Slytherin = {slytherin}\n")

scores = {
    "Gryffindor": gryffindor,
    "Ravenclaw": ravenclaw,
    "Hufflepuff": hufflepuff,
    "Slytherin": slytherin
}

winner=max(scores,key=scores.get)
print(f"You belong to : {winner}")
