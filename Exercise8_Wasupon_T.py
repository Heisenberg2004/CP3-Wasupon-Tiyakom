usernameInput = input("Username : ")
passwordInput = input("Password : ")
if usernameInput == "admin" and passwordInput == "1010" :
    print("Done ! ")
    print("------ WShop ------")
    print("1.Cake : 129THB")
    print("2.Pizza : 142THB")
    print("3.Water : 15THB")
    print("4.Orange : 46THB")
    cake = 129
    pizza = 142
    water = 151
    orange = 46
    userSelected = int(input(">>"))
    if userSelected == 1:
        Howmany = int(input("How many? : "))
        result = cake * Howmany
        print(result, "THB")
    elif userSelected == 2:
        Howmany = int(input("How many? : "))
        result = pizza * Howmany
        print(result, "THB")
    elif userSelected == 3:
        Howmany = int(input("How many? : "))
        result = water * Howmany
        print(result, "THB")
    elif userSelected == 4:
        Howmany = int(input("How many? : "))
        result = orange * Howmany
        print(result, "THB")
    else:
        print("Don't have.")

else:
    print("Pleas try again!")
