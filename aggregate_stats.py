from basketball_reference_web_scraper import client

YEAR_END = 2019
PRECISION = 2

# Parse the list of players and create a list
def get_values(player_list_string):
    values = []
    
    player_list = player_list_string.split(",")
    player_list = [x.lower().strip() for x in player_list] #iterates over list and makes everything lower()

    players = client.players_season_totals(YEAR_END)
    for player in players:
        if player['name'].lower() in player_list:
            values.append(player)
    return values 

# Get the sum total of all stats for the players inputted
def get_stats(player_dict):
    stats = {'points': 0, 'assists': 0, 'rebounds': 0, 'steals': 0, 'blocks': 0, 'made_field_goals': 0, 'attempted_field_goals': 0,'fg%': 0,  'made_free_throws': 0, 'attempted_free_throws': 0, 'ft%': 0, '3pm': 0, 'turnovers' : 0}
    
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
    stats['fg%'] = round(stats['made_field_goals']/stats['attempted_field_goals'] * 100, PRECISION)
    stats['ft%'] = round(stats['made_free_throws']/stats['attempted_free_throws'] * 100, PRECISION)
    return stats

def pretty_print(dictionary):
    print("\nSTATS:")
    for item in dictionary:
        print(item.capitalize()+": ", dictionary[str(item)])
    print("\n")

def main():
    team_1 = input("Enter comma separated list players. Please be wary of spelling!: \n")
    team1_players = get_values(team_1)
    pretty_print(get_stats(team1_players))
    
main()
