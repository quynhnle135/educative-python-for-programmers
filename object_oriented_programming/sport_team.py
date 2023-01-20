class Player:
    def __init__(self, id, name, team_name):
        self.id = id
        self.name = name
        self.team_name = team_name


class Team:
    def __init__(self, name):
        self.name = name
        self.players = []

    def get_number_of_players(self):
        return len(self.players)

    def add_player(self, player):
        self.players.append(player)


class School:
    def __init__(self, name):
        self.name = name
        self.teams = []

    def add_team(self, team):
        self.teams.append(team)

    def get_total_players(self):
        length = 0
        for n in self.teams:
            length = length + (n.get_number_of_players())
        return length


p1 = Player(1, "Harry", "Red")
p2 = Player(2, "Mitch", "Red")
p3 = Player(3, "Jess", "Blue")
p4 = Player(4, "Dean", "Blue")

blue_team = Team("Blue Team")
blue_team.add_player(p3)
blue_team.add_player(p4)

red_team = Team("Red Team")
red_team.add_player(p1)
red_team.add_player(p2)

my_school = School("EW")
my_school.add_team(blue_team)
my_school.add_team(red_team)

print("Total players: ", my_school.get_total_players())