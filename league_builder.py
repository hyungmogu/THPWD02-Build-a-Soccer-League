import csv
import io

def get_players():
    with open("soccer_players.csv", "r") as csvFile:
        csvReader = csv.DictReader(csvFile, delimiter=",")
        rows = list(csvReader)

    return rows


def get_experienced(players):
    output = []

    for player in players:
        if player["Soccer Experience"] == "YES":
            output.append(player)

    return output


def get_inexperienced(players):
    output = []

    for player in players:
        if player["Soccer Experience"] == "NO":
            output.append(player)

    return output


if __name__ == "__main__":
    teams = ["Sharks","Dragons","Raptors"]
    players = get_players()
    players_by_team = {team: [] for team in teams}

    # 1. separate players by experience
    players_experienced = get_experienced(players)
    players_experienced_per_team = int(len(players_experienced) / len(teams))

    players_inexperienced = get_inexperienced(players)
    players_inexperienced_per_team = int(len(players_inexperienced) / len(teams))

    # 2. add equal number of experienced, and inexperienced players to teams
    for index, team in enumerate(teams):
        slice_start_experienced = index * players_experienced_per_team
        slice_end_experienced = slice_start_experienced + players_experienced_per_team

        slice_start_inexperienced = index * players_inexperienced_per_team
        slice_end_inexperienced = slice_start_inexperienced + players_inexperienced_per_team

        players_by_team.update({team: players_by_team[team] + players_experienced[slice_start_experienced:slice_end_experienced]})
        players_by_team.update({team: players_by_team[team] + players_inexperienced[slice_start_inexperienced:slice_end_inexperienced]})

    # 3. add players to file in the following format
    # TEAM
    # NAME, EXPERIENCE, GUARDIAN NAMES
    with open("teams.txt", "a") as textFile:

        for team, players in players_by_team.items():
            textFile.write("{0}\n".format(team))
            for player in players:
                textFile.write("{0}, {1}, {2}\n".format(player['Name'],player['Soccer Experience'],player['Guardian Name(s)']))


