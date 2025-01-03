# Python与R语言大作业

## 1. 大作业题目 

二手房数据分析 

## 2. 作业内容 

**（1） 获取数据集：**使用Python爬虫从贝壳或链家网站中获取北京市东城区、海淀区、通州区、怀柔区的在售二手房数据，并选择合适的方式进行存储数据。下面的数据分析均针对东城区、海淀区、通州区、怀柔区这四个区的数据进行。（20分）  

**要求：每个城区的数据不少于1000条，字段属性不少于10个，**提交的作业中包含：  

1） 爬取方法作为报告的一个独立章节。 *

2） 爬虫代码和爬取到的原始数据文件。  

代码：指明在提交代码目录中所属文件名、模块名、函数名。（见：各功能源代码说明表示例）  

原始数据文件：格式自选，可以是SQL数据文件或csv数据文件或其他格式的数据文件。

**（2） 数据预处理：**对采集到的数据集进行重复值处理、缺失值处理、异常值的检测与处理。（10分）  

要求：报告中要写明做了哪些预处理操作和预处理的步骤，至少要进行重复值处理和缺失值处理，提交的作业中应包含：  

1） 预处理方法作为报告的一个独立章节；  

2） 处理代码和预处理后的数据文件。  代码：指明在提交代码目录中所属文件名、模块名、函数名。（见：各功能源代码说明表示例）

预处理后的数据文件：格式自选，可以与原始数据文件不一致。 

**（3） 这四个城区在售的二手房有哪些特点，**不限于从总价、单价、户型类别、楼层、建筑面积、建筑年代、电梯安装情况等属性进行统计性分析和可视化分析。例如，进行统计学分析时，可以使用箱线图分析并展示平均值、最大值、最小值等统计值的关系。（30分） 

要求：分析的数据特征不少于5个，分析每种数据特征时可视化图形种类不少于一种，比如，分析二手房单价（5个特征之一）时，如果使用箱线图，则需要分别绘制四个城区的箱线图。提交的报告中应包含：  

1） 统计分析和可视化分析的思路和结论作为报告的一个独立章节，本章节中插入可视化的图形（给出图题）。

 2）图形绘制代码。（指明在提交代码目录中所属文件名、模块名、函数名。见：各功能源代码说明表示例）  

**（4） 分析影响房价的主要因素有哪些**，即分析房价与其他变量之间的关系。  例如：分析住房面积对二手房总价的影响，绘制住房面积与总价的散点图，对比分析四个城区之间的不同，并给出合理的分析。（20分） 

要求：分析的变量不少于1种，可视化图形种类不少于两种。  

1） 分析的思路和结论作为报告的一个独立章节，本章节中插入可视化的图形（给出图题）。 

 2） 图形绘制代码。指明在提交代码目录中所属文件名、模块名、函数名。见：各功能源代码说明表示例）。  

**（5） 在地图上绘制这四个城区中在售二手房单位面积价格平均值的热力图和在售二手房总金额的热力图**，分析二手房价格的地理分布特征。例如，图中越红的区域表明单位房价越高。（20分）  

要求：报告中应有上述要求的两个热力图，并给出适当的分析。  

1） 分析的结论作为报告的一个独立章节，章节中插入可视化的图形（给出图题）。  

2） 图形绘制代码。（指明在提交代码目录中所属文件名、模块名、函数名。见：各功能源代码说明表示例）。  

**（6） 选做题：使用任意一种算法对数据进行分析建模**，预测房价走势。例如，使用机器学习中的线性回归模型，将数据划分训练集和测试集，选择一个或多个相关的数据特征对模型进行训练，需要解释你选择的特征为什么与房价相关，最后使用测试集评估模型的准确率。（10分）  

要求：  

1） 预测的思路和结论作为报告的一个独立章节，给出体现预测结果的数据（图、表均可）  

2） 预测的代码。（指明在提交代码目录中所属文件名、模块名、函数名。见：各功能源代码说明表示例）。 

**整体要求**  

（1） 应使用Python或R语言实现上述功能（也可以python与R混用），代码中给出必要和合理注释。  

（2） 报告要求不少于3000字，避免大篇幅的展示程序代码，可以展示部分关键代码（代码不计字数）。  

（3） 提交作业时应将源代码、数据文件和报告放至压缩包，一并提交。  报告内容：至少包括上述每一步要求的部分。  数据文件：包括：原始数据文件和预处理后的数据文件。  源代码：全部源放在一个目录下，并给出readme，说明如何执行可以得到上述每个要求的功能。

## 3. 实验具体过程

### 3.1 爬虫获取房价数据集

#### 3.1.1 链家网页分析

本次爬取链家网站中北京二手房的信息https://bj.lianjia.com/ershoufang/；

![](C:\Users\Zxzx\AppData\Roaming\Typora\typora-user-images\image-20241231142232874.png)

我们需要分别从东城区、海淀区、通州区、怀柔区爬取在售的二手房记录，对应的网址分别为https://bj.lianjia.com/ershoufang/dongcheng/、https://bj.lianjia.com/ershoufang/haidian/、https://bj.lianjia.com/ershoufang/tongzhou/、https://bj.lianjia.com/ershoufang/huairou/；了解清楚要爬取的网站的url后我们开始查看我们要爬取的具体的数据项，以东城区的二手房为例，观察链家二手房网页链家规律以及html规律；

![image-20241231145037438](C:\Users\Zxzx\AppData\Roaming\Typora\typora-user-images\image-20241231145037438.png)

观察html的具体内容，可以看到二手房的信息全部保存在li class=’clear’里面，包括房屋户型、所在楼层、建筑面积、户型结构、套内面积、建筑类型、房屋朝向、建筑结构、装修情况、梯户比例、供暖方式、配备电梯和房屋价格共13个属性，我们后续可以在得到每个页面的html后进行匹配读取,此外我们还发现不同的页面后加pg+页面数即可，即pg后面的数字表示第几页。所以访问时设置一个列表循环访问即可；

![image-20241231223330436](C:\Users\Zxzx\AppData\Roaming\Typora\typora-user-images\image-20241231223330436.png)

之后我们就可以根据我们观察到的HTML格式从爬取到的页面中正则匹配我们想要的数据

#### 3.1.2 链家数据的爬取

class为title中包含了房屋标题名属性，该HTML语句观察如下：

