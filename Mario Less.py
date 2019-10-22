'''
This program prints out a half-pyramid of a given height from the user
Miki Ando
'''

#get the height of the half-pyramid from the user
height = input("Height: ")

#If the values are not a digit or is not in the range between 0 and 23,
#the program asks the user to re-enter the height
while not(height.isdigit()) or int(height) < 0 or int(height) > 23:
        height = input("Retry: ")

#height is turned into an integer 
height = int(height)

#prints out the half-pyramid where 2 blocks are starting at the top 
for i in range(2, height + 2):
    block = "#" * i
    space = " " * (height - (i - 1))
    print(space + block)


    



        
    
    

