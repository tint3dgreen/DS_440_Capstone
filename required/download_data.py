import requests
import os
#This is the base URl to access the API, every request wil start with this
base = "https://services.cancerimagingarchive.net/nbia-api/services/v1/"
#The UID is the unique identifier we neeed to access a collection
uid = "1.3.6.1.4.1.14519.5.2.1.9203.4007.255174310552142665714524147524"

url = "https://services.cancerimagingarchive.net/nbia-api/services/v1/getContentsByName?name=nbia-33941643745631058"

print(url)

r = requests.get(url)

json = r.json()
i = 1
for item in json:
	path = "/storage/home/cma5750/DS_440/DS_440_Capstone/volume/data/raw/Images/data"+str(i)+".zip"
	url = base + "getImage?SeriesInstanceUID=" + item["SeriesInstanceUID"]
	r = requests.get(url)
	with open(path, "wb") as fd:
		for chunk in r.iter_content(chunk_size=128):
			fd.write(chunk)
	print(item["SeriesInstanceUID"])
	exdir = "/storage/home/cma5750/DS_440/DS_440_Capstone/volume/data/raw/Images/"+str(i)+"/"
	os.system("unzip "+path+ " -d "+ exdir)
	i = i+1


