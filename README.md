### 趣事百科爬虫
>趣事百科爬虫24小时热榜数据爬取存入mongodb

* 修改mongodb地址 [db](QSBK/items.py)
```python
    @classmethod
    def from_settings(cls, settings):
        client = pymongo.MongoClient('mongodb://localhost:27017/')  # 修改mongodb地址
        mydb = client['qushibaike']
        return cls(client, mydb['artile'])
```
 * scrapy crawl qsbkspider 


