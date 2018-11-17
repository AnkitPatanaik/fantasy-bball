from basketball_reference_web_scraper import client

YEAR_END = 2018

def get_values(player_list_string):
    values = []
    player_list = player_list_string.split(", ")
    players = client.players_season_totals(YEAR_END)
    for player in players:
        if player['name'] in player_list:
            values.append(player)
    return values 

def get_stats(player_dict):
    stats = {'points': 0, 'assists': 0, 'rebounds': 0, 'steals': 0, 'blocks': 0, 'made_field_goals': 0, 'attempted_field_goals': 0, 'made_free_throws': 0, 'attempted_free_throws': 0, '3pm': 0, 'turnovers' : 0}
    for player in player_dict:
        stats['points'] += player['made_field_goals'] * 2 + player['made_three_point_field_goals'] + player['made_free_throws']
        stats['assists'] += player['assists']
        stats['rebounds'] += player['offensive_rebounds'] + player['defensive_rebounds']
        stats['steals'] += player['steals']
        stats['blocks'] += player['blocks']
        stats['made_field_goals'] += player['made_field_goals'] 
        stats['attempted_field_goals'] += player['attempted_field_goals']
        stats['made_free_throws'] += player['made_free_throws'] 
        stats['attempted_free_throws'] += player['attempted_free_throws']
        stats['3pm'] += player['made_three_point_field_goals']
        stats['turnovers'] += player['turnovers']
    return stats


def main():
    team_1 = input("enter comma separated list with players from one team: \n")
    team1_players = get_values(team_1)
    print("STATS: \n", get_stats(team1_players))
    #team_2 = raw_input("enter comma separated list with players from the other team")
    
main()
