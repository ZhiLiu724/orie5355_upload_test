print('-------Importing packages and environment-------')
import os
import numpy as np 
import pandas as pd
import sys
import matplotlib.pyplot as plt
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import make_env_2024 as make_env

print('-------Getting team names-------')
current_script_path = os.path.abspath(__file__)
repo_name = os.path.basename(os.path.dirname(os.path.dirname(current_script_path)))
part_and_team_name = repo_name.split('part-')[1]
part_name = int(part_and_team_name.split('-', 1)[0])
team_name = part_and_team_name.split('-', 1)[1]
print('Your team name according to the repository name should be: ', team_name)
print('This is submission for project part: ', part_name)

print('-------Checking if file structure is correct-------')
folders = [f for f in os.listdir('./agents') if not os.path.isfile(os.path.join('./agents', f))]
folders = [f for f in folders if '__pycache__' not in f]
assert len(folders) == 1, "There should be only one folder in the agents directory, or that your team folder's name contains an underscore."
assert folders[0].lower() == team_name.lower(), "You should change the name of the folder to your actual team name."
if folders[0] != team_name:
    print('Actual team name contains upper case letters, converting...')
    team_name = folders[0]
files = [f for f in os.listdir('./agents')]
assert f"{team_name}.py" in files, "You should have an agent file in the /agents folder with your team's actual name" 

### delete all files except the agent file and the static prices file
files.remove(f"{team_name}.py")
files.remove('__init__.py')
files = [f for f in files if f != 'static_prices_submission.csv']
for f in files:
    # only remove non-folder files
    if os.path.isfile(os.path.join('./agents', f)):
        os.remove(os.path.join('./agents', f))

    
print('Team name: {}, file structure correct, running test script'.format(team_name))


print('-------Testing agent-------')
project_part = part_name 
if project_part == 1:
    agentnames = [team_name]
else:
    agentnames = [team_name, 'dummy_fixed_prices_adaptive']
env, agents = make_env.make_env_agents(
    agentnames = agentnames, 
    project_part = project_part, 
    first_file = 'data/datafile1_2024.csv', 
    second_file='data/datafile2_2024.csv'
    )
print('Successfully initialized environment and agents.')


print('-------Testing agent by running 200 steps-------')
T = 200

env.reset()
customer_covariates, sale, profits, inventories, time_until_replenish = env.get_current_state_customer_to_send_agents()
last_customer_covariates = customer_covariates
cumulativetimes = [0 for _ in agents]
n_errors = [0 for _ in agents]

fig, ax = plt.subplots(figsize=(20, 10))
for t in range(0, T):
    actions = []
    for id, agent in enumerate(agents):
        start = time.time()
        action = agent.action((customer_covariates, sale, profits, inventories, time_until_replenish))
        cumulativetimes[id] += time.time() - start
        if action < 0:
            n_errors[id] += 1
        actions.append(action)
    customer_covariates, sale, profits, inventories, time_until_replenish = env.step(actions)
    last_customer_covariates = customer_covariates

plt.close()
print("Cumulative profit: {}".format(env.agent_profits))
print("Cumulative buyer utility: {}".format(env.cumulative_buyer_utility))

print("Average per-customer runtime for your agent in seconds: {}".format(cumulativetimes[0]/T))
print("Number of rounds your agent output invalid prices: {}".format(n_errors[0]))


pricesfilename = 'static_prices_submission.csv'
assert f'{pricesfilename}' in files, "You have not submitted the static prices file"
static_prices_df = pd.read_csv(f'./agents/{pricesfilename}')
assert set(static_prices_df.columns) == set(['user_index', 'price_item', 'expected_revenue']), "Your submitted static prices file has wrong columns"
print('Your static prices file is submitted and the columns are correct')

print('-------ALL TESTS COMPLETED-------')
print("Your Submission has passed!")