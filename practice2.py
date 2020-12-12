import random 
print("RANDOM SELECTION\n\n")

list =[]
num =int(input("Enter the number of players: "))
for i in range(num):
     player = input("{}. ".format(i+1)).strip().lower()
     list.append(player)

selected = random.choice(list).title()
print("\n{} is selected!".format(selected))
     

