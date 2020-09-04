from bs4 import BeautifulSoup


class SourceFileSoupParser:
    def __init__(self, file):
        self.file = file
        self.soup = BeautifulSoup(self.read_file(), 'html.parser')

    def read_file(self):
        file = open(self.file)
        data = file.read()
        file.close()
        return data

    def event_name(self):
        tournament = self.soup.find('h1').text.split()
        tournament = tournament[:tournament.index('-')]
        tournament = ' '.join(tournament)
        return tournament

    def event_date(self):
        raw_date = self.soup.find('h2').text.split()
        return raw_date

    def event_year(self):
        event_year = self.event_date()[-1]
        return event_year

    def event_division(self):
        division_raw = self.soup.findAll("span", "mat-button-wrapper")[-1].text.split()[1]
        return division_raw

    def pools(self):
        pools = self.soup.find_all('app-schedule-pool')
        return pools

    def brackets(self):
        brackets = self.soup.find_all('app-schedule-bracket')
        return brackets
