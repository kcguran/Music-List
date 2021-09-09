import requests
from bs4 import BeautifulSoup

class SlowTurk:
    url = "https://www.slowturk.com.tr/top-20"
    html = requests.get(url).content
    soup = BeautifulSoup(html,'html.parser')
    totalListName = []
    def liste(self):
        self.list = self.soup.find_all("div",{"class" : "desc-author"})
        for self.isim in self.list:
            self.link = self.isim.get_text("class")
            self.totalListName.append(self.link)
        return self.totalListName
    
    def save(self,totalListName):
        self.totalListName = totalListName
        with open("slowTurk.txt", "w",encoding="UTF-8") as file:
            for item in self.totalListName:
                file.write(item + "\n")
        

class Fenomen:
    url = "https://www.radyofenomen.com/listeler_ilk10.html"
    html = requests.get(url).content
    soup = BeautifulSoup(html,'html.parser')
    totalList = []
    def liste(self):
        self.list = self.soup.find_all("div",{"data-format-name" : "Single"})
        for self.isim in self.list:
            self.link = self.isim.get("data-song-title")
            self.totalList.append(self.link)
        return self.totalList

    def save(self,totalList):
        self.totalList = totalList
        with open("Fenomen.txt", "w", encoding="UTF-8") as file:
            for item in self.totalList:
                file.write(item + "\n")
        

class NumberOneFM:
    url = "https://www.numberone.com.tr/muzik/number-one-top-20/"
    html = requests.get(url).content
    soup = BeautifulSoup(html,'html.parser')
    totalList = []
    def liste(self):
        self.list1 = self.soup.find("div",{"id" : "description first"})
        self.link1 = self.list1.h2.a.get("title")
        self.list2 = self.soup.find_all("div",{"id" : "description"})
        for self.isim in self.list2:
            self.link2 = self.isim.h2.a.get("title")
            self.totalList.append(self.link2)
        return self.totalList

    def save(self,totalList):
        self.totalList = totalList
        with open("NumberOneFM.txt", "w", encoding="UTF-8") as file:
            for item in self.totalList:
                file.write(item + "\n")


class MetroFM:
    url = "https://metrofm.com.tr/"
    html = requests.get(url).content
    soup = BeautifulSoup(html,'html.parser')
    totalList = []
    def liste(self):
        self.list = self.soup.find_all("strong",{"class" : "song_title"})
        songTitle=[]
        artistName=[]

        for self.isim in self.list:
            self.link = self.isim.get_text("class")
            songTitle.append(self.link)
        self.list2 = self.soup.find_all("strong",{"artist_name"})
        
        for self.isim2 in self.list2:
            self.link2 = self.isim2.get_text("class")
            artistName.append(self.link2)

        for i in range(12,52):
            self.topList = (artistName[i] +" "+  songTitle[i])
            self.totalList.append(self.topList)

        return self.totalList

    def save(self,totalList):
        self.totalList = totalList
        with open("MetroFm.txt", "w", encoding="UTF-8") as file:
            for item in self.totalList:
                file.write(item + "\n")
            

slowTurk = SlowTurk()
numberOne = NumberOneFM()
metroFm = MetroFM()
fenomen = Fenomen()
numberOneTotalList = numberOne.liste()
fenomenTotalList = fenomen.liste()
metroTotalList = metroFm.liste()
slowTurkTotalList = slowTurk.liste()
print(f'Fenomen Top List : {fenomen.save(fenomenTotalList)}')
print(f'NumberOneFM Top List : {numberOne.save(numberOneTotalList)}')
print(f'MetroFM Top List : {metroFm.save(metroTotalList)}')
print(f'SlowTurk Top Lİst :{slowTurk.save(slowTurkTotalList)}')