```html
<div class="title"><a class="" href="https://bj.lianjia.com/ershoufang/101123985657.html" target="_blank" data-log_index="1" data-el="ershoufang" data-housecode="101123985657" data-is_focus="" data-sl="">远大园六区 2室1厅 东南</a><!-- 拆分标签 只留一个优先级最高的标签--></div>
```

我们使用如下Python语句进行信息提取：

```python
 titles = response.xpath('//*[@id="content"]/div[1]/ul/li/div[1]/div[2]/div/a[1]/text()').getall()
 ......
 item = LianjiaItem()
 item['title'] = title
```

class为positionInfo中包含了房屋位置的属性，该HTML语句观察如下：

```html
<div class="positionInfo"><span class="positionIcon"></span><a href="https://bj.lianjia.com/xiaoqu/1114891833397117/" target="_blank" data-log_index="1" data-el="region">远大园六区 </a>   -  <a href="https://bj.lianjia.com/ershoufang/shijicheng/" target="_blank">世纪城</a> </div>
```

我们使用如下Python语句进行信息提取：

```python
positions = response.xpath('//*[@id="content"]/div[1]/ul/li/div[1]/div[2]/div/a[2]/text()').getall()
...
item['position'] = position
```

class为positionInfo中包含了房屋房间数目(房屋类型)、房屋面积、房屋朝向、房间的装修等级、房屋所处楼层、房屋修建时间(可选，有些房子没有)、房屋所处的建筑类型等属性，该HTML语句观察如下：

```html
<div class="houseInfo"><span class="houseIcon"></span>2室1厅 | 102.07平米 | 东南 | 简装 | 中楼层(共16层)  | 塔楼</div>
```

我们使用如下Python语句进行信息提取，注意这里会产生问题，即有些房屋没有修建时间，如果也使用这样的代码进行爬取收集会出现将房屋的建筑类型替代房屋修建年龄属性的情况：

```python
directions = response.xpath('//*[@id="content"]/div[1]/ul/li/div[1]/div[3]/div/text()').getall()
...
direction_parts = direction.split(' | ')
item['title'] = title
item['house_type'] = direction_parts[0] if len(direction_parts) > 0 else ''
item['area'] = direction_parts[1] if len(direction_parts) > 1 else ''
item['orientation'] = direction_parts[2] if len(direction_parts) > 2 else ''
item['decoration'] = direction_parts[3] if len(direction_parts) > 3 else ''
item['floor'] = direction_parts[4] if len(direction_parts) > 4 else ''
item['year_built'] = direction_parts[5] if len(direction_parts) > 5 else ''
item['building_type'] = direction_parts[6] if len(direction_parts) > 6 else ''
```

可能出现的错误如下，我们可以在后续的数据预处理部分再重新修订：

![](C:\Users\Zxzx\AppData\Roaming\Typora\typora-user-images\image-20250103132115599.png)

class为totalPrice中包含了房屋总价和单价两属性，该HTML语句观察如下：

```html
<div class="priceInfo"><div class="totalPrice totalPrice2"><i> </i><span class="">760</span><i>万</i></div><div class="unitPrice" data-hid="101127721546" data-rid="1111027377016" data-price="47447"><span>47,447元/平</span></div></div>
```

我们使用如下Python语句进行信息提取：

```python
prices = response.xpath('//*[@id="content"]/div[1]/ul/li/div[1]/div[6]/div[1]/span/text()').getall()
price_per_m_s = response.xpath('//*[@id="content"]/div[1]/ul/li/div[1]/div[6]/div[2]/span/text()').getall()
...
item['price'] = price
item['price_per_m'] = price_per_m
```

class为followInfo中包含了房屋关注人数和发售时间两属性，该HTML语句观察如下：

```html
<div class="followInfo"><span class="starIcon"></span>12人关注 / 8个月以前发布</div>
```

我们使用如下Python语句进行信息提取：

```python
followers = response.xpath('//*[@id="content"]/div[1]/ul/li/div[1]/div[4]/text()').getall()
...
follower_parts = follower.split(' / ')
item['followers'] = follower_parts[0] if len(follower_parts) > 0 else ''
item['publish_time'] = follower_parts[1] if len(follower_parts) > 1 else ''
```

之后我们将提取到的信息打包封装到我们定义的爬取信息结构体中，一并写入到csv文件中去，每一个区一个csv文件

#### 3.1.3 爬取部分小结

爬虫总体流程概括如下：

1. **定位字段的 XPath**

   通过 XPath 表达式找到 HTML 页面中各字段对应的元素，并提取这些字段的值，通过class属性定位到**titles**、**directions**、**prices**、**price_per_m_s**、**positions**和**followers**字段中；

2. ### **数据解析和封装**

   通过 XPath 获取的列表进行逐条处理，每次提取一组字段的值，并封装到一个 `item` 中，这一步要熟悉对XPath的内容获取，不然爬取下来的可能不是我们想要的数据；

3. **处理房源的多个数据**

   逐一遍历处理一套房的多个属性，包括**title**、**house_type**、**area**、**orientation**、**decoration**、**floor**、**year_built**、**building_type**、**price**、**price_per_m**、**position**、**followers**、**publish_time**，共计13个属性(之后还会丢弃或者生成各种新属性，这里指我们爬取的原始属性)，并打包生成一个爬取的item对象；

4. **将原始数据写入CSV文件**

   最终将处理好的item对象逐个写入对应文件夹下的csv文件保存起来即可；

爬虫模块的所属的文件为**scraper.py**，主要内容包含在**scraper.py**文件中的**class LianjiaSpider(scrapy.Spider)**中，部分写入和调用功能是现在了LianjiaPipeline中，具体的爬虫功能在**LianjiaSpider**类中实现，类中定义了我们要爬取的网页url，发送请求的cookie和hearder(需要注意，由于链家有反扒机制，如果要复现爬虫部分需要重新生成并替换cookie和hearder，不然无法通过链家网站的人机检验机制！！)，LianjiaSpider类的实现的功能如下(部分出现在LianjiaPipeline中的辅助功能我也归类如下)：

| 函数名                               | 函数实现的功能                    |
| ------------------------------------ | --------------------------------- |
| def start_requests(self)             | 向网页发送请求                    |
| def parse(self, response)            | 数据爬取的实现逻辑                |
| def open_spider(self, spider)        | 启动爬虫                          |
| def close_spider(self, spider)       | 关闭爬虫                          |
| def process_item(self, item, spider) | 将爬到的数据分区写入达到CSV文件中 |

