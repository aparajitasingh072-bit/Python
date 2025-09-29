#Take marks input from user
print("enter marks obtained in 6 subjects:")
Maths = int(input("maths:"))
English = int(input("English:"))
Science = int(input("Science:"))
Hindi = int(input("Hindi:"))
Socialsci = int(input("Socialsci:"))
ger = int(input("ger:"))

#Lets calculate the percentage of marks
sum=Maths+English+Science+Hindi
print('sum of math, english, science, hindi, Socialsci and ger:')

perc = (sum/480)*100

print(end="Percentage Mark=")
print(perc)
