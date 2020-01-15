from basketball_reference_scraper.teams import get_roster, get_team_stats, get_opp_stats, get_roster_stats, get_team_misc
from basketball_reference_scraper.players import get_stats
from basketball_reference_scraper.seasons import get_schedule, get_standings
from basketball_reference_scraper.box_scores import get_box_scores
from basketball_reference_scraper.pbp import get_pbp
from basketball_reference_scraper.shot_charts import get_shot_chart

def receive_input():
    query = input('What type of data do you want: ')
    if query == 'teams' or query == 'players' or query == 'seasons' or query == 'box scores' or query == 'shot charts':
        return query
    print('Try again')
    return receive_input()


# def parse_input(arg):
#    switcher = {
#            0: teams(),
#            1: players(),
#            2: seasons(),
#            3: box_scores(),
#            4: shot_charts()
#        }
#    return switcher.get(arg, "invalid input")

def main():
    type_request = receive_input()
    if type_request == 'teams':
        teams()
        break
    elif type_request == 'players':
        players()
        break
    elif type_request == 'box scores':
        box_scores()
        break
    elif type_request == 'shot charts':
        shot_charts()
        break

if __name__ == '__main__':
    main()
