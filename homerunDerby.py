from time import sleep  #program script to sleep
import urllib.request   #to open URLs
import os
from datetime import datetime

from bs4 import BeautifulSoup
#import numpy as np
#import matplotlib.pyplot as plt
#import pandas as pd

masterScoreTracker = {}

contestantName = ['Aki Komatsu', 'Player 2', 'Player 3', 'Player 4', 'Player 5',
                 'Player 6', 'Player 7', 'Player 8', 'Player 9', 'Player 10',
                  'Player 11', 'Player 12', 'Player 13', 'Player 14', 'Player 15']


contestantPicks = [
    ['https://www.mlb.com/player/j-d-martinez-502110',
    'https://www.mlb.com/player/christian-yelich-592885',
    'https://www.mlb.com/player/edwin-encarnacion-429665',
    'https://www.mlb.com/player/cody-bellinger-641355',
    'https://www.mlb.com/player/aaron-judge-592450',
    'https://www.mlb.com/player/anthony-rizzo-519203'], 
                  
    ['https://www.mlb.com/player/khris-davis-501981',
    'https://www.mlb.com/player/rhys-hoskins-656555',
    'https://www.mlb.com/player/edwin-encarnacion-429665',
    'https://www.mlb.com/player/aaron-judge-592450',
    'https://www.mlb.com/player/cody-bellinger-641355',
    'https://www.mlb.com/player/ronald-acuna-jr-660670'],
    
    ['https://www.mlb.com/player/khris-davis-501981',
    'https://www.mlb.com/player/rhys-hoskins-656555',
    'https://www.mlb.com/player/alex-bregman-608324',
    'https://www.mlb.com/player/aaron-judge-592450',
    'https://www.mlb.com/player/kris-bryant-592178',
    'https://www.mlb.com/player/matt-chapman-656305'],

    ['https://www.mlb.com/player/khris-davis-501981',
    'https://www.mlb.com/player/trevor-story-596115',
    'https://www.mlb.com/player/edwin-encarnacion-429665',
    'https://www.mlb.com/player/aaron-judge-592450',
    'https://www.mlb.com/player/cody-bellinger-641355',
    'https://www.mlb.com/player/mike-moustakas-519058'],

    ['https://www.mlb.com/player/nolan-arenado-571448',
    'https://www.mlb.com/player/javier-baez-595879',
    'https://www.mlb.com/player/mookie-betts-605141',
    'https://www.mlb.com/player/aaron-judge-592450',
    'https://www.mlb.com/player/joc-pederson-592626',
    'https://www.mlb.com/player/mike-moustakas-519058'],

    ['https://www.mlb.com/player/nolan-arenado-571448',
    'https://www.mlb.com/player/paul-goldschmidt-502671',
    'https://www.mlb.com/player/mookie-betts-605141',
    'https://www.mlb.com/player/cody-bellinger-641355',
    'https://www.mlb.com/player/aaron-judge-592450',
    'https://www.mlb.com/player/mike-moustakas-519058'],

    ['https://www.mlb.com/player/j-d-martinez-502110',
    'https://www.mlb.com/player/rhys-hoskins-656555',
    'https://www.mlb.com/player/charlie-blackmon-453568',
    'https://www.mlb.com/player/aaron-judge-592450',
    'https://www.mlb.com/player/luke-voit-572228',
    'https://www.mlb.com/player/mike-moustakas-519058'],

    ['https://www.mlb.com/player/giancarlo-stanton-519317',
    'https://www.mlb.com/player/rhys-hoskins-656555',
    'https://www.mlb.com/player/alex-bregman-608324',
    'https://www.mlb.com/player/aaron-judge-592450',
    'https://www.mlb.com/player/cody-bellinger-641355',
    'https://www.mlb.com/player/ronald-acuna-jr-660670'],
    
    ['https://www.mlb.com/player/mike-trout-545361',
    'https://www.mlb.com/player/bryce-harper-547180',
    'https://www.mlb.com/player/edwin-encarnacion-429665',
    'https://www.mlb.com/player/aaron-judge-592450',
    'https://www.mlb.com/player/cody-bellinger-641355',
    'https://www.mlb.com/player/randal-grichuk-545341'],
    
    ['https://www.mlb.com/player/giancarlo-stanton-519317',
    'https://www.mlb.com/player/bryce-harper-547180',
    'https://www.mlb.com/player/alex-bregman-608324',
    'https://www.mlb.com/player/aaron-judge-592450',
    'https://www.mlb.com/player/cody-bellinger-641355',
    'https://www.mlb.com/player/anthony-rizzo-519203'], 

    ['https://www.mlb.com/player/giancarlo-stanton-519317',
    'https://www.mlb.com/player/matt-carpenter-572761',
    'https://www.mlb.com/player/mookie-betts-605141',
    'https://www.mlb.com/player/aaron-judge-592450',
    'https://www.mlb.com/player/anthony-rizzo-519203',      
    'https://www.mlb.com/player/matt-chapman-656305'],
     
    ['https://www.mlb.com/player/giancarlo-stanton-519317',
    'https://www.mlb.com/player/bryce-harper-547180',
    'https://www.mlb.com/player/mookie-betts-605141',
    'https://www.mlb.com/player/aaron-judge-592450',
    'https://www.mlb.com/player/cody-bellinger-641355',
    'https://www.mlb.com/player/randal-grichuk-545341'],

    ['https://www.mlb.com/player/j-d-martinez-502110',
    'https://www.mlb.com/player/bryce-harper-547180',
    'https://www.mlb.com/player/alex-bregman-608324',
    'https://www.mlb.com/player/aaron-judge-592450',
    'https://www.mlb.com/player/gary-sanchez-596142',
    'https://www.mlb.com/player/ronald-acuna-jr-660670'],
    
    ['https://www.mlb.com/player/j-d-martinez-502110',
    'https://www.mlb.com/player/bryce-harper-547180',
    'https://www.mlb.com/player/alex-bregman-608324',
    'https://www.mlb.com/player/aaron-judge-592450',
    'https://www.mlb.com/player/kyle-schwarber-656941',
    'https://www.mlb.com/player/anthony-rizzo-519203'],
    
    ['https://www.mlb.com/player/giancarlo-stanton-519317',
    'https://www.mlb.com/player/bryce-harper-547180',
    'https://www.mlb.com/player/charlie-blackmon-453568',
    'https://www.mlb.com/player/aaron-judge-592450',
    'https://www.mlb.com/player/mike-moustakas-519058',
    'https://www.mlb.com/player/ronald-acuna-jr-660670']]

