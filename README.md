# Python-with-R-language-final-assignment
24-25学年Python与R语言大作业

| 功能               | 文件名                            | 模块名                                                       | 函数名                                                       |
| ------------------ | --------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 获取数据集         | scraper.py                        | class LianjiaPipeline、class LianjiaSpider(scrapy.Spider)    | def start_requests(self)、def parse(self, response)、def open_spider(self, spider)、def close_spider(self, spider)、def process_item(self, item, spider)->以上函数实现的功能在报告中写出 |
| 数据预处理         | cleaning.py和scraper.py(一小部分) | 无                                                           | def process_file(file_path, output_path)、def data_preprocessing(self)、def process_file(file_path, output_path)、def time_to_days(time_str)、def extract_rooms(house_type)、def preprocess_orientation(orientation)、def preprocess_floor(floor_str)->以上函数实现的功能在报告中写出 |
| 统计性分析及可视化 | data_analysis.py                  | 无（直接用库比如pandas、seaborn、matplotlib等）              | 无（主要是调用库的函数）                                     |
| 影响房价因素分析   | price_analysis.py                 | 无（直接用库比如pandas、seaborn、matplotlib等）              | 无（主要是调用库的函数）                                     |
| 热力图分析         | draw_map.py                       | 无（直接用库比如pandas、folium、HeatMap、requests等）        | def geocode_address(address)->调用高德API获取地址            |
| 房价预测           | prediction.py                     | 无（直接用库比如pandas、numpy、statsmodels、matplotlib、sklearn.preprocessing等） | 无（主要是调用库函数）                                       |

复现代码的步骤：

1. 运行scraper.py可以从链家网站上爬取数据（但是一定要用自己的cookie和hearder，不然可能会被检测到是爬取行为而被拒绝），爬取到的原数据和初步预处理的数据会被保存到和scraper.py文件同目录下的output文件夹中；
2. 运行cleaning.py对数据进行预处理，处理完的数据会被保存到和cleaning.py文件同目录下的cleaned_data文件夹中；
3. 运行data_analysis.py可以获取到统计性分析和可视化的所有图表，图表会被保存到和data_analysis.py文件同目录下的output_charts文件夹中；
4. 运行price_analysis.py可以获取到影响房价因素分析中的所有图表，图表会被保存到和price_analysis.py文件同目录下的analysis_charts文件夹中；
5. 运行draw_map.py可以得获取热力图（但是要用自己的高德地图API不然会被拒绝访问），生成的热力图会被保存到draw_map.py文件同目录下的analysis_charts文件夹中；
6. 运行prediction.py可以得到房价预测的结果
