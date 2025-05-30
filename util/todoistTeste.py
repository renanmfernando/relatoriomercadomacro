import todoist

token = 'c1a1f5a76f3cc03844bdbb27d414bcf56875a07a'
api = todoist.TodoistAPI(token)
api.sync()

for project in api.state['projects']:
    print(project['name'])


projects = [project.data for project in api.state['projects']] 

tasks = [task.data for task in api.state['items']]

for t in tasks:
    print(t['content'])