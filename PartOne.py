vname = input("enter variable name: ")

for letter in vname:
    if letter == letter.lower() :
        print(letter, end="")
    else:
        print("_"+letter.lower(),end="")
print("")
