#NAME: 	  XMLPARSER			#
#EDITORS: ROYAL STEWART			#
#	  VINH LE			#

from lxml import etree
import xml.etree.ElementTree as ET
from io import StringIO, BytesIO
import requests
import urllib2

url = "http://gstore.unm.edu/apps/rgis/search/datasets.kml?offset=0&sort=lastupdate&dir=desc&limit=3&theme=Digital+Orthophotography&subtheme=2013+USFS+Resource+Photography"

#xml = requests.get(url)

tree = ET.parse('test.xml')
root = tree.getroot()

# Grab Name
name = root[0][0][2][0].text
print("Name: " + name)

# Grab ID
ident = root[0][0][2].get('id')
print("ID: " + ident)

# Grab Date
date = root[0][0][2][1][0].text
print("Date: " + date)

# Grab Coordinates
coords = root[0][0][2][2][0][0][0].text
print("Coordinates: " + coords)

# Grab Service JSON
service = root[0][0][2][3][0][1].text

# Set Data in one array
data = [name, ident, date, coords]

