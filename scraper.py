import scrapy
from scrapy.crawler import CrawlerProcess
import csv
import pandas as pd
import os


class LianjiaItem(scrapy.Item):
    # Item定义保持不变
    title = scrapy.Field()
    house_type = scrapy.Field()
    area = scrapy.Field()
    orientation = scrapy.Field()
    decoration = scrapy.Field()
    floor = scrapy.Field()
    year_built = scrapy.Field()
    building_type = scrapy.Field()
    price = scrapy.Field()
    price_per_m = scrapy.Field()
    position = scrapy.Field()
    followers = scrapy.Field()
    publish_time = scrapy.Field()
    start_url = scrapy.Field()


class LianjiaPipeline:
    def __init__(self):
        self.file_handles = {}
        self.writers = {}

    def open_spider(self, spider):
        # 确保目录存在
        output_dir = 'output'
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # 为每个区域创建CSV文件
        regions = ['dongcheng', 'haidian', 'huairou', 'tongzhou']
        for region in regions:
            file_path = os.path.join(output_dir, f'{region}.csv')
            self.file_handles[region] = open(file_path, 'w', newline='', encoding='utf-8-sig')
            self.writers[region] = csv.DictWriter(self.file_handles[region], fieldnames=[
                'title', 'house_type', 'area', 'orientation', 'decoration',
                'floor', 'year_built', 'building_type', 'price',
                'price_per_m', 'position', 'followers', 'publish_time'
            ])
            self.writers[region].writeheader()

    def close_spider(self, spider):
        # 关闭所有文件句柄
        for file_handle in self.file_handles.values():
            file_handle.close()

        # 数据第一次预处理
        self.data_preprocessing()

    def process_item(self, item, spider):
        # 确定数据属于哪个区域
        start_url = item['start_url']
        region = None
        for r in ['dongcheng', 'haidian', 'huairou', 'tongzhou']:
            if r in start_url:
                region = r
                break

        if region:
            # 创建要写入的数据字典
            row_dict = {
                'title': item.get('title', ''),
                'house_type': item.get('house_type', ''),
                'area': item.get('area', ''),
                'orientation': item.get('orientation', ''),
                'decoration': item.get('decoration', ''),
                'floor': item.get('floor', ''),
                'year_built': item.get('year_built', ''),
                'building_type': item.get('building_type', ''),
                'price': item.get('price', ''),
                'price_per_m': item.get('price_per_m', ''),
                'position': item.get('position', ''),
                'followers': item.get('followers', ''),
                'publish_time': item.get('publish_time', '')
            }

            try:
                self.writers[region].writerow(row_dict)
                self.file_handles[region].flush()  # 确保数据立即写入文件
            except Exception as e:
                spider.logger.error(f'Error writing to {region}.csv: {str(e)}')

        return item

    def data_preprocessing(self):
        output_dir = 'output'
        for filename in ['dongcheng', 'haidian', 'huairou', 'tongzhou']:
            try:
                input_path = os.path.join(output_dir, f'{filename}.csv')
                output_path = os.path.join(output_dir, f'{filename}_cleaned.csv')

                # 读取CSV文件
                df = pd.read_csv(input_path, encoding='utf-8-sig')

                # 数据清洗
                df.drop_duplicates(inplace=True)
                df['year_built'] = df['year_built'].fillna('暂无数据')  # 填充缺失的建成时间为“暂无数据”
                df.fillna('未知', inplace=True)  # 填充其他列的缺失值

                # 检查并修正建筑类型被错误填入建筑时间中的情况
                def correct_building_type(row):
                    if row['year_built'] not in ['暂无数据'] and not row['year_built'].endswith('年'):
                        row['building_type'] = row['year_built']
                        row['year_built'] = '暂无数据'
                    return row

                df = df.apply(correct_building_type, axis=1)
                # 处理数值类型
                df['price'] = pd.to_numeric(df['price'], errors='coerce')
                df['area'] = df['area'].str.replace('平米', '').astype(float, errors='ignore')
                df['price_per_m'] = df['price_per_m'].str.replace('元/平', '').str.replace(',', '').astype(float,
                                                                                                           errors='ignore')

                # 保存处理后的数据
                df.to_csv(output_path, index=False, encoding='utf-8-sig')
            except Exception as e:
                print(f'Error processing {filename}: {str(e)}')


