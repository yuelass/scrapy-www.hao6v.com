"""
功能：本项目主要演示Scrapy数据存储MySQL具体操作；
运行环境：win7 64 + python3.6 + scrapy1.4 + mysql；
运行方式：进入scrapyMysql目录（scrapy.cfg目录)输入：

数据库名称：movie
建表语句
CREATE TABLE `newmovie` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `downurl` text,
  `img` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4826 DEFAULT CHARSET=utf8;
scrapy crawl inputMysql
"""
import pymysql.cursors


class MySQLPipeline(object):
    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host='127.0.0.1',  # 数据库地址
            port=3306,  # 数据库端口
            db='movie',  # 数据库名
            user='root',  # 数据库用户名
            passwd='123456',  # 数据库密码
            charset='utf8',  # 编码方式
            use_unicode=True)
        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
#       self.cursor.execute(
#            """insert into newmovie(title,downurl,img)
#            value (%s,%s,%s)""",  # 纯属python操作mysql知识，不熟悉请恶补
 #           (item['title'],  # item里面定义的字段和表字段对应
 #            item['downurl'],
 #            item['img'],
 #            ))
        # 提交sql语句
  #     self.connect.commit()
        try:
            # 查重处理
            self.cursor.execute(
                """select * from newmovie where img = %s""",
                item['img'])
            # 是否有重复数据
            repetition = self.cursor.fetchone()

            # 重复
            if repetition:
                pass

            else:
                # 插入数据
                self.cursor.execute(
                    """insert into newmovie(title,downurl,img)
                    value (%s,%s,%s)""",  # 纯属python操作mysql知识，不熟悉请恶补
                    (item['title'],  # item里面定义的字段和表字段对应
                     item['downurl'],
                     item['img'],
                     ))

            # 提交sql语句
            self.connect.commit()

        except Exception as error:
        # 出现错误时打印错误日志
            log(error)
        return item
        # 必须实现返回