### 3.2 数据预处理

预处理部分主要分为两大块，第一节为基本的预处理，即调整数据表格中的列属性、处理缺失值、异常值等；第二节为特征工程，即明确各个属性是数值属性或非数值属性，删除可能冗余的属性或生成必要的新属性。

#### 3.2.1 基本预处理

我们在爬取到数据后就可以进行第一步的数据预处理，因此数据预处理的第一个模块我打算和爬虫功能一起实现，具体的内容如下：

- 移除重复数据，将重复的行进行删除

  ```python
  df.drop_duplicates(inplace=True)
  ```

- 填充缺失值，将修建年份未知的填入'暂无数据'

  ```python
  df['year_built'] = df['year_built'].fillna('暂无数据')
  df.fillna('未知', inplace=True)
  ```

- 纠正数据异常，这一操作主要是为了修正上一节爬虫中遇到的有些房子修建年龄属性缺失，导致将建筑类型填充到修建年龄这一列的问题

  ```python
  def correct_building_type(row):
      if row['year_built'] not in ['暂无数据'] and not row['year_built'].endswith('年'):
          row['building_type'] = row['year_built']
          row['year_built'] = '暂无数据'
      return row
  df = df.apply(correct_building_type, axis=1)
  ```

- 数值处理，将明显为数值属性的特征数字化，方便接下来的特征分析

  - 价格

    ```python
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    ```

  - 面积

    ```python
    df['area'] = df['area'].str.replace('平米', '').astype(float, errors='ignore')
    ```

  - 每平米价格

    ```python
    df['price_per_m'] = df['price_per_m'].str.replace('元/平', '').str.replace(',', '').astype(float, errors='ignore')
    ```

- 保存结果，将初步与处理好的数据写入到xx_cleaned.csv(比如dongcheng_cleaned.csv)文件中，便于我们后续使用

  ```python
  df.to_csv(output_path, index=False, encoding='utf-8-sig')
  ```

#### 3.2.2 特征工程

这一节的质量好坏直接影响了后续的二手房特点分析，特征工程做好了后续的分析才能事倍功半，我们以东城区为例，其余各区和东城区做一样的操作，便于统一分析；

观察发现东城区中built_year属性缺失率实在是太高了，我们考虑直接将该列从各个区的数据中移除，不纳入后续的分析；
![](C:\Users\Zxzx\AppData\Roaming\Typora\typora-user-images\image-20250103144125522.png)

此外，**我们不需要这些数据的标题列**，这个属性对我们分析房子的价格没有任何影响，应该也一并丢弃；经过对数据的观察，**我们可以将followers和publish_time这两列数据进行优化**，转变为数值属性方便之后的分析；**整合house_type属性**，将形如'3室1厅'这样的属性变成4表示房间总数形成新列rooms，从简处理就不区分客厅和卧室的数量了(这样做不利于分别讨论客厅数目和卧室数目对价格的影响)；并**把orientation属性空格前的值作为改列的新属性**；**处理floor属性**，只保留高、中、低三种属性，对于只有楼层的数据行给予删除；

综上我们给出以下预处理操作，具体内容为丢弃修建时间、丢弃title列、将关注人数变成数值属性(保留人数)并将发布时间转为按天为单位，将house_type列整合为rooms列(即将该列变成房间数目)，取orientation空格前的方位：

```python
 # 删除 'year_built' 列
    data = data.drop(columns=['year_built'], errors='ignore')

    # 删除 'title' 列
    data = data.drop(columns=['title'], errors='ignore')

    # 提取 follower 列中的数字部分
    data['followers'] = data['followers'].str.extract(r'(\d+)').astype(int)

    # 定义转换函数
    def time_to_days(time_str):
        if isinstance(time_str, str):
            if '天' in time_str:
                return int(time_str.split('天')[0])
            elif '个月' in time_str:
                months = int(time_str.split('个月')[0])
                return months * 30  # 按 1 个月 30 天计算
            elif '年' in time_str:
                years = int(time_str.split('年')[0].replace('一', '1'))
                return years * 365  # 按 1 年 365 天计算
        return None  # 如果格式不匹配或不是字符串

    # 应用转换函数
    data['publish_time'] = data['publish_time'].apply(time_to_days)

    # 定义转换函数
    def extract_rooms(house_type):
        if isinstance(house_type, str):
            parts = house_type.split('室')
            if len(parts) > 1:
                bedrooms = int(parts[0])  # 提取卧室数
                living_rooms = int(parts[1].split('厅')[0])  # 提取厅数
                return bedrooms + living_rooms  # 总房间数
        return None  # 如果格式不匹配，返回 None

    # 应用转换函数
    data['rooms'] = data['house_type'].apply(extract_rooms)

    # 删除原来的 house_types 列
    data = data.drop(columns=['house_type'], errors='ignore')

    # 预处理 'orientation' 列，取空格前的方向
    def preprocess_orientation(orientation):
        if isinstance(orientation, str):
            # 提取空格前的部分
            return orientation.split()[0]
        return orientation  # 如果不是字符串，直接返回原值

    data['orientation'] = data['orientation'].apply(preprocess_orientation)
    
    # 预处理 'floor' 列
    def preprocess_floor(floor_str):
        # 如果包含 '低楼层'、'中楼层' 或 '高楼层'，则保留
        if '低楼层' in floor_str:
            return '低楼层'
        elif '中楼层' in floor_str:
            return '中楼层'
        elif '高楼层' in floor_str:
            return '高楼层'
        # 如果是单纯的楼层数字（如 '11层'），丢弃该行
        return None

    # 应用预处理函数并丢弃无效的行
    data['floor'] = data['floor'].apply(preprocess_floor)
    data = data.dropna(subset=['floor'])  # 丢弃没有楼层类型的行
```

对各个区应用这些预处理操作并生成最终的预处理后的csv文件：

![image-20250103151108055](C:\Users\Zxzx\AppData\Roaming\Typora\typora-user-images\image-20250103151108055.png)

注：这里经过两轮处理，第一轮在爬虫部分完成，第二轮在预处理模块中完成，因此在output和cleaned_data两个文件夹中都有xx_cleaned.csv文件，最终的预处理后的文件保存在cleaned_data中；

