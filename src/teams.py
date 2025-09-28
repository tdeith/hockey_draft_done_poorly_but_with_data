import csv
from typing import Any

### CSV dict columns:
###
### team
### season
### name
### team
### position
### situation
### games_played
### xGoalsPercentage
### corsiPercentage
### fenwickPercentage
### iceTime
### xOnGoalFor
### xGoalsFor
### xReboundsFor
### xFreezeFor
### xPlayStoppedFor
### xPlayContinuedInZoneFor
### xPlayContinuedOutsideZoneFor
### flurryAdjustedxGoalsFor
### scoreVenueAdjustedxGoalsFor
### flurryScoreVenueAdjustedxGoalsFor
### shotsOnGoalFor
### missedShotsFor
### blockedShotAttemptsFor
### shotAttemptsFor
### goalsFor
### reboundsFor
### reboundGoalsFor
### freezeFor
### playStoppedFor
### playContinuedInZoneFor
### playContinuedOutsideZoneFor
### savedShotsOnGoalFor
### savedUnblockedShotAttemptsFor
### penaltiesFor
### penalityMinutesFor
### faceOffsWonFor
### hitsFor
### takeawaysFor
### giveawaysFor
### lowDangerShotsFor
### mediumDangerShotsFor
### highDangerShotsFor
### lowDangerxGoalsFor
### mediumDangerxGoalsFor
### highDangerxGoalsFor
### lowDangerGoalsFor
### mediumDangerGoalsFor
### highDangerGoalsFor
### scoreAdjustedShotsAttemptsFor
### unblockedShotAttemptsFor
### scoreAdjustedUnblockedShotAttemptsFor
### dZoneGiveawaysFor
### xGoalsFromxReboundsOfShotsFor
### xGoalsFromActualReboundsOfShotsFor
### reboundxGoalsFor
### totalShotCreditFor
### scoreAdjustedTotalShotCreditFor
### scoreFlurryAdjustedTotalShotCreditFor
### xOnGoalAgainst
### xGoalsAgainst
### xReboundsAgainst
### xFreezeAgainst
### xPlayStoppedAgainst
### xPlayContinuedInZoneAgainst
### xPlayContinuedOutsideZoneAgainst
### flurryAdjustedxGoalsAgainst
### scoreVenueAdjustedxGoalsAgainst
### flurryScoreVenueAdjustedxGoalsAgainst
### shotsOnGoalAgainst
### missedShotsAgainst
### blockedShotAttemptsAgainst
### shotAttemptsAgainst
### goalsAgainst
### reboundsAgainst
### reboundGoalsAgainst
### freezeAgainst
### playStoppedAgainst
### playContinuedInZoneAgainst
### playContinuedOutsideZoneAgainst
### savedShotsOnGoalAgainst
### savedUnblockedShotAttemptsAgainst
### penaltiesAgainst
### penalityMinutesAgainst
### faceOffsWonAgainst
### hitsAgainst
### takeawaysAgainst
### giveawaysAgainst
### lowDangerShotsAgainst
### mediumDangerShotsAgainst
### highDangerShotsAgainst
### lowDangerxGoalsAgainst
### mediumDangerxGoalsAgainst
### highDangerxGoalsAgainst
### lowDangerGoalsAgainst
### mediumDangerGoalsAgainst
### highDangerGoalsAgainst
### scoreAdjustedShotsAttemptsAgainst
### unblockedShotAttemptsAgainst
### scoreAdjustedUnblockedShotAttemptsAgainst
### dZoneGiveawaysAgainst
### xGoalsFromxReboundsOfShotsAgainst
### xGoalsFromActualReboundsOfShotsAgainst
### reboundxGoalsAgainst
### totalShotCreditAgainst
### scoreAdjustedTotalShotCreditAgainst
### scoreFlurryAdjustedTotalShotCreditAgainst

class RelevantTeamData:
    def __init__(self, raw_csv_data):
        self.name_abbr = raw_csv_data['name']
        self.shots_against = float(raw_csv_data['shotsOnGoalAgainst'])
        self.penalties = float(raw_csv_data['penaltiesAgainst'])
        self.goals_against = float(raw_csv_data['goalsAgainst'])
        self.games_played = float(raw_csv_data['games_played'])
        self.blocked_shots = float(raw_csv_data['blockedShotAttemptsAgainst'])

class AllTeamData:
    def __init__(self, csv_file_in: str):
        teams = dict()
        with open(csv_file_in, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                if row['situation'].lower() != 'all':
                    continue
                new_team = RelevantTeamData(row)
                teams[new_team.name_abbr] = new_team
        self.__teams = teams
        self.all_teams = teams.values()

    def get_team(self, name_abbr: str) -> RelevantTeamData:
        return self.__teams.get(name_abbr)
