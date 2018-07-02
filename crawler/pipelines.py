class CrawlerPipeline(object):

    def process_item(self, item, spider):
        crawl_reason = item['crawl_reason']
        page = item['url'].split("/")[-2]
        filename = 'crawler_outputs/dvwa-%s-%s.html' % (page, crawl_reason)
        with open(filename, 'wb') as file:
            file.write(item['body'])
        return item
