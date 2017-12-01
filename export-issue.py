import requests
from xml.etree import ElementTree as etree

def getIds(token,project,max_issues,):
    all_ids = []
    API = "https://nyuwp.myjetbrains.com/youtrack/rest/issue/byproject/"+project+"?max="+str(max_issues)
    print(API)
    headers = {'Authorization': token}
    r = requests.get(API, headers = headers)
    tree = etree.fromstring(r.content)

    for child in tree:
        # print(child.tag, child.attrib['id'])
        all_ids.append(child.attrib['id'])

    return all_ids

def getCommentsForAnIssue(token, issue_id):
    API = "https://nyuwp.myjetbrains.com/youtrack/rest/issue/"+issue_id+"/comment"
    headers = {'Authorization': token}
    r = requests.get(API,headers = headers)
    tree = etree.fromstring(r.content)
    comment_arr = []
    for child in tree:
        print(child.attrib['text'])
        comment_arr.append(child.attrib['text'])


file_obj = open('my_token', 'r')
token = file_obj.read()

#print(getIds(token,'AUTOMATION',700,))
print(getCommentsForAnIssue(token,'WP-553'))