#### 3.3.3 数据预处理部分小结

预处理总体流程概括如下：

1. **爬虫阶段的数据预处理**

   这一步主要是对刚拿到手的数据进行粗加工，对异常列和缺失值做第一手的处理，为后续的特征工程提供便利；

2. **数据预处理模块中的数据预处理**

   这一步是对粗加工后的数据做更加细致的预处理，包括删除缺失值太多的列、删除无用的列、对非数值类数据进行必要的数值化，为后续的房价分析和绘图做好准备；

数据预处理部分包含在**scraper.py**和**cleaning.py**两个程序中，其中scraper.py完成数据的粗加工，cleaning.py完成特征工程部分，两者结合起来实现对数据的预处理工作，实现具体功能的函数如下：

| 函数名                                   | 函数实现的功能                                |
| ---------------------------------------- | --------------------------------------------- |
| def data_preprocessing(self)             | 数据的粗加工，包含于scraper.py文件中          |
| def process_file(file_path, output_path) | 数据的特征工程部分，在cleaning.py文件中       |
| def time_to_days(time_str)               | 时间转化，用于将发布时间统一转化为天          |
| def extract_rooms(house_type)            | 房间数目转化，用于将house_type转化为rooms属性 |
| def preprocess_orientation(orientation)  | 处理朝向，只保留一个方向(一个方向足以描述)    |
| def preprocess_floor(floor_str)          | 处理楼层，删去具体的层数                      |

### 3.3  各城区二手房特点分析

##### 3.3.1 特征图像绘制和分析

我们对四个区依次进行特点分析，对每个区我们都绘制五张图像并分析图像的含义，分别绘制**price 的箱线图**、**area 和 price_per_m 的散点图**、**decoration 的饼状图**、**building_type 的直方图**和 **publish_time 和 price 的散点图**，代码逻辑如下：

```python
	    # 绘制 price 的箱线图
        plt.figure(figsize=(8, 6))
        sns.boxplot(x=df['price'])
        plt.title(f'{district_name} - Boxplot of Price')
        plt.savefig(f"{output_folder}/{district_name}_price_boxplot.png")
        plt.close()

        # 绘制 area 和 price_per_m 的散点图
        plt.figure(figsize=(8, 6))
        sns.scatterplot(x=df['area'], y=df['price_per_m'])
        plt.title(f'{district_name} - Scatter plot of Area vs Price per m²')
        plt.xlabel('Area')
        plt.ylabel('Price per m²')
        plt.savefig(f"{output_folder}/{district_name}_area_price_scatter.png")
        plt.close()

        # 绘制 decoration 的饼状图
        decoration_counts = df['decoration'].value_counts()
        plt.figure(figsize=(8, 6))
        decoration_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90, cmap='Set3')
        plt.title(f'{district_name} - Decoration Distribution')
        plt.ylabel('')  # 去掉 y 轴标签
        plt.savefig(f"{output_folder}/{district_name}_decoration_pie.png")
        plt.close()

        # 绘制 building_type 的直方图
        plt.figure(figsize=(8, 6))
        sns.histplot(df['building_type'], kde=False, bins=len(df['building_type'].unique()))
        plt.title(f'{district_name} - Building Type Distribution')
        plt.xlabel('Building Type')
        plt.ylabel('Frequency')
        plt.savefig(f"{output_folder}/{district_name}_building_type_histogram.png")
        plt.close()

        # 绘制 publish_time 和 price 的散点图
        # 确保 publish_time 转为日期类型
        if not pd.api.types.is_datetime64_any_dtype(df['publish_time']):
            df['publish_time'] = pd.to_datetime(df['publish_time'])

        plt.figure(figsize=(8, 6))
        sns.scatterplot(x=df['publish_time'], y=df['price'])
        plt.title(f'{district_name} - Scatter plot of Publish Time vs Price')
        plt.xlabel('Publish Time')
        plt.ylabel('Price')
        plt.xticks(rotation=45)
        plt.savefig(f"{output_folder}/{district_name}_publish_time_price_scatter.png")
        plt.close()
```

具体分区的可视化图像和对应的分析如下：

- 东城区

  1. price的箱线图

     ![dongcheng_price_boxplot](E:\CodePlace\Python\Python-with-R-language-final-assignment\output_charts\dongcheng_price_boxplot.png)

     该图像告诉我们，东城区房价的中位数在700w左右，数据整体微微右偏，即使是二手房价格却普遍不低，且虚高房价不少，符合对北京城区房子的一般印象；

  2. area和price_per_m的散点图

     ![dongcheng_area_price_scatter](E:\CodePlace\Python\Python-with-R-language-final-assignment\output_charts\dongcheng_area_price_scatter.png)

     观察东城区中面积和每平米价格的散点图可以发现东城区的房子面积普遍小于100平米，但是单价却并不低，进一步说明了东城区地价高，地段优越，即便是二手房也非常抢手；

  3. decoration属性的饼状图

     ![dongcheng_decoration_pie](E:\CodePlace\Python\Python-with-R-language-final-assignment\output_charts\dongcheng_decoration_pie.png)

     从饼状图可以非常清晰地看出东城区的在售二手房中，精装修的房子占到了大多数，大多数家庭并不吝啬于装修自己房屋，房屋的居住环境普遍较好；

  4. building_type的直方图

     ![dongcheng_building_type_histogram](E:\CodePlace\Python\Python-with-R-language-final-assignment\output_charts\dongcheng_building_type_histogram.png)

     从东城建筑类型柱状图中可以发现东城区的房子以板楼结构为主，板塔结合和塔楼两者数量接近；

  5. publish_time和price的散点图 

     ![dongcheng_publish_time_price_scatter](E:\CodePlace\Python\Python-with-R-language-final-assignment\output_charts\dongcheng_publish_time_price_scatter.png)
     
     这幅图像说明，绝大多数房子的房价并不随着发售时间的推移而降价，且在售房屋没有明显的减少趋势，证明原房主并不急于出手，房屋普遍比较保值；

