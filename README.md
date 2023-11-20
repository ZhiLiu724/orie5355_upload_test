# Upload test for ORIE 5355 project

This repo contains the files to automatically detect package version discrepancies in students' submissions. Make sure to update the `requirements.txt` file so that it is consistent with the versions on Google Colab.

The test proceeds by importing all the relevant packages, initializing a `gym` environment, and then running the submitted agent against a dummy agent for 200 time steps. It does not test for the runtime.

## Setting up the autograder

To set up an autograder that tests students' submissions, use the following setup command

`sudo git clone https://github.com/ZhiLiu724/orie5355_upload_test.git upload_test; sudo -H pip3 install -r upload_test/requirements.txt`

and the following run command

`python upload_test/test.py`
