print('-------Importing packages and environment-------')
import os
import numpy as np 
import sys
import matplotlib.pyplot as plt
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import make_env

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
folders = [f for f in folders if '_' not in f]
assert len(folders) == 1, "There should be only one folder in the agents directory, or that your team folder's name contains an underscore."
assert folders[0].lower() == team_name.lower(), "You should change the name of the folder to your actual team name."
if folders[0] != team_name:
    team_name = folders[0]
files = [f for f in os.listdir('./agents')]
assert f"{team_name}.py" in files, "You should have an agent file in the /agents folder with your team's actual name" 
print('Team name: {}, file structure correct, running test script'.format(team_name))


print('-------Testing agent-------')
project_part = part_name 
agentnames = [team_name, 'dummy_fixed_prices_adaptive']
if project_part == 1:
    env, agents = make_env.make_env_agents(agentnames = agentnames, project_part = project_part)
    
else:
    env, agents = make_env.make_env_agents(agentnames = agentnames, project_part = project_part
    , first_file = 'data/datafile1.csv', second_file='data/datafile2.csv')
print('Successfully initialized environment and agents.')


print('-------Testing agent by running 200 steps against dummy adaptive agent-------')
T = 200
env.reset()
customer_covariates, sale, profits = env.get_current_state_customer_to_send_agents()
last_customer_covariates = customer_covariates
cumulativetimes = [0 for _ in agents]

# fig, ax = plt.subplots(figsize=(20, 10))
for t in range(0, T):
    actions = []
    for enoutside, agent in enumerate(agents):
      ts = time.time()
      action = agent.action((customer_covariates, sale, profits))
      assert len(action) == project_part ## Have to give 1 price for each item. There is 1 item in part 1, 2 items in part 2
      curtime = time.time()
      cumulativetimes[enoutside] += curtime - ts
      actions.append(action)
    customer_covariates, sale, profits = env.step(actions)
    # newplot = env.render(True)
    # if newplot:
    #   display.clear_output(wait=True)
    #   display.display(plt.gcf())
    # print('last customer covariate: ', last_customer_covariates)
    # print('last (item bought, agent bought from, prices): ', sale)
    # print('current_profit per agent: ', profits)
    last_customer_covariates = customer_covariates
# plt.close()
# print("Cumulative buyer utility: {}".format(env.cumulative_buyer_utility))
# print("Average per-customer runtime agent 0 in seconds: {}".format(cumulativetimes[0]/T))
# print("Average per-customer runtime agent 1 in seconds: {}".format(cumulativetimes[1]/T))

print("Your Submission has passed!")
