#for i in range(0,5):
#    for j in range(0, i+1):
#        print('*', end = '')
#    print()

#i = 1
#while i < 6:
#    print(i*'*', end = '')
#    print()
#    i += 1

#CHALLENGE 1 ----------------------------------------------
#import random

#L = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
#items = {}
#for i in range(1,6):
#    j = random.randint(0,10)
#    for k in range(0,j):
#        if i not in items:
#            items[i] = L[k]
#        else:
#            items[i] += L[k]
#print(items)
#calories = list(items.values())
#maximum = max(calories)
#elf = 0
#for i in items:
#    if maximum == items[i]:
#        elf = i
#print("Elf carrying most calories:", elf, ", Calories:", maximum)
#---------------------------------------------
#import random
#score = 0
#friend = ['A','B','C']
#me = ['X','Y','Z']

#strat = []
#for i in range(0,3):
#    j = random.randint(0, 2)
#    strat = strat + [friend[j]]

#print('To win, use this: ', strat)

#game = []
#--------------------------------
#def check(i):
#    factors = 0
#   for j in range(1, i+1):
#        if i%j == 0:
#            factors += 1
#        if factors >2:
#            break
#    if factors == 2:
#        print(i)

#def generate():
#    for i in range(2,1000):
#        check(i)
#generate()
#---------------------

factors = 0
a = int(input("Enter a number: "))

for i in range(1, a + 1):
    if a%i == 0:
        factors = factors + 1
    if factors > 2:
        print("Not prime")
        break
if factors == 2:
    print("prime")
