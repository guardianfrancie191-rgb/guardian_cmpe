TeamA = {"ferrari", "haas", "astonmartin","haas"}
TeamB = {"ferrari", "Haas","Williams","cadillac"}
print(TeamA)
TeamA.add("audi")
print(TeamA)


TeamsUnion = TeamA.union(TeamB)
print(TeamsUnion)
TeamsIntersection = TeamA.intersection(TeamB)
print(TeamsIntersection)
TeamDifference = TeamA.difference(TeamB)
print(TeamDifference)

