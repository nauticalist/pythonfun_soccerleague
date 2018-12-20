import csv


def get_players_from_csv():
    with open('soccer_players.csv', newline='') as csvfile:
        players = csv.DictReader(csvfile, delimiter=",")
        rows = list(players)
        return rows


if __name__ == '__main__':
    players = get_players_from_csv()
    for player in players:
        print(player['Name'])
