import os


print('-------Getting team names-------')
folders = [f for f in os.listdir('./agents') if not os.path.isfile(os.path.join('./agents', f))]
folders = [f for f in folders if '_' not in f]
assert len(folders) == 1, "There should be only one folder in the agents directory, or that your team name contains an underscore."
team_name = folders[0]
print('Team name: {}, running test script'.format(team_name))

print("Hello World!")