from Models import TeamDivisionType


class Team:
    def __init__(self, divtype: TeamDivisionType, division):
        self.divtype = divtype
        self.division = division
