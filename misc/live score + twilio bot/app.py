urls = {
    'group': 'https://worldcup.sfg.io/teams/group_results',
    'country': 'https://worldcup.sfg.io/matches/country?fifa_code=',
    'today': 'https://worldcup.sfg.io/matches/today',
    'tomorrow': 'https://worldcup.sfg.io/matches/tomorrow',
    'teams': 'https://worldcupjson.net/teams'
}

countries = ['KOR', 'PAN', 'MEX', 'ENG', 'COL', 'JPN', 'POL', 'SEN',
'RUS', 'EGY', 'POR', 'MAR', 'URU', 'KSA', 'IRN', 'ESP',
'DEN', 'AUS', 'FRA', 'PER', 'ARG', 'CRO', 'BRA', 'CRC',
'NGA', 'ISL', 'SRB', 'SUI', 'BEL', 'TUN', 'GER', 'SWE']

import requests
html = requests.get(urls['teams']).json()
html = html['groups']

for match in html:
    print(match['letter'])