- 海淀区

  1. price的箱线图

     ![haidian_price_boxplot](E:\CodePlace\Python\Python-with-R-language-final-assignment\output_charts\haidian_price_boxplot.png)

     该图像告诉我们，海淀区房价的中位数接近1000w，售价相当高，数据整体倾向于右偏，且和东城区类似，即便是二手房价格却普遍不低，且虚高房价不少，房价十分高；

  2. area和price_per_m的散点图

     ![haidian_area_price_scatter](E:\CodePlace\Python\Python-with-R-language-final-assignment\output_charts\haidian_area_price_scatter.png)

     观察海淀区中面积和每平米价格的散点图可以发现东城区的房子面积普遍小于100平米，但是单价却并不低，甚至和东城区相比这一特点更加突出，房屋小而单价贵，进一步说明了海淀区地价高，地段优越，即便是二手房也非常抢手；

  3. decoration属性的饼状图

     ![haidian_decoration_pie](E:\CodePlace\Python\Python-with-R-language-final-assignment\output_charts\haidian_decoration_pie.png)

     和东城区类似，海淀区的房屋精装比例占比很高，居住环境普遍较好；

  4. building_type的直方图

     ![haidian_building_type_histogram](E:\CodePlace\Python\Python-with-R-language-final-assignment\output_charts\haidian_building_type_histogram.png)

     海淀区的房屋以塔楼结构居多，板楼次之，板塔结构的房屋最少；

  5. publish_time和price的散点图 

     ![haidian_publish_time_price_scatter](E:\CodePlace\Python\Python-with-R-language-final-assignment\output_charts\haidian_publish_time_price_scatter.png)
     
     随着发售时间的推移，房价有一定的下降趋势，但并不是非常明显，且在售房屋数目没有明显的减少趋势，房子普遍比较保值；

- 通州区

  1. price的箱线图

     ![tongzhou_price_boxplot](E:\CodePlace\Python\Python-with-R-language-final-assignment\output_charts\tongzhou_price_boxplot.png)

     该图像告诉我们，通州区房价的中位数接近400w，售价相较于东城海淀明显低了很多，数据无明显左右偏，有些房子价格虚高或过低，整体分布比较均匀；

  2. area和price_per_m的散点图

     ![tongzhou_area_price_scatter](E:\CodePlace\Python\Python-with-R-language-final-assignment\output_charts\tongzhou_area_price_scatter.png)

     通州区大部分房子在100平米左右，相较于东城海淀，大于140平米的房子明显更多且每平米售价很集中，说明通州区居住用地不像海淀和东城那么紧张，地段特别突出的地方较少；

  3. decoration属性的饼状图

     ![tongzhou_decoration_pie](E:\CodePlace\Python\Python-with-R-language-final-assignment\output_charts\tongzhou_decoration_pie.png)

     精装房屋的比例小于50%，可能说明最初的房东买下来的时候主要并不是急于自己居住，新房比例可能比较高，可能当初一手交易的时候就是为了二手转出，所以原房主并不急于装修；

  4. building_type的直方图

     ![tongzhou_building_type_histogram](E:\CodePlace\Python\Python-with-R-language-final-assignment\output_charts\tongzhou_building_type_histogram.png)

     通州在售的二手房以板楼结构居多，板塔结合的次之，塔楼结构很少；

  5. publish_time和price的散点图 

     ![tongzhou_publish_time_price_scatter](E:\CodePlace\Python\Python-with-R-language-final-assignment\output_charts\tongzhou_publish_time_price_scatter.png)
     
     可以发现随着时间的推移通州区在售二手房有明显的减少趋势，大部分房子在售一年内大概率能卖出，房子成交数目较东城海淀高很多，房子以居住性质为主；

- 怀柔区

  1. price的箱线图

     ![huairou_price_boxplot](E:\CodePlace\Python\Python-with-R-language-final-assignment\output_charts\huairou_price_boxplot.png)

     该图像告诉我们，怀柔区房价的中位数在250w左右，售价相较于其余三区明显低了很多，数据无明显左右偏，有些房子价格虚高，整体分布比较均匀；

  2. area和price_per_m的散点图

     ![huairou_area_price_scatter](E:\CodePlace\Python\Python-with-R-language-final-assignment\output_charts\huairou_area_price_scatter.png)

     怀柔区大部分房子面积集中在100平米左右，在售二手房整体面积分布比较均匀，每平米售价相较于其他区更低，说明怀柔区居住用地不像其他区那么紧张，地段特别突出的地方较少；

  3. decoration属性的饼状图

     ![image-20250103174207059](C:\Users\Zxzx\AppData\Roaming\Typora\typora-user-images\image-20250103174207059.png)

     该区的精装修房屋占比最低，可能说明最初的房东买下来的时候主要并不是急于自己居住，新房比例可能比较高，可能当初一手交易的时候就是为了二手转出，所以原房主并不急于装修；

  4. building_type的直方图
  
     ![huairou_building_type_histogram](E:\CodePlace\Python\Python-with-R-language-final-assignment\output_charts\huairou_building_type_histogram.png)
  
     怀柔区以板楼结构为主，其他类型的建筑非常少；
  
  5. publish_time和price的散点图 
  
     ![huairou_publish_time_price_scatter](E:\CodePlace\Python\Python-with-R-language-final-assignment\output_charts\huairou_publish_time_price_scatter.png)
     
     房屋售价没有随着发布时间的推移呈现出明显的降低趋势，此外在发布时间长的区间里在售房屋的数目也不少，二手房成交率不是特别高，房屋关注度相较于其他区低很多；

##### 3.3.2 各城区二手房特点分析部分小结

这一部分主要对4个区分别绘制了五张图（涵盖了饼状图、箱线图和散点图），涵盖了五个以上的属性（price、publish_time、decoration、building_type、area和price_per_m），并对其中有特点的地方进行了分析，比如**海淀、东城**的房子的价格、关注度、房屋精装比例都比**怀柔和通州**的房子要高，**通州区**的房屋居住性质很强，相应的**海淀、东城和怀柔**的房屋成交比率不是特别高；

本节为接下来影响房价的主要因素分析打下了基础，该部分的代码包含于**data_analysis.py中**，由于该部分主要是以画图为主，并不需要额外设计太多函数，本节就不设置模块表格了；

### 3.4 影响房价的主要因素分析

和上一小节一样，我们分区域进行研究；实验思路如下：**对于数值类数据**，我们画出变量之间的热力图；**对于非数值类数据**，我们直接画出和price和各个非数值属性的散点图，并标注高于对应区price中位数的样本数目；

