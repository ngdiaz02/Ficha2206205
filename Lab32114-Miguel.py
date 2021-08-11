blocks = int(input("Enter the number of blocks: "))
height = 0
j = 1                   # índice 1, 2, 3, 4....
while j <= blocks:
    height += 1
    blocks -= j
    j += 1

print("The height of the pyramid:", height)
#height     j
#1          1 
#2          3   (3-1=2)
#3          6   (6-3=3)
#4          10  (10-6=4)
#5          15  (15-10=5)
#6          21  (21-15=6)
