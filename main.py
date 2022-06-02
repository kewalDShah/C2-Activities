#Learn about Defining List
#Create a list of all your friends
friends=["Joy","Happy","Kelly"]

#print list of friends using variable
print(friends)

#Learn to print specific value from a list
#print specific value
print(friends[0])

#ask one more friend to add in the list
oneMoreFriend=input("Enter one friend name which you want to add to the list: ")

#add the newly asked friend name to the list
friends.append(oneMoreFriend)

#print list of subject using variable
print(friends)

#Learn about if-conditions
#Condition to check if your name in list
if("Joy" in friends):
  
  #print a string to inform about friend's name is there in list
  print("Your name is there in the list")
  
#Else condtion if frined's name not in list
else:
  print("Your name not in list")



#Learn about operators
#______________What is Operators (==, <,>)
#Initialize a variable and assign a number of your choice from 1-10
number=6
#Condition




if (password=="letsCode"):
  #print the string to authenticate the access
  print("You have been granted access")
#add a else condition for password not matching
else:
  #Print a string to mention password incorrect
  print("Password incorrect")


#Activity 2:
#__________What are comparision operators (<,>)
# ask the user age
age = int(input("Enter your age to check eligiblity for U16 football ?"))
#check if the age is greater than 16
if(age>16):
  #print a message to say user cannot is not eligible
  print("You cant be selected as you are age don't match the criteria")
#add a elif condition to check age less than 14
elif(age<14):
  #print message to inform the user is very young for eligiblity
  print("You are too young try next year")
#add a else condition to inform for selection round
else:
  #print the message that the user is eligible for selection
  print("You are eligble for selection round")
