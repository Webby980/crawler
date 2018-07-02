""" This module constitutes as the single point of configuration for the application and pulls
the necessary environment variables required to run th=e application. Such as secrets. """
import os
DVWA_USER_NAME = os.environ.get('DVWA_USERNAME')
DVWA_PASSWORD = os.environ.get('DVWA_PASSWORD')
DVWA_BASE_URL = os.environ.get('DVWA_BASE_URL', 'http://10.250.248.71/')
