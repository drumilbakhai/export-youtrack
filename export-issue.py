import requests
import csv
from xml.etree import ElementTree as etree

def writeToCSVFile(filename, comments):
    # Simply Appending the Issue Id and the comments in a csv file
    """
    A simple method to write data to the CSV file
    :param filename: The name of the file where the data will be stored or written
    :param comments: The list of comments pertaining to a single issue
    """
    with open(filename, 'a') as csvfile:
        writer = csv.writer(csvfile, dialect='excel')
        writer.writerow(comments)


def getIds(token,project,max_issues):
    """
    Method that retrieves the list of all the Issues along with Issue ID in the project
    :param token: Token for Authorization. Token is read from a file
    :param project: The name of the project for which the issue ids will be fetched.
    :param max_issues: An upper limit to retrieve the number of issues.
    :return:
    """
    all_ids = []
    # Preparing URL for getting list of ids for a given project
    API = "https://nyuwp.myjetbrains.com/youtrack/rest/issue/byproject/"+project+"?max="+str(max_issues)
    headers = {'Authorization': token}
    print(API)

    # Sending request
    r = requests.get(API, headers = headers)
    print(r.content)

    data = etree.fromstring(r.content)

    for child in data:
        issue_details = []
        print("Title ", child[2][0].text)
        print("Issue Description ", child[3][0].text, "and type is ",type(child[3][0].text))
        issue_details.append(child.attrib['id'])

        issue_details.append(child[2][0].text)
        issue_description = child[3][0].text
        if issue_description[0].isdigit():
            print("No Project Description for ",child.attrib['id'])
            issue_details.append("No Project Description")
        else:
            issue_details.append(issue_description)

        all_ids.append(issue_details)
    #print(all_ids)
    return all_ids


def getCommentsForAnIssue(token, issue_id):
    """
    A sample method to retrieve the list of comments based on the issue id
    :param token: Token for Authorization. Token is read from a file
    :param issue_id: Issue id for which the comments will be retrieved
    :return: Return the list of comments made on a issue
    """
    comment_arr = []
    #comment_arr.insert(0, issue_id)

    # Preparing URL for getting all the comments for a given issue
    API = "https://nyuwp.myjetbrains.com/youtrack/rest/issue/"+issue_id+"/comment"
    headers = {'Authorization': token}

    # Sending Request
    r = requests.get(API,headers = headers)

    # Getting the data back in XML Format
    tree = etree.fromstring(r.content)

    for child in tree:
        # Formating the output to display the name of user who commented.
        line = child.attrib['author'] +' commented ==> '+ child.attrib['text'] + '\n'
        comment_arr.append(line)

    return comment_arr

# Reading Authorization Token
file_obj = open('my_token', 'r')
token = file_obj.read()

# Input the project
wp_project = input()
filename = wp_project + '.csv'
max_issues = 1000

# Get the list of all Issue id for a project
list_ids = getIds(token,wp_project,max_issues)

# Iterate over each issue id, retrieve the comments for that issue and append the comments to csv file
for each_id in list_ids:
     issue_data = []
     issue_data.append(each_id[0])
     issue_data.append(each_id[1])
     issue_data.append(each_id[2])
     comments_list = getCommentsForAnIssue(token,each_id[0])
     comment_data = " ".join(comments_list)
     issue_data.append(comment_data)
     # print(issue_data)
     writeToCSVFile(filename,issue_data)