#### 3.4.1 分区域讨论对价格影响的因素

- 东城区

  1. 对数值类属性绘制热力图

     ![dongcheng_heatmap](E:\CodePlace\Python\Python-with-R-language-final-assignment\analysis_charts\dongcheng_heatmap.png)

     从热力图中可以很清晰的得出price和area是强相关关系，即房屋面积越大总价就会越高；

  2. 对非数值属性绘制散点图

     ![dongcheng_orientation_price_scatter](E:\CodePlace\Python\Python-with-R-language-final-assignment\analysis_charts\dongcheng_orientation_price_scatter.png)

     ![dongcheng_floor_price_scatter](E:\CodePlace\Python\Python-with-R-language-final-assignment\analysis_charts\dongcheng_floor_price_scatter.png)

     ![dongcheng_decoration_price_scatter](E:\CodePlace\Python\Python-with-R-language-final-assignment\analysis_charts\dongcheng_decoration_price_scatter.png)

     ![dongcheng_building_type_price_scatter](E:\CodePlace\Python\Python-with-R-language-final-assignment\analysis_charts\dongcheng_building_type_price_scatter.png)

     分析以上图标我们可以发现东城区的房子中，我们统计各个非数值属性中房价大于中位数的房子数目并绘制散点图，得到如下结论：**房屋朝向东南**、**精装**和**中低楼层**都和房屋价格正相关；

  3. 东城区对价格影响大的因素总结如下：

     房屋**面积越大**、**楼层中低**、**房屋朝向南或东**、**装修越好**的价格越高；

- 海淀区

  1. 对数值类属性绘制热力图

     ![haidian_heatmap](E:\CodePlace\Python\Python-with-R-language-final-assignment\analysis_charts\haidian_heatmap.png)

     从热力图中可以很清晰的得出price和area和rooms是强相关关系，即房屋面积越大、房间数目越多总价就会越高；

  2. 对非数值属性绘制散点图

     ![haidian_orientation_price_scatter](E:\CodePlace\Python\Python-with-R-language-final-assignment\analysis_charts\haidian_orientation_price_scatter.png)

     ![haidian_floor_price_scatter](E:\CodePlace\Python\Python-with-R-language-final-assignment\analysis_charts\haidian_floor_price_scatter.png)

     ![haidian_decoration_price_scatter](E:\CodePlace\Python\Python-with-R-language-final-assignment\analysis_charts\haidian_decoration_price_scatter.png)

     ![haidian_building_type_price_scatter](E:\CodePlace\Python\Python-with-R-language-final-assignment\analysis_charts\haidian_building_type_price_scatter.png)
     
     分析以上图标我们可以发现海淀区的房子中，我们统计各个非数值属性中房价大于中位数的房子数目并绘制散点图，得到如下结论：**房屋朝向东南**、**精装**和**中低楼层**都和房屋价格正相关；
     
  3. 海淀区对价格影响大的因素总结如下：

     房屋**面积越大**、**房间数目越多**、**楼层中低**、**房屋朝向南或东**、**装修越好**的价格越高；

- 怀柔区

  1. 对数值类属性绘制热力图

     ![huairou_heatmap](E:\CodePlace\Python\Python-with-R-language-final-assignment\analysis_charts\huairou_heatmap.png)

     从热力图中可以很清晰的得出price和area和price_per_m是强相关关系，即房屋面积越大、房屋单价越高则总价就会越高；

  2. 对非数值属性绘制散点图

     ![huairou_orientation_price_scatter](E:\CodePlace\Python\Python-with-R-language-final-assignment\analysis_charts\huairou_orientation_price_scatter.png)

     ![huairou_floor_price_scatter](E:\CodePlace\Python\Python-with-R-language-final-assignment\analysis_charts\huairou_floor_price_scatter.png)

     ![huairou_decoration_price_scatter](E:\CodePlace\Python\Python-with-R-language-final-assignment\analysis_charts\huairou_decoration_price_scatter.png)

     ![huairou_building_type_price_scatter](E:\CodePlace\Python\Python-with-R-language-final-assignment\analysis_charts\huairou_building_type_price_scatter.png)
     
     分析以上图标我们可以发现怀柔区的房子中，我们统计各个非数值属性中房价大于中位数的房子数目并绘制散点图，得到如下结论：**房屋朝向南**、**建筑类型是板楼**和**中高楼层**都和房屋价格正相关；
     
  3. 怀柔区对价格影响大的因素总结如下：

     房屋**面积越大**、**每平米单价越高**、**楼层中高**、**房屋朝向南**、**建筑类型是板楼**的总价格越高；

- 通州区

  1. 对数值类属性绘制热力图

     ![tongzhou_heatmap](E:\CodePlace\Python\Python-with-R-language-final-assignment\analysis_charts\tongzhou_heatmap.png)

     从热力图中可以很清晰的得出price和area和price_per_m是强相关关系，即房屋面积越大、房屋单价越高则总价就会越高；

  2. 对非数值属性绘制散点图

     ![tongzhou_orientation_price_scatter](E:\CodePlace\Python\Python-with-R-language-final-assignment\analysis_charts\tongzhou_orientation_price_scatter.png)

     ![tongzhou_floor_price_scatter](E:\CodePlace\Python\Python-with-R-language-final-assignment\analysis_charts\tongzhou_floor_price_scatter.png)

     ![tongzhou_decoration_price_scatter](E:\CodePlace\Python\Python-with-R-language-final-assignment\analysis_charts\tongzhou_decoration_price_scatter.png)

     ![tongzhou_building_type_price_scatter](E:\CodePlace\Python\Python-with-R-language-final-assignment\analysis_charts\tongzhou_building_type_price_scatter.png)

     分析以上图标我们可以发现怀柔区的房子中，我们统计各个非数值属性中房价大于中位数的房子数目并绘制散点图，得到如下结论：**房屋朝向南**、**建筑类型是板楼**、**房屋精装修**和**中高楼层**都和房屋价格正相关；

  3. 通州区对房价影响大的因素如下：

     房屋**面积越大**、**每平米单价越高**、**楼层中高**、**房屋朝向南**、**建筑类型是板楼**、**装修越好**的总价格越高

