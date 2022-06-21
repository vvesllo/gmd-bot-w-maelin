import requests
from bs4 import BeautifulSoup

HEADERS = {
	"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 OPR/86.0.4363.70"
}

# DemonList
class DemonList:
	def __init__(self):
		self.url = "https://geometry-dash.fandom.com/ru/wiki/Топ_сложнейших_демонов_(версия_pointercrate)"
		responce = requests.get(self.url).text
		self.demon_list = self._parse(responce)
	
	# !!!!!!!!! НЕ ТРОЙГАЙ ЭТОТ МЕТОД !!!!!!!!!
	def _parse(self, text):
		soup = BeautifulSoup(text, 'html.parser')
		l = []
		for tr in soup.find("table", {"class": "wikitable"}).tbody.find_all("tr"):
			l.append(tr.find_all("td"))
		del l[0]
		final_l = []
		for i in l:
			final_l.append({
				"position": i[0].text[:-1], 
				"title": i[1].text[:-1],
				"creator": i[2].text[:-1],
				"verifer": i[3].text[:-1],
				"in-version": i[4].text[:-1]
			})
		return final_l


	def get_all_list(self):
		return self.demon_list # возвращает список со словарями

	def get_at_pos(self, index):
		return self.demon_list[index] # индексация начинается с 0


	def update(self):
		responce = requests.get(self.url).text
		return self._parse(responce)

# Get song data from from NG
class NewGrounds:
	global HEADERS
	def __init__(self):
		self.url = "https://www.newgrounds.com/audio/listen/"

	def get(self, id):
		responce = requests.get(self.url+str(id), headers=HEADERS).text
		self.data = self._parse(responce)
		return self.data

	def _parse(self, text):
		soup = BeautifulSoup(text, 'html.parser')
		"""
		TODO:
		title - V
		author - V
		length - V
		listens - V
		faves - V
		downloads - V
		votes - V
		score - V
		uploaded - V
		time - V
		genre - V
		size - x

		:))
		
		"""
		if soup.find(id='pageerror') is not None: # error
			return -1

		data = {
			"title": soup.find("title").text,
			"author": soup.find("a", {"class": "item-author"}).text.strip(),
			"length": soup.find_all("dl", {"class": "sidestats"})[1].find_all("dd")[-1].text.strip(),
			
			"listens": soup.find("dl", {"class": "sidestats"}).find("dd").text.strip(),
			"faves": soup.find("dl", {"class": "sidestats"}).find_all("dd")[1].text.strip(),
			"downloads": soup.find("dl", {"class": "sidestats"}).find_all("dd")[2].text.strip(),
			"votes": soup.find("dl", {"class": "sidestats"}).find_all("dd")[3].text.strip(),
			"score": soup.find("dl", {"class": "sidestats"}).find_all("dd")[4].text.strip(),

			"uploaded": soup.find_all("dl", {"class": "sidestats"})[1].find_all("dd")[0].text.strip(),
			"time": soup.find_all("dl", {"class": "sidestats"})[1].find_all("dd")[1].text.strip(),
			"size": soup.find_all("dl", {"class": "sidestats"})[1].find_all("dd")[4].text.strip(),
			"genre": soup.find_all("dl", {"class": "sidestats"})[2].find("dd").text.strip()
		}
		return data

