import requests
from bs4 import BeautifulSoup

url_link = "http://data.huffingtonpost.com/2016/jail-deaths"

response_text = requests.get(url_link).text

soup = BeautifulSoup(response_text, 'html.parser')

soup_prisoner = soup.findAll("div", {"class": "person-container"})

csv_file = open("result.csv","w+")
csv_file.write("\"Name\";\"Status\";\"Description\";\"Jail or Agency\";\"State\";\"Date arrested or booked\";\"Date of death\";\"Age at death\";\"Source\";\n")

for prisoner in soup_prisoner:
    #prisoner = soup_prisoner[0]
    name = prisoner.find("span",{"class":"name"}).text
    cause = prisoner.find("span", {"class":"cause-label"}).text

    info_list = prisoner.find("ul", {"class":"person-expanded"}).findAll("li")

    description = info_list[0].text

    jail = str(info_list[1].text)[16:]

    state = str(info_list[2].text)[7:]

    date_ar = str(info_list[3].text)[25:]

    date_death =  str(info_list[4].text)[15:]

    age_d = str(info_list[5].text)[14:]

    source = ""
    if info_list[6].find("a"):
        source = str(info_list[6].find("a")['href'])

    csv_file.write("\""+name+"\";\""+cause+"\";\""+description+"\";\""+jail+"\";\""+state+"\";\""+date_ar+"\";\""+date_death+"\";\""+age_d+"\";\""+source+"\"\n")
