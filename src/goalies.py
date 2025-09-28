import csv

from teams import AllTeamData, RelevantTeamData

### CSV columns:
### playerId
### season
### name
### team
### shutouts
### position
### situation
### games_played
### icetime
### xGoals
### goals
### unblocked_shot_attempts
### xRebounds
### rebounds
### xFreeze
### freeze
### xOnGoal
### ongoal
### xPlayStopped
### playStopped
### xPlayContinuedInZone
### playContinuedInZone
### xPlayContinuedOutsideZone
### playContinuedOutsideZone
### flurryAdjustedxGoals
### lowDangerShots
### mediumDangerShots
### highDangerShots
### lowDangerxGoals
### mediumDangerxGoals
### highDangerxGoals
### lowDangerGoals
### mediumDangerGoals
### highDangerGoals
### blocked_shot_attempts
### penalityMinutes
### penalties

class RelevantGoalieData:
    def __init__(self, raw_goalie_data, team: RelevantTeamData):
        self.team = team
        self.name = raw_goalie_data['name']
        self.games_played = float(raw_goalie_data['icetime']) / 3600.0
        self.goals_against_pg = float(raw_goalie_data['goals']) / self.games_played
        self.saves_pg = (
            float(raw_goalie_data['ongoal']) -
            float(raw_goalie_data['goals'])
        ) / self.games_played
        self.saves_above_expectation = float(raw_goalie_data['xGoals']) / self.games_played - self.goals_against_pg
        self.shutouts_pg = float(raw_goalie_data['shutouts']) / self.games_played
        self.expected_value_pg = self._expected_value_per_game()
        self.total_expected_value = self.expected_value_pg * self.games_played

    def _expected_value_per_game(self) -> float:
        return (
            self.saves_pg * 0.6
            + self.shutouts_pg * 4.0
            - self.goals_against_pg
            - self.games_played / 82.0 * 6.0
        )

class AllGoalieData:
    def __init__(self, goalie_csv_in: str, all_teams: AllTeamData):
        self.goalies: list[RelevantGoalieData] = []
        with open(goalie_csv_in, 'r') as csv_file:
            for row in csv.DictReader(csv_file):
                if row['situation'] != 'all':
                    continue
                team = all_teams.get_team(row['team'])
                goalie = RelevantGoalieData(row, team)
                self.goalies.append(goalie)
