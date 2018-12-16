from basketball_reference_web_scraper import client
from utils import pretty_print, get_values, get_stats,PRECISION

/
def get_average(stats):
    games_played = stats['games_played']
    avg_dict= {'points': 0, 'assists': 0, 'rebounds': 0, 'steals': 0, 'blocks': 0, 'made_field_goals': 0, 'attempted_field_goals': 0,'fg%': 0,  'made_free_throws': 0, 'attempted_free_throws': 0, 'ft%': 0, '3pm': 0, 'turnovers': 0}
    avg_dict['fg%'] = stats['fg%']
    avg_dict['ft%'] = stats['ft%']
    for stat in stats:
        avg_dict['assists'] = round(stats['assists'] / games_played , PRECISION)
        avg_dict['rebounds'] = round(stats['rebounds'] / games_played, PRECISION)
        avg_dict['steals'] = round(stats['steals'] / games_played , PRECISION)
        avg_dict['blocks'] = round(stats['blocks'] / games_played, PRECISION)
        avg_dict['made_field_goals'] = round(stats['made_field_goals'] / games_played, PRECISION)
        avg_dict['attempted_field_goals'] = round(stats['attempted_field_goals'] / games_played, PRECISION)
        avg_dict['made_free_throws'] = round(stats['made_free_throws'] / games_played, PRECISION) 
        avg_dict['attempted_free_throws'] = round(stats['attempted_free_throws'] / games_played , PRECISION)
        avg_dict['3pm'] = round(stats['3pm'] / games_played , PRECISION)
        avg_dict['turnovers'] = round(stats['turnovers'] / games_played, PRECISION)
        avg_dict['games_played'] = games_played
        avg_dict['points'] =  round((stats['made_field_goals'] * 2 + stats['3pm'] + stats['made_free_throws']) / games_played, PRECISION)
    return avg_dict

def main():
    team_1 = input("Enter comma separated list players. Please be wary of spelling!: \n")
    team1_players = get_values(team_1)
    pretty_print(get_average(get_stats(team1_players)))
    
main()
