import requests
from bs4 import BeautifulSoup

class Fenomen:
    url = "https://www.radyofenomen.com/listeler_ilk10.html"
    html = requests.get(url).content
    soup = BeautifulSoup(html,'html.parser')
    list = soup.find_all("div",{"data-format-name" : "Single"})
    for isim in list:
        link = isim.get("data-song-title")

class NumberOneFM:
    url = "https://www.numberone.com.tr/muzik/number-one-top-20/"
    html = requests.get(url).content
    soup = BeautifulSoup(html,'html.parser')
    list1 = soup.find("div",{"id" : "description first"})
    link1 = list1.h2.a.get("title")
    list2 = soup.find_all("div",{"id" : "description"})
    for isim in list2:
        link2 = isim.h2.a.get("title")


class MetroFM:
    url = "https://metrofm.com.tr/"
    html = requests.get(url).content
    soup = BeautifulSoup(html,'html.parser')
    list = soup.find_all("strong",{"class" : "song_title"})
    songTitle=[]
    artistName=[]

    for isim in list:
        link = isim.get_text("class")
        songTitle.append(link)


    list2 = soup.find_all("strong",{"artist_name"})
    for isim2 in list2:
        link2 = isim2.get_text("class")
        artistName.append(link2)

    for i in range(12,52):
        kerem = (artistName[i] +" "+  songTitle[i])
        