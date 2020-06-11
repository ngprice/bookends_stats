from bs4 import BeautifulSoup
import requests
import json

def read_file():
    file = open(r'C:\Users\hunte\Desktop\Frisbee Stats\ultiarchive_webscraper.py\2010_club_open_nationals.html')
    data = file.read()
    file.close()
    return data

content = BeautifulSoup(read_file(), 'html.parser')
first_team = a.text
teams = []
seeds = []
records = []

for team in content.find_all('app-schedule-team', {'class': "ng-star-inserted"}):
    teams = team.find_all('a', {'class': "ng-star-inserted"})
    for team in teams:
        print(team.text)

for seed in content.find_all('span', {'class': 'seed'}):
    seeds.append(seed.text)

for record in content.find_all('span', {'class': 'record'}):
    records.append(record.text)
for record in records:
    record[:-2]

print(first_team)

class Pool:
    def __init__ (self, team, seed, record):
        self.team = team
        self.seed = seed
        self.record = record

'''
teams = []
for tag in tags():
    if tag not in teams:
        teams.append(tag.text)
    print(teams)
    #team_names = team_names.append(tag.text)
'''