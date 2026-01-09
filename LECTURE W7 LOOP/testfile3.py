citizenship = "Chinese"
Age = 25
registered = True

if citizenship == "Chinese" and Age >= 18:
    if registered:
        print ("You can vote")
    else:
        print ("You cannot vote and you are not registered")


elif citizenship == "Chinese" and Age < 18:
    if registered:
        print ("You cannot vote, Please wait until you are eligible")

else:
    print ("You cannot vote nor register")


