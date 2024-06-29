import requests
from bs4 import BeautifulSoup
import csv
import os

date = input("Please enter in a date in the folllowing format MM/DD/YY : ")
# date = "7/7/2024"
page = requests.get(f"https://www.yallakora.com/match-center/?date={date}")

matchs_details = []
def main(page):
    #get content of page
    src = page.content

    #parse the content
    soup = BeautifulSoup(src,"lxml")
    
    championships = soup.find_all("div",{'class':'matchCard'})
    
    def get_match_info(championship):
        championship_title = championship.contents[1].find('h2').text.strip()
        all_matches = championship.contents[3].find_all("div",{'class':'liItem'})
        number_of_matches = len(all_matches)

        for i in range(number_of_matches):
            #get teams names
            team_A = all_matches[i].find("div",{'class':'teams teamA'}).find('p').text.strip()
            team_B = all_matches[i].find("div",{'class':'teams teamB'}).find('p').text.strip()
        
            #get score
            match_result = all_matches[i].find("div",{'class':'MResult'}).find_all('span',{'class':'score'})
            score = f"{match_result[0].text.strip()} - {match_result[1].text.strip()}"
            
            #get match time
            match_time = all_matches[i].find("div",{'class':'MResult'}).find('span',{'class':'time'}).text.strip()

            #add match info to matches_details
            matchs_details.append({"ChampionType" : championship_title,
                                  "TeamA" : team_A,
                                  "TeamB" : team_B,
                                  "MatchTime" : match_time,
                                  "Score" : score
                                  })

    for i in range(len(championships)):
        get_match_info(championships[i])

    keys = matchs_details[0].keys()

    with open(os.path.join(os.getcwd()+'/matches-details.csv'),'w',encoding='utf-8') as output_file:
        dict_writer = csv.DictWriter(output_file,keys)
        dict_writer.writeheader()
        dict_writer.writerows(matchs_details)

        print("check the file created")

main(page)