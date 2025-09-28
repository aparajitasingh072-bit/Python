#Take marks input from user
print("enter marks obtained in 4 subjects:")
Maths = int(input("maths:"))
English = int(input("English:"))
Science = int(input("Science:"))
Hindi = int(input("Hindi:"))

#Lets calculate the percentage of marks
sum=Maths+English+Science+Hindi
print('sum of math, english, science and hindi:')

perc = (sum/400)*100

print(end="Percentage Mark=")
print(perc)
