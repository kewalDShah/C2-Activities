#Learn about Defining List
#Create a list of all your friends
friends=["Joy","Happy","Kelly"]

#print list of friends using variable
print(friends)

#Learn to print specific value from a list
#print specific value
print(friends[0])

#ask one more friend's name to add to the list
oneMoreFriend=input("Enter one friend name which you want to add to the list: ")

#Add the name of the newly asked friend to the list.
friends.append(oneMoreFriend)

#print list of friends using variable
print(friends)

#Learn about if-conditions
#Add a condition to check if the name of your best friend is in the list
if("Joy" in friends):
  
  #Print a message to inform the user that the best friend's name is in the list of friends
  print("Your name is there in the list")
  
#Else condtion if frined's name not in list
else:
  print("Your name not in list")



#Learn about operators
#______________What is Operators (==, <,>)
  
#Initialize a variable and assign a number of your choice from 1 to 10
number=6

#ask for an input from the user for a number
inpNumber=input("Enter a number to check you guess")

#convert the input of number to an integer
inpNumber=int(inpNumber)

#Add a condition to check if the guessed number is greater than the number in the game
if(inpNumber>number):

  #print the message that user guessed too high number
  print("You have guessed too high number")

#Add an elif condition to check if the guessed number is less than the number in the game.
elif(inpNumber<number):

  #print the message that user guessed too small number
  print("You have guessed too small number")

#Add an elif condition to check if the guessed number is equal to the number in the game
elif(inpNumber==number):
  #print the message that guessed numnber is correct
  print("You have done it. You got the exact number")
