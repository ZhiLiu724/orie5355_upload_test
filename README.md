# Upload test for ORIE 5355 project part I

This repo contains the files to automatically detect package version discrepancies in students' submissions. Make sure to update the `requirements.txt` file so that it is consistent with the versions on Google Colab.

The test proceeds by importing all the relevant packages, initializing a `gym` environment, and then running the submitted agent against a dummy agent for 20 time steps. It does not test for the runtime.
