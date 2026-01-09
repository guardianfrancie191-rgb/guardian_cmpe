TeamA = ['ferrari', 'mercedes',"wiliams", "redbull"]
TeamB = ["ferrari", "haas", "astonmartin","haas"]
TeamC = ["ferrari", "Haas","Williams","cadillac"]

teamGroup_list = list(zip(TeamA, TeamB, TeamC))
print(teamGroup_list)
print(teamGroup_list[2])
print(teamGroup_list[2][1])

teamGroup_Plus = TeamA + TeamB + TeamC
print(teamGroup_Plus)

TeamA.extend(TeamB)
TeamA.extend(TeamC)
print(TeamA)


TeamA = {'ferrari', 'mercedes',"wiliams", "redbull"}
TeamB = {"ferrari", "haas", "astonmartin","haas"}
TeamsGroupListOfSet =[TeamA, TeamB,]
print(TeamsGroupListOfSet)

