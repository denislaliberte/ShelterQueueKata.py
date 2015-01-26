deactivate 
which python3
sudo rm -r p3
virtualenv --python=/usr/local/bin/python3 p3
source p3/bin/activate
pip install pytest
python3 -m pytest ShelterQueueKata_test.py
