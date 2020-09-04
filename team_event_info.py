from bs4 import BeautifulSoup
from itertools import accumulate
from file_soup_methods import Pool_Soup
from file_soup_methods import Bracket_Soup

class Teams_Seeds:
    def __init__(self, pools):
        self.pools = pools
    
    def teams_raw(self):
        teams = []
        raw_pools = [pool.findAll('a') for pool in self.pools]
        for raw_pool in raw_pools:
            for team in raw_pool:
                teams += team
        return teams

    def overall_seeds_raw(self):
        overall_seeds_raw = []
        overall_seeds = []
        spans = [pool.findAll("span", "ng-star-inserted") for pool in self.pools]
        for span in spans:
            for overall_seed_span in span:
                overall_seeds_raw += overall_seed_span.text.split()
        for seed in overall_seeds_raw:
            if len(seed) == 4 or len(seed) == 3:
                overall_seeds.append(seed[1:-1])
        return overall_seeds

    def teams_seeds_dict(self):
        teams_seeds_raw = dict(zip(self.teams_raw(), self.overall_seeds_raw()))
        teams_seeds_sorted = sorted(teams_seeds_raw.items(), key=lambda x: int(x[1]))
        return teams_seeds_sorted

    def teams_unique_ordered(self):
        sorted_teams = []
        for i in self.teams_seeds_dict():
            sorted_teams.append(i[0])
        return sorted_teams
    
    def seeds_ordered(self):
        sorted_seeds = []
        for i in self.teams_seeds_dict():
            sorted_seeds.append(i[1])
        return sorted_seeds