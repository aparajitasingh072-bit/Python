#input a word
text = str(input("enter a string: "))

#reverse string
#using step value as -1 to iterate in reverse
revText = text[: : -1]

print("Reverse of given string is:")
print(revText)