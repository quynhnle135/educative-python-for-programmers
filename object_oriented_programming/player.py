class Player:
    teamName = "Liverpool" # class variables
    teamMembers = []

    def __init__(self, name):
        self.name = name # instance variables
        self.formerTeams = []
        self.teamMembers.append(self.name)

    @classmethod
    def getTeamName(cls):
        return cls.teamName

    @staticmethod
    def demo():
        print("I am a static method")


print(Player.getTeamName())


p1 = Player('Mark')
p1.formerTeams.append('Barcelona')
print("Name: ", p1.name)
print("Team name: ", p1.teamName)
print("Team member: ", p1.teamMembers)


p2 = Player('Steve')
p2.formerTeams.append('Chelsea')
p2.formerTeams.append('Manchester')

# p2.team_name = "Manchester"
print(f"Name: {p2.name}")
print(f"Team name: {p2.teamName}")
print(p2.formerTeams)
print("Team members: ", p2.teamMembers)
