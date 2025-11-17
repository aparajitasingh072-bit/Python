valid = False
while not valid: #using nested while loop 
    try:
       n = int(input("enter a number: "))
       while n%2==0:
        print("bye bye")
        valid = True
    except ValueError:
       print("Invalid")
