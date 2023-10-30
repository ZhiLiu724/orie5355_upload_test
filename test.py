import os

if ___name___ == "__main__":
    print('-------Getting team names-------')
    folders = [f for f in os.listdir('../agents') if not os.path.isfile(os.path.join('../agents', f))]
    folders = [f for f in folders if '_' not in f]
    assert len(folders) == 1, "There should be only one folder in the agents directory, or that your team name contains an underscore."

    print("Hello World!")