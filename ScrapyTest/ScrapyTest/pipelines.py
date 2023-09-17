# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from scrapy.exporters import CsvItemExporter

class ScrapytestPipeline:
    def __init__(self):
        self.file = open('ptt.csv', 'wb')
        self.exporter = CsvItemExporter(self.file, encoding = 'big5')
        self.exporter.start_exporting()
    def process_item(self, item, spider):
        item['push'] = int(item['push'])
        self.exporter.export_item(item)
        return item
    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

class DeleteNullTitlePipeline:
    def process_item(self, item, spider):
        title = item['title']
        if title:
            return item
        else:
            raise DropItem('found null title $s', item)