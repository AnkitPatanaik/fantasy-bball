from basketball_reference_web_scraper import client

YEAR_END = 2019

def get_values(player_list):
    values = []

    players = client.players_season_totals(YEAR_END)
    for player in players:
        if player['name'] in player_list:
            values.append(player)
    return values 

def get_stats(player_dict):
    stats = {'points': 0, 'assists': 0, 'rebounds': 0, 'steals': 0, 'blocks': 0, 'fg%': 0, 'ft%': 0, '3pm': 0, 'turnovers' : 0}
    for player in player_dict:
        stats['points'] += player['made_field_goals'] * 2 + player['made_three_point_field_goals'] + player['made_free_throws']
        return stats


def main():
    team_1 = raw_input("enter comma separated list with players from one team")
    team_2 = raw_input("enter comma separated list with players from the other team")
    
#print(get_stats(get_values(["Joe Harris", "Kevin Durant"])))
print(get_values(["Joe Harris"]))