def getHomerunCount(soup):
    
    table = soup.find_all('table')[0]
    #print ('Retreiving Homerun Count...')
    
    #headers = table.find_all('tr')
    #for row in rows:
        #cols=row.find_all('th')
        #cols=[x.text.strip() for x in cols]
        #print (cols)

    rows = table.find_all('tr')
    cols = 0
    for row in rows:
        cols=row.find_all('td')
        cols=[x.text.strip() for x in cols]
        #print (cols)
    HR_Count = int((cols[2]))
    print ("Homerun Count: " + str(HR_Count))
    homerunList.append(HR_Count)


def getContestantTotal(name, cList):
    for i in range(len(cList)):
        playerpage = urllib.request.urlopen(cList[i])
        print ("Retreiving Player " + cList[i] + "...")
        
        # parse the html using beautiful soup and store in variable 'soup'
        playersoup = BeautifulSoup(playerpage, 'html.parser')
        
        getHomerunCount(playersoup)
    
    total = sum(homerunList)
    print ('Printing Total For: ' + name)
    print (total)
    
    masterScoreTracker[name]= total


for i in range(len(contestantName)):
    homerunList = []
    getContestantTotal(contestantName[i], contestantPicks[i])


def outputStandings(masterScoreTracker):
    currentDT = datetime.now()
    print ('Standings as of: ' + currentDT.strftime("%a, %b %d, %Y %I:%M:%S %p"))
    for name, total in masterScoreTracker.items():
        print('{}: {}'.format(name, total))
        
outputStandings(masterScoreTracker)
