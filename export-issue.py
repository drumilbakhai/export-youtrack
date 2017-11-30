import requests
file_obj = open('my_token', 'r')
token = file_obj.read()
headers = {'Authorization': token}
r = requests.get('https://nyuwp.myjetbrains.com/youtrack/rest/issue/WP-851/attachment', headers = headers)
print(r)