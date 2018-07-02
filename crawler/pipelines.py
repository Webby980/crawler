class CrawlerPipeline(object):

    def process_item(self, item, spider):
        page = item['url'].split("/")[-2]
        filename = 'dvwa-%s.html' % page
        with open(filename, 'wb') as file:
            file.write(item['body'])
        return item
