myInfo = {"Name" : "Francie N. Guardian", "Age" : 19, "Gender" : "Male", "Address": "Sta. Mesa"}
print(myInfo)
print(myInfo["Age"])
print(myInfo["Gender"])
print(myInfo["Address"])
print(myInfo["Name"])
print(myInfo.get("Name"))
myInfo["Name"] = "Lewis Hamilton"
print(myInfo)
print(myInfo["Age"])
myInfo.update({"Gender": 4})
print(myInfo)

myInfo = {
    "Name":  {
        "FirstName ": "Lewis",
        "LastName": "Hamilton",
    },
    "Age": 19,
    "Interest": [ "Formula 1", "Formula 2", "Formula 3" ]

}




print(myInfo)
print(myInfo["Name"]["FirstName "])
print(myInfo["Interest"])
print(myInfo["Age"])
print(myInfo["Name"]["FirstName "] + " " + myInfo ["Name"]["LastName"])
print(myInfo["Interest"][1])