#NAME: 	HTMLPARSER			#
#EDITORS: ROYAL STEWART			#
#	  VINH LE			#

from bs4 import BeautifulSoup
import requests
import json
import urllib2

# Create a URL variable that accepts the URL of the EDAC Database
url = "http://gstore.unm.edu/apps/rgis/search/datasets.kml?offset=0&sort=lastupdate&dir=desc&limit=02&theme=Digital+Orthophotography&subtheme=2013+USFS+Resource+Photography"

# Request the HTML document
html_doc = requests.get(url)

# Create a BeautifulSoup data type and run the HMTL document through the BS constructor
soup = BeautifulSoup(html_doc.text)

# Acquire the data types from the BS data type
names = soup.find_all("name")
whens = soup.find_all("when")
coords = soup.find_all("coordinates")

# Assign values to single array for easy access
watershed = [names, whens, coords]

print watershed
