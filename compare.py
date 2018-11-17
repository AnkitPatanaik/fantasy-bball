from basketball_reference_web_scraper import client

YEAR_END = 2018

def get_values(player_list):
    values = []

    players = client.players_season_totals(YEAR_END)
    for player in players:
        if player['name'] in player_list:
            values.append(player)
    return values 

def main():
    team_1 = raw_input("enter comma separated list with players from one team")
    team_2 = raw_input("enter comma separated list with players from the other team")
    
print(get_values(["Joe Harris"]))
