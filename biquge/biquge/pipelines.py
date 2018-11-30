# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
class BiqugePipeline(object):


    def process_item(self, item, spider):

        #return item
       
        curPath = 'E:/小说/'
        tempPath = str(item['name'])

        targetPath = curPath+ tempPath  
        #print('-----')
        #print(targetPath)
        if not os.path.exists(targetPath):
            os.makedirs(targetPath)  
         
        filename_path = targetPath+'/'+ str(item['chapter_name']) + '.txt'
        print('------')
        print(filename_path)
        print(item['chapter_content'])  
        with open(filename_path, 'a', encoding='utf-8') as f: 
            f.writelines(item['chapter_content'])  
        
        return item
      
   
