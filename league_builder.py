import csv

teams = {"Sharks": [], "Dragons": [], "Raptors": []}


def get_players_from_csv():
    with open('soccer_players.csv', newline='') as csvfile:
        players = csv.DictReader(csvfile, delimiter=",")
        experienced_players = []
        noob_players = []
        for player in players:
            if player['Soccer Experience'] == 'YES':
                experienced_players.append(player)
            else:
                noob_players.append(player)
        return {'experienced players': experienced_players,
                'noob players': noob_players}


def create_teams(teams, players):
    experienced_players = players['experienced players']
    noob_players = players['noob players']
    experienced_players_per_team = len(experienced_players) // len(teams)
    noob_players_per_team = len(noob_players) // len(teams)
    for team, players in teams.items():
        for i in range(experienced_players_per_team):
            players.append(experienced_players.pop(0))
        for i in range(noob_players_per_team):
            players.append(noob_players.pop(0))
    for team, players in teams.items():
        print(team, ': ', players)


if __name__ == '__main__':
    players = get_players_from_csv()
    create_teams(teams, players)
