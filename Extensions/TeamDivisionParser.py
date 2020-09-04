import pandas


class TeamDivisionParser:
    @staticmethod
    def parse(self, teamDivision):
        return self.teams_df(teamDivision)

    def full_teams(self):
        full_teams = []
        for d in self.teams_divisions:
            full_teams += d.teams()
        return full_teams

    def full_divisions(self):
        full_divisions = []
        for d in self.teams_divisions:
            full_divisions += d.divisions()
        return full_divisions

    def teams_dictionary(self):
        teams_divisions_dictionary = dict(zip(self.full_teams(), self.full_divisions()))
        return teams_divisions_dictionary

    def teams_unique(self):
        teams_unique = list(self.teams_dictionary().keys())
        return teams_unique

    def divisions(self):
        divisions = list(self.teams_dictionary().values())
        return divisions

    def nulls(self):
        nulls = ['null'] * len(self.teams_unique())
        return nulls

    def teams_df(self, teamDivision):
        teams = pandas.DataFrame(
            {'team_name': self.teams_unique(), 'team_city': self.nulls(), 'division': self.divisions(),
             'region': self.nulls()})
        teams.index += 1
        return teams
