print('select your ride')
print("1. Bike")
print('2. Car')

#take input of 1 and 2
#select your ride
choice= int(input("Enter your choice: "))

#user enters 1
if (choice==1 ): #condition 1 outer if statement
    print('what type of bike?')
    print('1. scooty\n')
    print('2. scooter\n')

#condition for selecting the type of bike 
    choice2=int(input('enter your choice2: '))
    if choice2==1: #inner if statement
     print("you have selected scooty")
    else:
     print("you have selected scooter")

#user entering option 2
elif (choice==2): #outer elif
  print('what type of car?')
  print('1. Sedan\n')
  print('2. XUV\n')
  choice3= int(input("Enter your choice3: "))

  if choice3==1: #inner if statement
     print("you have selected Sedan")
  else:
     print("you have selected XUV ")
    




 
