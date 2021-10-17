# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from jira import JIRA

loginJira = ''
passJira = ''
tokenJira = ''

def initJira():
    jira_options = {'server': 'https://open-genes.atlassian.net'}
    return JIRA(options=jira_options, basic_auth=(loginJira, tokenJira))

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, i am {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('jiraPy')

    jira = initJira()
    project_key = 'OG'
    work_date = '20211001'
    reporter = '70121:3bf008e2-6e0d-4025-9572-24942d2fee45'
    jql = 'project = ' + project_key + ' AND  worklogDate >= ' + work_date + ' AND  reporter = ' + reporter
    issues_list = jira.search_issues(jql)

    print(issues_list)
    print(issues_list.total)
    for issue in issues_list:
        print("{0}".format(issue.key))
        worklogs = jira.worklogs(issue.key)
        print(worklogs)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
