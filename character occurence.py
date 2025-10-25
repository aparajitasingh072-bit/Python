string = input("please enter your own word: ")
char = input("please eneter your own character: ")
i = 0
count = 0
while (i < len(string)): 
    if (string[i] == char): 
        count = count + 1
    i = i + 1

print("The total number of Times", char, "has occured = ", count)