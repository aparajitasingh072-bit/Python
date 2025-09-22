#Assigning different Variables
name="penguin"
age= 15
is_student = True
weight = 38.5

#printing differnet Variables and their data type
print("Name :", name)
print("Data type of name is", type(name))

print("Age :", age)
print("Data type of name is", type(age))

print("is_student :", is_student)
print("Data type of name is", type(is_student))

print("Weight :", weight)
print("Data type of name is", type(weight))

#Type casting to convert into another data type of variables
print("\nAfter type casting...")
age=str(age)
print("data type of age is", type(age))
weight=int(weight)
print("Weight :", weight)
print("Data type of weight is", type(weight))