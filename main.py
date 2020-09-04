import os
from os import listdir
from pathlib import Path
from Extensions import TeamDivisionParser


def getsourcenames(path):
    return listdir(path)


# list the files
path = Path(__file__).parent
print(path)
sourcePath = os.path.join(path, 'Source')
print(sourcePath)

# parse the teams
teamDivisions = getsourcenames(sourcePath)
print(teamDivisions)

# prepare the results in a dictionary
result = {}

for teamDivision in teamDivisions:
    result[teamDivision.name] = TeamDivisionParser.parse(teamDivision)

print(result.values())
