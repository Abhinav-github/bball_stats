from basketball_reference_scraper.teams import get_roster, get_team_stats, get_opp_stats, get_roster_stats, get_team_misc
from basketball_reference_scraper.players import get_stats
from basketball_reference_scraper.seasons import get_schedule, get_standings
from basketball_reference_scraper.box_scores import get_box_scores
from basketball_reference_scraper.pbp import get_pbp
from basketball_reference_scraper.shot_charts import get_shot_chart

dict_query = {
    'teams'       : 0,
    'players'     : 1,
    'seasons'     : 2,
    'box scores'  : 3,
    'shot charts' : 4
    }

dict_teams = {
    'roster'       : 0,
    'team stats'   : 1,
    'opp stats'    : 2,
    'roster stats' : 3,
    'misc stats'   : 4
    }

dict_seasons = {
    'schedule'  : 0,
    'standings' : 1
}

def receive_input():
    query = input('What type of data do you want: ')
    if query in dict_query:
        return query
    print('Try again')
    return receive_input()


def parse_input(arg):
    switcher = {
        0: teams(),
        1: get_team_stats(),
        2: get_opp_stats(),
        3: get_roster_stats(),
        4: get_team_misc()
        }
    return switcher.get(arg, "invalid input")

def parse_teams(arg):
    switcher = {
        0: get_roster(),
        1: players(),
        2: seasons(),
        3: box_score(),
        4: shot_charts()
        }
    return switcher.get(arg, "invalid input")

def teams():
    teams_query = input('What type of team data do you want: ')
    if teams_query in dict_teams:
        return teams_query
    print('Try again')
    return teams()

def main():
    type_request = receive_input()
    parse_input(dict_query.get(type_request))

if __name__ == '__main__':
    main()
