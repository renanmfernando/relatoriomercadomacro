from googleapiclient.discovery import build
service = build('tasks', 'v1')

minhasTasks = service.tasks().list(tasklist='@default').execute()


# First retrieve the task to update.
task = service.tasks().get(tasklist='@default', task='taskID').execute()
task['status'] = 'completed'

result = service.tasks().update(tasklist='@default', task=task['id'], body=task).execute()
# Print the completed date.
print(result['completed'])