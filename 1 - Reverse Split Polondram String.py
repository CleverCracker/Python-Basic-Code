def Reverse(str_word):
    return str_word[::-1]


Name = input("Please Enter Your Full Name = ")
print("Reverse Name = " + Reverse(Name).lower())

nameList = Name.lower().split(" ")
if nameList.__len__() < 2:
    print("Second Name Not Found")
else:
    if nameList[1] == Reverse(nameList[1]):
        print("Second Name is Polindrame")
    else:
        print("Second Name is Not Polindrame")

# For  Full Name Polindrame Checking

if Reverse(Name.lower()) == Name.lower():
    print("Name is Polindrame")
else:
    print("Name is not Polindrame")