class LianjiaSpider(scrapy.Spider):
    name = "lianjia"
    allowed_domains = ["bj.lianjia.com"]
    start_urls = [
        "https://bj.lianjia.com/ershoufang/dongcheng/",
        "https://bj.lianjia.com/ershoufang/haidian/",
        "https://bj.lianjia.com/ershoufang/huairou/",
        "https://bj.lianjia.com/ershoufang/tongzhou/"
    ]

    def start_requests(self):
        cookies = {
            'lianjia_uuid': '17b79646-5837-435f-846d-9cfff5dfb2c5',
            'select_city': '110000',
            'Hm_lvt_46bf127ac9b856df503ec2dbf942b67e': '1735876759',
            'HMACCOUNT': 'E5B12C20858E845E',
            '_jzqc': '1',
            '_jzqckmp': '1',
            '_qzjc': '1',
            'sajssdk_2015_cross_new_user': '1',
            'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%221942a514e2c2415-072e92c30a057a-26011851-1638720-1942a514e2d1cff%22%2C%22%24device_id%22%3A%221942a514e2c2415-072e92c30a057a-26011851-1638720-1942a514e2d1cff%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24latest_referrer_host%22%3A%22www.google.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%7D',
            '_ga': 'GA1.2.1127874382.1735876770',
            '_gid': 'GA1.2.1582632213.1735876770',
            'login_ucid': '2000000461197904',
            'lianjia_token': '2.00149f9b384283a4840532b209466157ba',
            'lianjia_token_secure': '2.00149f9b384283a4840532b209466157ba',
            'security_ticket': 'joopZpyD+IrijK7YCx92PF/bhEcT8Ug0P01OMNm/k9xomqQtlWb50+2muV2YbPj/14V7nMRX6YvrZxvr9fS4UQRb6t38DPFInvjsWa2NiymArFi7My9hWGqdszoN0GIeIWLa8RbHS/PQHy8abIQWy3y0vm/ND4CuCvr+CqSU8To=',
            'ftkrc_': '4198a02a-e979-461c-ba74-e35ee841016c',
            'lfrc_': '5d82d9db-829a-412d-8062-05a045b9bc36',
            'lianjia_ssid': 'a0f78921-44be-4aab-a0b0-5214f3691a45',
            '_jzqa': '1.1321930983939710500.1735876759.1735880779.1735889846.4',
            '_jzqx': '1.1735876759.1735889846.3.jzqsr=google%2Ecom|jzqct=/.jzqsr=google%2Ecom|jzqct=/',
            'Hm_lpvt_46bf127ac9b856df503ec2dbf942b67e': '1735889849',
            '_qzja': '1.1744237685.1735876758920.1735880779322.1735889845950.1735889845950.1735889848709.0.0.0.7.4',
            '_qzjb': '1.1735889845950.2.0.0.0',
            '_qzjto': '7.4.0',
            '_jzqb': '1.2.10.1735889846.1',
            'srcid': 'eyJ0Ijoie1wiZGF0YVwiOlwiYmVkYjY5YTY2NDg0YzAxOTY3YmMyYjk5MjZhNzc2YWVjNjlhYmZmM2UzODIzZjk3YWNlNzZmZmIxNDFjZDRjOTYzMmQxNDE0OWUxMDEyODFlZjZhN2FhNjQ1YzRiNmFkN2FmZjgzZTJkMTIxNTc1MTVmMDA1M2Q3ZjJiOTY2NmI1ZDQ1ZGY0MWRhOTQyNmJmM2QwYTY0NzVlMzE4ZTAzNjAwZTEwNDE0ZmY5OTBhNDcxMWE1ODkwMjYwOGJkMDUzZDY0YzU4Y2MwYzExMmRhNzIwM2E2ZTUwOTgwODdhM2U3OGU2YjhlOTczNWI3OWNhYjNlNzU5ZTc5NjJkZDljZFwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCJmZGI2YTUyN1wifSIsInIiOiJodHRwczovL2JqLmxpYW5qaWEuY29tL2Vyc2hvdWZhbmcvIiwib3MiOiJ3ZWIiLCJ2IjoiMC4xIn0=',
            '_gat': '1',
            '_gat_past': '1',
            '_gat_global': '1',
            '_gat_new_global': '1',
            '_gat_dianpu_agent': '1',
            '_ga_KJTRWRHDL1': 'GS1.2.1735889858.4.1.1735889859.0.0.0',
            '_ga_QJN1VP0CMS': 'GS1.2.1735889858.4.1.1735889859.0.0.0',
        }

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            # 'Cookie': 'lianjia_uuid=17b79646-5837-435f-846d-9cfff5dfb2c5; select_city=110000; Hm_lvt_46bf127ac9b856df503ec2dbf942b67e=1735876759; HMACCOUNT=E5B12C20858E845E; _jzqc=1; _jzqckmp=1; _qzjc=1; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221942a514e2c2415-072e92c30a057a-26011851-1638720-1942a514e2d1cff%22%2C%22%24device_id%22%3A%221942a514e2c2415-072e92c30a057a-26011851-1638720-1942a514e2d1cff%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24latest_referrer_host%22%3A%22www.google.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%7D; _ga=GA1.2.1127874382.1735876770; _gid=GA1.2.1582632213.1735876770; login_ucid=2000000461197904; lianjia_token=2.00149f9b384283a4840532b209466157ba; lianjia_token_secure=2.00149f9b384283a4840532b209466157ba; security_ticket=joopZpyD+IrijK7YCx92PF/bhEcT8Ug0P01OMNm/k9xomqQtlWb50+2muV2YbPj/14V7nMRX6YvrZxvr9fS4UQRb6t38DPFInvjsWa2NiymArFi7My9hWGqdszoN0GIeIWLa8RbHS/PQHy8abIQWy3y0vm/ND4CuCvr+CqSU8To=; ftkrc_=4198a02a-e979-461c-ba74-e35ee841016c; lfrc_=5d82d9db-829a-412d-8062-05a045b9bc36; lianjia_ssid=a0f78921-44be-4aab-a0b0-5214f3691a45; _jzqa=1.1321930983939710500.1735876759.1735880779.1735889846.4; _jzqx=1.1735876759.1735889846.3.jzqsr=google%2Ecom|jzqct=/.jzqsr=google%2Ecom|jzqct=/; Hm_lpvt_46bf127ac9b856df503ec2dbf942b67e=1735889849; _qzja=1.1744237685.1735876758920.1735880779322.1735889845950.1735889845950.1735889848709.0.0.0.7.4; _qzjb=1.1735889845950.2.0.0.0; _qzjto=7.4.0; _jzqb=1.2.10.1735889846.1; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiYmVkYjY5YTY2NDg0YzAxOTY3YmMyYjk5MjZhNzc2YWVjNjlhYmZmM2UzODIzZjk3YWNlNzZmZmIxNDFjZDRjOTYzMmQxNDE0OWUxMDEyODFlZjZhN2FhNjQ1YzRiNmFkN2FmZjgzZTJkMTIxNTc1MTVmMDA1M2Q3ZjJiOTY2NmI1ZDQ1ZGY0MWRhOTQyNmJmM2QwYTY0NzVlMzE4ZTAzNjAwZTEwNDE0ZmY5OTBhNDcxMWE1ODkwMjYwOGJkMDUzZDY0YzU4Y2MwYzExMmRhNzIwM2E2ZTUwOTgwODdhM2U3OGU2YjhlOTczNWI3OWNhYjNlNzU5ZTc5NjJkZDljZFwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCJmZGI2YTUyN1wifSIsInIiOiJodHRwczovL2JqLmxpYW5qaWEuY29tL2Vyc2hvdWZhbmcvIiwib3MiOiJ3ZWIiLCJ2IjoiMC4xIn0=; _gat=1; _gat_past=1; _gat_global=1; _gat_new_global=1; _gat_dianpu_agent=1; _ga_KJTRWRHDL1=GS1.2.1735889858.4.1.1735889859.0.0.0; _ga_QJN1VP0CMS=GS1.2.1735889858.4.1.1735889859.0.0.0',
            'Referer': 'https://bj.lianjia.com/',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        for url in self.start_urls:
            for i in range(1, 40):
                full_url = f"{url}pg{i}/"
                yield scrapy.Request(
                    url=full_url,
                    cookies=cookies,
                    headers=headers,
                    callback=self.parse,
                    meta={'start_url': url}
                )

    def parse(self, response):
        print(response.text)
        titles = response.xpath('//*[@id="content"]/div[1]/ul/li/div[1]/div[2]/div/a[1]/text()').getall()
        directions = response.xpath('//*[@id="content"]/div[1]/ul/li/div[1]/div[3]/div/text()').getall()
        prices = response.xpath('//*[@id="content"]/div[1]/ul/li/div[1]/div[6]/div[1]/span/text()').getall()
        price_per_m_s = response.xpath('//*[@id="content"]/div[1]/ul/li/div[1]/div[6]/div[2]/span/text()').getall()
        positions = response.xpath('//*[@id="content"]/div[1]/ul/li/div[1]/div[2]/div/a[2]/text()').getall()
        followers = response.xpath('//*[@id="content"]/div[1]/ul/li/div[1]/div[4]/text()').getall()

        for title, direction, price, price_per_m, position, follower in zip(titles, directions, prices, price_per_m_s,
                                                                            positions, followers):
            item = LianjiaItem()
            direction_parts = direction.split(' | ')
            item['title'] = title
            item['house_type'] = direction_parts[0] if len(direction_parts) > 0 else ''
            item['area'] = direction_parts[1] if len(direction_parts) > 1 else ''
            item['orientation'] = direction_parts[2] if len(direction_parts) > 2 else ''
            item['decoration'] = direction_parts[3] if len(direction_parts) > 3 else ''
            item['floor'] = direction_parts[4] if len(direction_parts) > 4 else ''
            item['year_built'] = direction_parts[5] if len(direction_parts) > 5 else ''
            item['building_type'] = direction_parts[6] if len(direction_parts) > 6 else ''
            item['price'] = price
            item['price_per_m'] = price_per_m
            item['position'] = position
            follower_parts = follower.split(' / ')
            item['followers'] = follower_parts[0] if len(follower_parts) > 0 else ''
            item['publish_time'] = follower_parts[1] if len(follower_parts) > 1 else ''
            item['start_url'] = response.meta['start_url']  # 添加 start_url 字段
            print(item)
            yield item


def main():
    # 配置Scrapy设置
    settings = {
        'BOT_NAME': 'lianjia',
        'ROBOTSTXT_OBEY': False,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 16,
        'CONCURRENT_REQUESTS_PER_IP': 16,
        'ITEM_PIPELINES': {
            '__main__.LianjiaPipeline': 300,
        },
        'TWISTED_REACTOR': 'twisted.internet.asyncioreactor.AsyncioSelectorReactor',
        'FEED_EXPORT_ENCODING': 'utf-8',
    }

    # 运行爬虫
    process = CrawlerProcess(settings)
    process.crawl(LianjiaSpider)
    process.start()


if __name__ == "__main__":
    main()