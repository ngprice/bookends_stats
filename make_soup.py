from bs4 import BeautifulSoup
from files import Files

class Make_Soup:
    def __init__(self, file):
        self.file = file

    def read_file(self):    
        file = open(self.file)
        data = file.read()
        file.close()
        return data

    def make_soup(self):
        soup = BeautifulSoup(self.read_file(), 'html.parser')
        return soup
    
    def event_name(self):
        tournament = self.make_soup().find('h1').text.split()
        tournament = tournament[:tournament.index('-')]
        tournament = ' '.join(tournament)
        return tournament
    
    def event_date(self):
        raw_date = self.make_soup().find('h2').text.split()
        return raw_date
    
    def event_year(self):
        event_year = self.event_date()[-1]
        return event_year
    
    def event_division(self):
        division_raw = self.make_soup().findAll("span", "mat-button-wrapper")[-1].text.split()[1]
        return division_raw

    def pools(self):
        pools = self.make_soup().find_all('app-schedule-pool')
        return pools
    
    def brackets(self):
        brackets = self.make_soup().find_all('app-schedule-bracket')
        return brackets

class File_Soup:
    club_2010_mixed_nationals_soup = Make_Soup(Files.club_2010_mixed_nationals_file)
    club_2010_open_nationals_soup = Make_Soup(Files.club_2010_open_nationals_file)
    club_2010_womxns_nationals_soup = Make_Soup(Files.club_2010_womxns_nationals_file)
    club_2011_mixed_nationals_soup = Make_Soup(Files.club_2011_mixed_nationals_file)
    club_2011_open_nationals_soup = Make_Soup(Files.club_2011_open_nationals_file)
    club_2011_womxns_nationals_soup = Make_Soup(Files.club_2011_womxns_nationals_file)
    club_2012_mixed_us_open_soup = Make_Soup(Files.club_2012_mixed_us_open_file)
    club_2012_open_us_open_soup = Make_Soup(Files.club_2012_open_us_open_file)
    club_2012_womxns_us_open_soup = Make_Soup(Files.club_2012_womxns_us_open_file)
    club_2012_mixed_nationals_soup = Make_Soup(Files.club_2012_mixed_nationals_file)
    club_2012_open_nationals_soup = Make_Soup(Files.club_2012_open_nationals_file)
    club_2012_womxns_nationals_soup = Make_Soup(Files.club_2012_womxns_nationals_file)
    club_2013_mixed_us_open_soup = Make_Soup(Files.club_2013_mixed_us_open_file)
    club_2013_open_us_open_soup = Make_Soup(Files.club_2013_open_us_open_file)
    club_2013_womxns_us_open_soup = Make_Soup(Files.club_2013_womxns_us_open_file)
    club_2013_open_pe_challenge_soup = Make_Soup(Files.club_2013_open_pe_challenge_file)
    club_2013_womxns_pe_challenge_soup = Make_Soup(Files.club_2013_womxns_pe_challenge_file)
    club_2013_mixed_pe_challenge_soup = Make_Soup(Files.club_2013_mixed_pe_challenge_file)
    club_2013_open_es_challenge_co_soup = Make_Soup(Files.club_2013_open_es_challenge_co_file)
    club_2013_womxns_es_challenge_co_soup = Make_Soup(Files.club_2013_womxns_es_challenge_co_file)
    club_2013_mixed_es_challenge_wa_soup = Make_Soup(Files.club_2013_mixed_es_challenge_wa_file)
    club_2013_womxns_esf_challenge_wa_soup = Make_Soup(Files.club_2013_womxns_esf_challenge_wa_file)
    club_2013_mixed_pf_finale_soup = Make_Soup(Files.club_2013_mixed_pf_finale_file)
    club_2013_open_pf_finale_soup = Make_Soup(Files.club_2013_open_pf_finale_file)
    club_2013_womxns_pf_finale_soup = Make_Soup(Files.club_2013_womxns_pf_finale_file)
    club_2013_mixed_nationals_soup = Make_Soup(Files.club_2013_mixed_nationals_file)
    club_2013_open_nationals_soup = Make_Soup(Files.club_2013_open_nationals_file)
    club_2013_womxns_nationals_soup = Make_Soup(Files.club_2013_womxns_nationals_file)
    club_2014_mixed_us_open_soup = Make_Soup(Files.club_2014_mixed_us_open_file)
    club_2014_open_us_open_soup = Make_Soup(Files.club_2014_open_us_open_file)
    club_2014_womxns_us_open_soup = Make_Soup(Files.club_2014_womxns_us_open_file)
    club_2014_open_pe_challenge_va_soup = Make_Soup(Files.club_2014_open_pe_challenge_va_file)
    club_2014_womxns_pe_challenge_va_soup = Make_Soup(Files.club_2014_womxns_pe_challenge_va_file)
    club_2014_mixed_pe_challenge_ny_soup = Make_Soup(Files.club_2014_mixed_pe_challenge_ny_file)
    club_2014_mixed_es_challenge_soup = Make_Soup(Files.club_2014_mixed_es_challenge_file)
    club_2014_open_es_challenge_soup = Make_Soup(Files.club_2014_open_es_challenge_file)
    club_2014_womxns_es_challenge_soup = Make_Soup(Files.club_2014_womxns_es_challenge_file)
    club_2014_mixed_pf_finale_soup = Make_Soup(Files.club_2014_mixed_pf_finale_file)
    club_2014_open_pf_finale_soup = Make_Soup(Files.club_2014_open_pf_finale_file)
    club_2014_womxns_pf_finale_soup = Make_Soup(Files.club_2014_womxns_pf_finale_file)
    club_2014_mixed_nationals_soup = Make_Soup(Files.club_2014_mixed_nationals_file)
    club_2014_open_nationals_soup = Make_Soup(Files.club_2014_open_nationals_file)
    club_2014_womxns_nationals_soup = Make_Soup(Files.club_2014_womxns_nationals_file)
    club_2015_mixed_us_open_soup = Make_Soup(Files.club_2015_mixed_us_open_file)
    club_2015_open_us_open_soup = Make_Soup(Files.club_2015_open_us_open_file)
    club_2015_womxns_us_open_soup = Make_Soup(Files.club_2015_womxns_us_open_file)
    club_2015_mixed_es_challenge_soup = Make_Soup(Files.club_2015_mixed_es_challenge_file)
    club_2015_open_es_challenge_soup = Make_Soup(Files.club_2015_open_es_challenge_file)
    club_2015_womxns_es_challenge_soup = Make_Soup(Files.club_2015_womxns_es_challenge_file)
    club_2015_mixed_pe_challenge_soup = Make_Soup(Files.club_2015_mixed_pe_challenge_file)
    club_2015_open_pe_challenge_soup = Make_Soup(Files.club_2015_open_pe_challenge_file)
    club_2015_womxns_pe_challenge_soup = Make_Soup(Files.club_2015_womxns_pe_challenge_file)
    club_2015_mixed_sf_invite_soup = Make_Soup(Files.club_2015_mixed_sf_invite_file)
    club_2015_open_sf_invite_soup = Make_Soup(Files.club_2015_open_sf_invite_file)
    club_2015_womxns_sf_invite_soup = Make_Soup(Files.club_2015_womxns_sf_invite_file)
    club_2015_mixed_pf_finale_soup = Make_Soup(Files.club_2015_mixed_pf_finale_file)
    club_2015_open_pf_finale_soup = Make_Soup(Files.club_2015_open_pf_finale_file)
    club_2015_womxns_pf_finale_soup = Make_Soup(Files.club_2015_womxns_pf_finale_file)
    club_2015_mixed_nationals_soup = Make_Soup(Files.club_2015_mixed_nationals_file)
    club_2015_open_nationals_soup = Make_Soup(Files.club_2015_open_nationals_file)
    club_2015_womxns_nationals_soup = Make_Soup(Files.club_2015_womxns_nationals_file)
    club_2016_mixed_us_open_soup = Make_Soup(Files.club_2016_mixed_us_open_file)
    club_2016_open_us_open_soup = Make_Soup(Files.club_2016_open_us_open_file)
    club_2016_womxns_us_open_soup = Make_Soup(Files.club_2016_womxns_us_open_file)
    club_2016_mixed_es_challenge_soup = Make_Soup(Files.club_2016_mixed_es_challenge_file)
    club_2016_open_es_challenge_soup = Make_Soup(Files.club_2016_open_es_challenge_file)
    club_2016_womxns_es_challenge_soup = Make_Soup(Files.club_2016_womxns_es_challenge_file)
    club_2016_mixed_pe_challenge_soup = Make_Soup(Files.club_2016_mixed_pe_challenge_file)
    club_2016_open_pe_challenge_soup = Make_Soup(Files.club_2016_open_pe_challenge_file)
    club_2016_womxns_pe_challenge_soup = Make_Soup(Files.club_2016_womxns_pe_challenge_file)
    club_2016_mixed_sf_invite_soup = Make_Soup(Files.club_2016_mixed_sf_invite_file)
    club_2016_open_sf_invite_soup = Make_Soup(Files.club_2016_open_sf_invite_file)
    club_2016_womxns_sf_invite_soup = Make_Soup(Files.club_2016_womxns_sf_invite_file)
    club_2016_mixed_pf_finale_soup = Make_Soup(Files.club_2016_mixed_pf_finale_file)
    club_2016_open_pf_finale_soup = Make_Soup(Files.club_2016_open_pf_finale_file)
    club_2016_womxns_pf_finale_soup = Make_Soup(Files.club_2016_womxns_pf_finale_file)
    club_2016_mixed_nationals_soup = Make_Soup(Files.club_2016_mixed_nationals_file)
    club_2016_open_nationals_soup = Make_Soup(Files.club_2016_open_nationals_file)
    club_2016_womxns_nationals_soup = Make_Soup(Files.club_2016_womxns_nationals_file)
    club_2017_mixed_pe_challenge_soup = Make_Soup(Files.club_2017_mixed_pe_challenge_file)
    club_2017_open_pe_challenge_soup = Make_Soup(Files.club_2017_open_pe_challenge_file)
    club_2017_womxns_pe_challenge_soup = Make_Soup(Files.club_2017_womxns_pe_challenge_file)
    club_2017_mixed_us_open_soup = Make_Soup(Files.club_2017_mixed_us_open_file)
    club_2017_open_us_open_soup = Make_Soup(Files.club_2017_open_us_open_file)
    club_2017_womxns_us_open_soup = Make_Soup(Files.club_2017_womxns_us_open_file)
    club_2017_mixed_sf_invite_soup = Make_Soup(Files.club_2017_mixed_sf_invite_file)
    club_2017_open_sf_invite_soup = Make_Soup(Files.club_2017_open_sf_invite_file)
    club_2017_womxns_sf_invite_soup = Make_Soup(Files.club_2017_womxns_sf_invite_file)
    club_2017_mixed_es_challenge_soup = Make_Soup(Files.club_2017_mixed_es_challenge_file)
    club_2017_open_es_challenge_soup = Make_Soup(Files.club_2017_open_es_challenge_file)
    club_2017_womxns_es_challenge_soup = Make_Soup(Files.club_2017_womxns_es_challenge_file)
    club_2017_mixed_pro_championships_soup = Make_Soup(Files.club_2017_mixed_pro_championships_file)
    club_2017_open_pro_championships_soup = Make_Soup(Files.club_2017_open_pro_championships_file)
    club_2017_womxns_pro_championships_soup = Make_Soup(Files.club_2017_womxns_pro_championships_file)
    club_2017_mixed_nationals_soup = Make_Soup(Files.club_2017_mixed_nationals_file)
    club_2017_open_nationals_soup = Make_Soup(Files.club_2017_open_nationals_file)
    club_2017_womxns_nationals_soup = Make_Soup(Files.club_2017_womxns_nationals_file)
    club_2018_mixed_pe_challenge_soup = Make_Soup(Files.club_2018_mixed_pe_challenge_file)
    club_2018_open_pe_challenge_soup = Make_Soup(Files.club_2018_open_pe_challenge_file)
    club_2018_womxns_pe_challenge_soup = Make_Soup(Files.club_2018_womxns_pe_challenge_file)
    club_2018_mixed_sf_invite_soup = Make_Soup(Files.club_2018_mixed_sf_invite_file)
    club_2018_open_sf_invite_soup = Make_Soup(Files.club_2018_open_sf_invite_file)
    club_2018_womxns_sf_invite_soup = Make_Soup(Files.club_2018_womxns_sf_invite_file)
    club_2018_mixed_us_open_soup = Make_Soup(Files.club_2018_mixed_us_open_file)
    club_2018_open_us_open_soup = Make_Soup(Files.club_2018_open_us_open_file)
    club_2018_womxns_us_open_soup = Make_Soup(Files.club_2018_womxns_us_open_file)
    club_2018_mixed_es_challenge_soup = Make_Soup(Files.club_2018_mixed_es_challenge_file)
    club_2018_open_es_challenge_soup = Make_Soup(Files.club_2018_open_es_challenge_file)
    club_2018_womxns_es_challenge_soup = Make_Soup(Files.club_2018_womxns_es_challenge_file)
    club_2018_mixed_pro_championships_soup = Make_Soup(Files.club_2018_mixed_pro_championships_file)
    club_2018_open_pro_championships_soup = Make_Soup(Files.club_2018_open_pro_championships_file)
    club_2018_womxns_pro_championships_soup = Make_Soup(Files.club_2018_womxns_pro_championships_file)
    club_2018_mixed_nationals_soup = Make_Soup(Files.club_2018_mixed_nationals_file)
    club_2018_open_nationals_soup = Make_Soup(Files.club_2018_open_nationals_file)
    club_2018_womxns_nationals_soup = Make_Soup(Files.club_2018_womxns_nationals_file)
    club_2019_mixed_pe_challenge_soup = Make_Soup(Files.club_2019_mixed_pe_challenge_file)
    club_2019_open_pe_challenge_soup = Make_Soup(Files.club_2019_open_pe_challenge_file)
    club_2019_womxns_pe_challenge_soup = Make_Soup(Files.club_2019_womxns_pe_challenge_file)
    club_2019_mixed_sf_invite_oh_soup = Make_Soup(Files.club_2019_mixed_sf_invite_oh_file)
    club_2019_open_sf_invite_oh_soup = Make_Soup(Files.club_2019_open_sf_invite_oh_file)
    club_2019_womxns_sf_invite_oh_soup = Make_Soup(Files.club_2019_womxns_sf_invite_oh_file)
    club_2019_mixed_us_open_soup = Make_Soup(Files.club_2019_mixed_us_open_file)
    club_2019_open_us_open_soup = Make_Soup(Files.club_2019_open_us_open_file)
    club_2019_womxns_us_open_soup = Make_Soup(Files.club_2019_womxns_us_open_file)
    club_2019_mixed_es_challenge_soup = Make_Soup(Files.club_2019_mixed_es_challenge_file)
    club_2019_open_es_challenge_soup = Make_Soup(Files.club_2019_open_es_challenge_file)
    club_2019_womxns_es_challenge_soup = Make_Soup(Files.club_2019_womxns_es_challenge_file)
    club_2019_mixed_pro_championships_soup = Make_Soup(Files.club_2019_mixed_pro_championships_file)
    club_2019_open_pro_championships_soup = Make_Soup(Files.club_2019_open_pro_championships_file)
    club_2019_womxns_pro_championships_soup = Make_Soup(Files.club_2019_womxns_pro_championships_file)
    club_2019_mixed_nationals_soup = Make_Soup(Files.club_2019_mixed_nationals_file)
    club_2019_open_nationals_soup = Make_Soup(Files.club_2019_open_nationals_file)
    club_2019_womxns_nationals_soup = Make_Soup(Files.club_2019_womxns_nationals_file)

'''
1st prequarter, 1st quarter, 2nd quarter, 
1st semi, 2nd prequarter, 3rd quarter, 4th quarter, 2nd semi, finals
'''