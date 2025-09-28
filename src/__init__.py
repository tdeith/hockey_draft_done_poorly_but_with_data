from goalies import  *
from teams import *
from skaters import *

if __name__ == '__main__':
    all_teams = AllTeamData('../data/teams.csv')
    all_goalies: list[RelevantGoalieData] = AllGoalieData('../data/goalies.csv', all_teams).goalies
    all_goalies.sort(key=lambda g: g.total_expected_value, reverse=True)

    for goalie in all_goalies[:100]:
        team_shots_against = goalie.team.shots_against
        ex_shots_against_pg = goalie.team.shots_against / goalie.team.games_played
        shots_against_discrepancy = (goalie.goals_against_pg + goalie.saves_pg - ex_shots_against_pg) * goalie.games_played
        print(f"\
{goalie.name:<30},\
{goalie.team.name_abbr},\
{goalie.total_expected_value:.2f},\
{goalie.expected_value_pg:.2f},\
{goalie.games_played:.1f},\
{shots_against_discrepancy:.1f},\
{goalie.goals_against_pg:.2f}")

    all_skaters = AllSkaters('../data/skaters.csv')
    defense = all_skaters.ranked_defense()[:90]
    centers = all_skaters.ranked_centers()[:60]
    lefties = all_skaters.ranked_lefties()[:60]
    righties = all_skaters.ranked_righties()[:60]
#    all_skaters = defense + centers + lefties + righties
 #   all_skaters.sort(key=lambda s: s.expected_value, reverse=True)
    for skater in all_skaters.skaters[:300]:
        print(f"{skater.pos},{skater.name},{skater.team},{skater.expected_value:.0f},{skater.expected_value_pg:.1f}")