- 各区房价因素影响异同总结

  | 区划名 | 和房屋总价格正相关的因素                                     |
  | ------ | ------------------------------------------------------------ |
  | 东城区 | **面积越大**、**楼层中低**、**房屋朝向南或东**、**装修越好** |
  | 海淀区 | **面积越大**、**房间数目越多**、**楼层中低**、**房屋朝向南或东**、**装修越好** |
  | 怀柔区 | **面积越大**、**每平米单价越高**、**楼层中高**、**房屋朝向南**、**建筑类型是板楼** |
  | 通州区 | **面积越大**、**每平米单价越高**、**楼层中高**、**房屋朝向南**、**建筑类型是板楼**、**装修越好** |

#### 3.4.2 分区域讨论对价格的影响部分的小结

这一部分的代码包含于**price_analysis.py**，和上一小节一样没有特别需要说明的代码和模块功能，在此就不罗列模块功能表了；

### 3.5 在地图上绘制各城区二手房的价格热力图并分析背后的原因

#### 3.5.1 地图的绘制逻辑和绘制的地图展示

我们对四个区依次进行特点分析，对每个区我们都绘制五张图像并分析图像的含义，我们先来简单描述一下我们的地图绘制逻辑；

根据我们爬取的数据中的position属性，我们没法直接在地图上描点画图，我们必须借助相关的地图API根据地名获取我们的经纬度并最后在地图上作图，这次我们调用高德API获取房产的经纬度，将回传的经纬度数据保存并在地图上分别绘制总价和单价的热力图，代码实现逻辑如下：

```python
# 添加经纬度列
df['latitude'], df['longitude'] = zip(*df['position'].apply(geocode_address))
...
# 创建基础地图（背景设置为 OpenStreetMap）
m = folium.Map(location=[39.9042, 116.4074], zoom_start=12, tiles='OpenStreetMap')

# 添加价格每平米的热力图
heatmap_data_price_per_m = df[['latitude', 'longitude', 'price_per_m']].values.tolist()
HeatMap(heatmap_data_price_per_m, name='Price per m² Heatmap', min_opacity=0.5, max_zoom=15).add_to(m)

# 添加总价的热力图
heatmap_data_price = df[['latitude', 'longitude', 'price']].values.tolist()
HeatMap(heatmap_data_price, name='Total Price Heatmap', min_opacity=0.5, max_zoom=15).add_to(m)
```

调用高德API的代码逻辑实现如下：

```python
def geocode_address(address):

    # 使用高德地图 API 将地址转换为经纬度
    url = f'https://restapi.amap.com/v3/geocode/geo?address={address}&city=北京&key={AMAP_API_KEY}'
    response = requests.get(url).json()
    if response['status'] == '1' and response['geocodes']:
        location = response['geocodes'][0]['location']
        lng, lat = map(float, location.split(','))
        return lat, lng
    else:
        return None, None
```

基于这个逻辑我们绘制每个区的单价和总价的热力分布图并分析可能的原因：

- 东城区

  东城区房屋单价分布热力图如下：

  ![image-20250103191205625](C:\Users\Zxzx\AppData\Roaming\Typora\typora-user-images\image-20250103191205625.png)

  东城区房屋总价分布热力图如下：

  ![image-20250103191246497](C:\Users\Zxzx\AppData\Roaming\Typora\typora-user-images\image-20250103191246497.png)

  由于单价和总价分布基本一致，我们选其中之一讨论出现图中高热度区的原因即可；可以发现房价热力高的点集中分布在东直门街道和和平里街道，这附近配套设施良好（医院学校公园等），交通便利，距CBD近地价高；

- 海淀区

  海淀区房屋单价分布热力图如下：

  ![image-20250104021948685](C:\Users\Zxzx\AppData\Roaming\Typora\typora-user-images\image-20250104021948685.png)

  海淀区房屋总价分布热力图如下：

  ![image-20250103191338269](C:\Users\Zxzx\AppData\Roaming\Typora\typora-user-images\image-20250103191338269.png)

  由于单价和总价分布基本一致，我们选其中之一讨论出现图中高热度区的原因即可；可以发现房价热力高的点集中分布在中关村街道，这附近配套设施良好（医院学校公园等），交通便利，靠近高新技术园区，高校林立，地价很高；

- 怀柔区

  怀柔区房屋单价分布热力图如下：

  ![image-20250103191408321](C:\Users\Zxzx\AppData\Roaming\Typora\typora-user-images\image-20250103191408321.png)

  怀柔区房屋总价分布热力图如下：

  ![image-20250103191421603](C:\Users\Zxzx\AppData\Roaming\Typora\typora-user-images\image-20250103191421603.png)

  由于单价和总价分布基本一致，我们选其中之一讨论出现图中高热度区的原因即可；可以发现房价热力高的点集中分布在怀柔区市区部分，这附近配套较怀柔区其他部分配套设施更好，交通相对更加便利；

- 通州区

  通州区房屋单价分布热力图如下：

  ![image-20250103191500873](C:\Users\Zxzx\AppData\Roaming\Typora\typora-user-images\image-20250103191500873.png)
  
  通州区房屋总价分布热力图如下：
  
  ![image-20250103191520741](C:\Users\Zxzx\AppData\Roaming\Typora\typora-user-images\image-20250103191520741.png)
  
  由于单价和总价分布基本一致，我们选其中之一讨论出现图中高热度区的原因即可；可以发现房价热力高的点集中分布在通运街道和临河里街道，这附近靠近景区，交通便利，距北京副中心近相较于通州其他区低价更高；

#### 3.5.2 在地图上绘制各城区二手房的价格热力图并分析背后的原因部分的小结

| 行政区划 | 房价高的区域           | 可能的原因                                                   |
| -------- | ---------------------- | ------------------------------------------------------------ |
| 东城区   | 东直门街道和和平里街道 | 配套设施良好（医院学校公园等），交通便利，距CBD近地价高      |
| 海淀区   | 中关村街道             | 配套设施良好（医院学校公园等），交通便利，靠近高新技术园区，高校林立，地价很高 |
| 怀柔区   | 怀柔区市区部分         | 较怀柔区其他部分配套设施更好，交通相对更加便利               |
| 通州区   | 通运街道和临河里街道   | 靠近景区，交通便利，距北京副中心近                           |

这一部分的代码包含于**draw_map.py**，和上一小节一样没有特别需要说明的代码和模块功能，在此就不罗列模块功能表了；

### 3.6 房价走势建模预测

#### 3.6.1 房价预测的具体实现思路

