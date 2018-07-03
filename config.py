import os
from constants import USER_AGENT_KEY, ITEM_PIPELINES_KEY

# DVWA application config
DVWA_USER_NAME = os.environ.get('DVWA_USERNAME')
DVWA_PASSWORD = os.environ.get('DVWA_PASSWORD')
DVWA_BASE_URL = os.environ.get('DVWA_BASE_URL')

# Misc helpers
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

# Scrapy config
CRAWLER_PROCESS_USER_AGENT = 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
CRAWLER_PIPELINE = {'crawler.pipelines.CrawlerPipeline': 300}
DVWA_CRAWLER_SETTINGS = {
    USER_AGENT_KEY: CRAWLER_PROCESS_USER_AGENT,
    ITEM_PIPELINES_KEY: CRAWLER_PIPELINE
}


