import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest
import os 

job_title = []
company_name = []
locations_name = []
job_skill = []
links = []
job_req = []
date_posted = []

def main(soup):
    job_titles = soup.find_all("h2",{'class':'css-m604qf'})
    company_names = soup.find_all("a",{'class':'css-17s97q8'})
    locations_names = soup.find_all("span",{'class':'css-5wys0k'})
    job_skills = soup.find_all("div",{'class':'css-y4udm8'})
    posted_old = soup.find_all('div',{'class':'css-do6t5g'})
    posted_new = soup.find_all('div',{'class':'css-4c4ojb'})
    posted = [*posted_new,*posted_old]
    
    for i in range(len(job_titles)):
        job_title.append(job_titles[i].text)
        links.append(job_titles[i].find('a').attrs['href'])
        company_name.append(company_names[i].text)
        locations_name.append(locations_names[i].text)
        job_skill.append(job_skills[i].text)
        date_posted.append(posted[i].text.strip())

    for link in links:
        headers = {'User-Agent': 'Mozilla/5.0'}
        job_data = requests.get(link,headers=headers)
        src = job_data.content
        newsoup = BeautifulSoup(src,"lxml")
        try:
            job_req.append(newsoup.find('div',{'class':'css-1t5f0fr'}).text.strip())
        except Exception as e:
            print(f"Error : {e}")
        # print(link)
        # print(newsoup.find('div',{'class':'css-1t5f0fr'}).ul)

    keys = ['job_title','company_name','date_posted','locations_name','job_skill','link','job_req']

    with open(os.path.join(os.getcwd()+'/jobs-details.csv'),'w',encoding='utf-8') as output_file:
        wr = csv.writer(output_file)
        wr.writerow(keys)
        # for i in range(len(job_title)):
        #     wr.writerow([job_title[i],company_name[i],locations_name[i],job_skill[i]])
        
        wr.writerows(zip_longest(*[job_title,company_name,date_posted,locations_name,job_skill,links,job_req]))

page_num = 0
page_limit = 0
while True:
   
   data = requests.get(f"https://wuzzuf.net/search/jobs/?a=hpb&q=embedded&start={page_num}")
   src = data.content

   soup = BeautifulSoup(src,"lxml") 
   if page_limit == 0:
       page_limit = int(soup.find('strong').text.strip())//15
   main(soup)
   page_num+=1
   if page_num > page_limit:
       break

