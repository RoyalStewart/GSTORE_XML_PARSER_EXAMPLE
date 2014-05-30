import requests
import json

# Headers
headers = {'content-type' : 'application/json'}

# Create URL object
url = 'http://134.197.42.46:5000/todo/api/v1.0/sample'

# Create data value object
payload = {
		'title': 'Gurrhurrdurrs Odyssey!',
		'description': u'Gurrhurrdurr tries to go to the store for some milk, on the way, hilarity ensues',
	}

# Create files object
files = {'title': 'Read a Book'}

# Post data to url (original)
#r = requests.post(url, data=payload, headers=headers)

# Post data to url (new)
#r = requests.post(url, data=json.dumps(payload), headers=headers)

# Get data from url
#r = requests.get(url)

# Delete data from url
#r = requests.delete(url)

# Check response
print r.text

# Check for "ok" status code
print r.status_code == requests.codes.ok
