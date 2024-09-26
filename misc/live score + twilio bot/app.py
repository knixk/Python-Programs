import requests
import os
from flask import Flask, request
from dateutil import parser, tz
from twilio.twiml.messaging_response import MessagingResponse

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

html = requests.get(urls['teams']).json()
html = html['groups'][0]
html = html['teams']

# print(html)
print('\n')
print("Data starts here... ")
print("Teams in GROUP A:")

def printSep():
    print('\n')
    print('==========================================')
    print('\n')


# main code
for data in html:
    printSep()
    print("name: ", data['name'])
    print("wins: ", data['wins'])
    print("losses: ", data['losses'])
    print("games_played: ", data['games_played'])

print('==========================================')



# for match in html:
    # for data in match['teams']:
        # print(data) 
    # print(match)
# 