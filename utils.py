from basketball_reference_web_scraper import client

YEAR_END = 2019
PRECISION = 2

def pretty_print(dictionary):
    print("\nSTATS:")
    for item in dictionary:
        print(item.capitalize()+": ", dictionary[str(item)])
    print("\n")


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