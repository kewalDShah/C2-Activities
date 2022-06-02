#LEARN ABOUT LIST
#Create a list of all your friends
friends=["Joy","Happy","Kelly"]

#print the list of your friends 
print(friends)

#print specific value
print(friends[0])
print(friends[2])

#Take the input of one more friend's name and add it to the list.
oneMoreFriend=input("Enter one friend name which you want to add to the list: ")

friends.append(oneMoreFriend)


#print list of your friends
print(friends)

#LEARN ABOUT CONDITIONS
#Add a condition to check if your best friend's name is present in the list or not and print a message accordingly

if("Joy" in friends):
  print("Your name is there in the list")
else:
  print("Your name not in list")



#LEARN ABOUT OPERATORS(==, <,>) 
  
#Initialize a variable and assign a jackpot number of your choice 
JackpotNumber=6

#Ask the user to guess the jackpot number and store it in a variable
guessedJackpotNumber=input("Enter a number to check you guess")

#convert the guessed jackpot number to an integer
guessedJackpotNumber=int(guessedJackpotNumber)

#Add an if condition to check if the guessed jackpot number is equal to the jackpot number and print a message accordingly
if(guessedJackpotNumber==JackpotNumber):
  print("You won the Jackpot!")

#Add a elif condition to check if the guessed jackpot number is greater than the jackpot number and print a message accordingly
elif(guessedJackpotNumber>JackpotNumber):
  print("The guessed number is greater then the Jackpot number")

#Add an elif condition to check if the guessed number is lesser than the jackpot number and print a message accordingly
elif(guessedJackpotNumber<JackpotNumber):
  print("The guessed number is lesser then the Jackpot number")
