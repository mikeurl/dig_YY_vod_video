# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import log

class TutorialPipeline(object):
    
    def process_item(self, item, spider):
        try:
            with open( item['data_anchor'] + '.txt', 'r') as fp:
       def process_item(self, item, spider):
    try:
        with open(item['data_anchor'] + '.txt', 'r', encoding='utf-8') as fp:
            if item['data_pid'] in fp.read():
                return item
    except IOError as e:
        if e.errno == 2:
            log.msg(f'Item {item["data_anchor"]}.txt not created', level='WARNING')
    
    with open(item['data_anchor'] + '.txt', 'a', encoding='utf-8') as fp:
        if 'data_pid' in item:
            fp.write('|'.join(item.get_ex_record()) + '\n')
        else:
            fp.write('|'.join(item.get_record()) + '\n')

    return item