我们就在东城区数据集上开展预测，实验思路如下：

**特征选择**：

- 选用以下特征预测房价：

  - `area`（面积）
  - `decoration`（装修）
  - `floor`（楼层）
  - `orientation`（朝向）

  为什么选择以上特征来进行训练模型？因为根据3.4节中对东城区房价影响最大的因素讨论结果可知，面积、装修水平、楼层和房屋朝向和房价正相关水平较高，因此选择这四个属性来进行预测；

**数据预处理**：

- **类别特征编码**：将非数值型特征（如 `decoration`）编码为数值。
- **标准化数值特征**：对 `area` 进行标准化，消除量纲对模型的影响。

**模型构建**：

- 使用 `statsmodels` 实现线性回归。
- 通过最小二乘法计算回归系数，建立线性模型。

**模型评估**：

- 使用训练集训练模型，测试集评估模型性能。
- 指标：
  - **R²**：衡量模型对房价变化的解释能力。
  - **MSE**：评估模型预测误差。

大致的代码逻辑如下：

```python
# 编码非数值特征
label_encoder = LabelEncoder()
for col in ['decoration', 'floor', 'orientation']:
    df[col] = label_encoder.fit_transform(df[col])

# 标准化连续变量
scaler = StandardScaler()
df['area'] = scaler.fit_transform(df[['area']])

# 线性回归建模
X = df[features]
X = sm.add_constant(X)  # 添加常数项
y = df[target]

# 拆分训练集和测试集
train_size = int(0.8 * len(X))
X_train, X_test = X.iloc[:train_size], X.iloc[train_size:]
y_train, y_test = y.iloc[:train_size], y.iloc[train_size:]

# 使用 OLS 进行线性回归
model = sm.OLS(y_train, X_train).fit()

# 打印模型摘要
print(model.summary())

# 模型预测
y_pred = model.predict(X_test)
```

得到的模型性能和预测结果和实际数据分布图如下：

![image-20250104024308120](C:\Users\Zxzx\AppData\Roaming\Typora\typora-user-images\image-20250104024308120.png)

![image-20250104024234372](C:\Users\Zxzx\AppData\Roaming\Typora\typora-user-images\image-20250104024234372.png)

#### 3.6.2 房价预测部分的总结

这一部分的代码包含于**predication.py**，主要是调用库函数对房价进行预测，和上一小节一样没有特别需要说明的代码和模块功能，在此就不罗列模块功能表了；

## 4. 实验心得与总结

本次实验围绕北京市四个城区的二手房数据展开，从数据的获取、预处理、分析到可视化，以及最后的建模预测。以下是我在实验过程中获得的一些心得体会：

1. **数据采集和爬取**
   通过使用爬虫技术获取真实的二手房数据，我充分体会到如何使用Python语言开展网络爬虫。从起初的目标站点分析到应对反爬策略，再到成功获取大规模的数据并，每一步都需要细致的规划和耐心的尝试。

2. **数据预处理的重要性**
   数据预处理环节让我深刻认识到，数据质量直接影响分析结果的可靠性和可用性。清洗重复值、处理缺失值以及检测异常值的过程帮助我熟练掌握了数据清理的常用方法，也让我体会到这一环节的复杂性和必要性。

3. **数据可视化**
   在数据分析和特征探索的过程中，可视化为我提供了极大的帮助。通过图形的直观呈现，我能够迅速识别数据的分布特征、趋势和潜在关系。绘制箱线图、散点图和热力图的过程也增强了我对各种可视化工具的熟悉程度。

4. **多维数据分析的洞察**
   在分析房价影响因素时，我进一步理解了不同变量（如面积、户型、楼层等）对房价的多维影响。这让我认识到，在实际问题中，单一特征的分析往往不足，需要结合多种因素才能得出更加全面的结论。

5. **基于大数据的机器学习**
   通过构建机器学习模型进行房价预测，我掌握了数据建模的基本流程，包括特征选择、数据划分、模型训练和评估。这部分内容尤其让我感受到数学理论与实际应用结合的魅力，同时也让我意识到模型性能受限于数据质量和特征选择的重要性。

6. **Python语言的灵活使用**

   Python语言功能丰富，使用方便，本次实验充分使用了本学期学到的各种python语言技巧，包括但不限于网络爬虫（scrapy）、数据预处理和分析（Numpy、Pandas）、数据可视化和热力图（matplotlib、python对API的调用）等等，极大的促进了我对python语言的理解和使用，让我深刻理解到python语言在大数据领域和机器学习的重要性。

### 实验总结

1. **实验成果**
   - 成功获取北京市东城区、海淀区、通州区和怀柔区的二手房数据，每个区的样本数超过1000条，字段属性超过10个。
   - 数据预处理过程完整，消除了重复值和缺失值，并处理了异常值。
   - 完成了从房价统计特征到影响因素分析的多维度探索，生成了多种图表（如箱线图、散点图、热力图），并形成了清晰的分析结论。
   - 在选做题中，使用线性回归模型进行了房价预测（以东城区为例），取得了不错的预测结果。
2. **收获与成长**
   - 熟悉了数据采集、预处理、分析、可视化和建模的全流程。
   - 掌握了网络爬虫的基本方法，增强了应对反爬机制的能力。
   - 提升了数据清洗、可视化设计和统计分析的实战技能。
   - 初步掌握了机器学习模型的构建和性能评估方法。
3. **不足与改进方向**
   - 爬虫过程中耗费的时间较长，反扒策略有待加强（每次爬取都要重新获取cookie和header不然就会被拦截）。
   - 数据分析和可视化部分的深度仍有待提升，例如在探索变量之间关系时，可引入更多的统计检验方法。
   - 选用的模型较为基础，未来可以尝试更复杂的机器学习或深度学习模型以提升预测精度。

## 5. 实验额外说明

实验报告分为五个部分，前两节介绍实验的具体要求和要实现的目标，第三第四小结集中展示了实验的实验思路和实验具体流程，并对关键代码和图像进行了阐释和分析，每个实验要求的实现均单独组成一个章节，且将对应的模块和功能实现(具体的函数)部分附在章节末尾，此外还在代码的readme部分详细说明了每个模块的功能和如果要复现需要进行的步骤和事项。所有的表格编码均采用UTF-8，使用正确的格式打开csv才不会乱码！

