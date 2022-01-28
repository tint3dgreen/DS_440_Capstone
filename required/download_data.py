import requests

base = "https://services.cancerimagingarchive.net/nbia-api/services/v1/"
uid = "1.3.6.1.4.1.14519.5.2.1.9203.4007.255174310552142665714524147524"

url = base +"getImage?SeriesInstanceUID="+uid

print(url)

r = requests.get(url)

with open("data.zip", "wb") as fd:
	for chunk in r.iter_content(chunk_size=128):
		fd.write(chunk)
