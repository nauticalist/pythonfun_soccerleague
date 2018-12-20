import csv

# Teams dict with empty player lists
teams = {"Sharks": [], "Dragons": [], "Raptors": []}
date_of_first_practice = "01 January 2019 09:00 am"


def get_players_from_csv():
    """
    Get list of players from the csv file and return experienced
    and noobie players as dict
    """
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
    """
    Get experienced and noobie players
    Calculate players per team
    Assign players to teams
    """
    experienced_players = players['experienced players']
    noob_players = players['noob players']
    experienced_players_per_team = len(experienced_players) // len(teams)
    noob_players_per_team = len(noob_players) // len(teams)
    for team, players in teams.items():
        for i in range(experienced_players_per_team):
            players.append(experienced_players.pop(0))
        for i in range(noob_players_per_team):
            players.append(noob_players.pop(0))
    return teams


def create_team_lists_file(teams):
    """
    Create a list which inclued teams and its members and
    save it to teams text file.
    (Players name, Has experience, Player's guardians name)
    """
    with open('teams.txt', mode='w') as textfile:
        for team, players in teams.items():
            textfile.write("{}\n".format(team))
            for char in team:
                textfile.write("=")
            textfile.write("\n")
            for value in players:
                textfile.write("{}, {}, {}\n".format(
                    value['Name'],
                    value['Soccer Experience'],
                    value['Guardian Name(s)']))
            textfile.write("\n\n\n")


def create_player_list_with_teams(teams):
    """
    Create player list with the guardian(s) name(s), player's name,
    team name, and date & time of first practice.
    """
    player_list = []
    for team, players in teams.items():
        for value in players:
            member = {
                'Guardian Name(s)': value['Guardian Name(s)'],
                'Name': value['Name'],
                'Team Name': team,
                'First Practice': date_of_first_practice,
            }
            player_list.append(member)
    return player_list


def create_message_files(player_list):
    """
    Create message files for the players guardians(s)
    """
    for player in player_list:
        filename = "{}.{}".format(
            player['Name'].lower().replace(" ", "_"),
            "txt")
        with open(filename, mode='w') as textfile:
            textfile.write("Dear {},\n\n\n".format(player['Guardian Name(s)']))
            textfile.write("Player Name: {}\n".format(player['Name']))
            textfile.write("Team Name: {}\n".format(player['Team Name']))
            textfile.write("First Practice: {}\n".format(
                player['First Practice']))


if __name__ == '__main__':
    # Step 1: Get players
    players = get_players_from_csv()
    # Step 2: Create teams
    teams = create_teams(teams, players)
    # Step 3: Create teams.txt file with name of the team followed by
    # the members of the team
    create_team_lists_file(teams)
    # Step 4: Create player list for guardian's messages
    player_list = create_player_list_with_teams(teams)
    # Step 5: Create message files for the players guardian(s)
    create_message_files(player_list)
