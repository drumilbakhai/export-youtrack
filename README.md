# export-youtrack
This repository contains a python script that scrapes all the youtrack issues using Youtrack Export API call

To execute this script it is necessary to have authorization token. Therefore refer Youtrack's Login Information.
https://www.jetbrains.com/help/youtrack/standalone/Log-in-to-YouTrack.html#dev-Permanent-Token

Store the newly generated token on a new local file named "my_token" in a following format
Bearer perm:token_goes_here

Execute the script export-issue and it will ask for project name.
Enter the project name and sit back for few minutes till it creates a new csv file which contains Issue id and comments
