import requests
import pprint
import json
pp = pprint.PrettyPrinter()
#
url_github = 'https://api.github.com/'

user_github = requests.get(url_github + 'users/jhonatanmsc')
print('- Get usuario -')
pp.pprint(user_github.json())

user_github = requests.get(url_github + 'users/dann95')
print('\n- Get usuario -')
pp.pprint(user_github.json())

user = 'jhonatanmsc',
token = 'arrume uma token'

repo = {
	'name': 'new-teste',
	'description': 'New teste code',
	'auto_init': 'true'
}

#create a new repo
m_usergit = requests.post(url_github+'user/repos', auth=(user, token), data=json.dumps(repo))
print('- Post new repo -')
pp.pprint(m_usergit.json())
