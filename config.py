import os

# DVWA application config
DVWA_USER_NAME = os.environ.get('DVWA_USERNAME')
DVWA_PASSWORD = os.environ.get('DVWA_PASSWORD')
DVWA_BASE_URL = os.environ.get('DVWA_BASE_URL', 'http://192.168.0.27/')

# Misc helpers
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))


