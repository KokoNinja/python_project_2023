#PRINT 1 TO 10

for a in range(0,5):
    print(a)

########################
for a in range(1,11,2):
    print(a)

########################
colors = ["red", "green", "yellow", "blue", "white"]

for i in range(0,5):
    print(colors[i])

for i in range(0,5):
    print(colors)

for i in range(0,len(colors)):
    print(colors[i])

################################################
numbers=[45,98,75,65,24,88,74,56,75]

for t in range(0,9):
    print(numbers[t])

#print all item that are less than or equal to 50

for t in range(0,9):
    if numbers[t]<=50:
        print(numbers[t])
