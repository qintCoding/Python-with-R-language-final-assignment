import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pylab import mpl

# 设置中文显示
mpl.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 指定默认字体，解决中文显示问题

# 指定数据文件夹路径
data_folder = "cleaned_data"
output_folder = "output_charts"

# 创建保存图表的文件夹（如果不存在）
os.makedirs(output_folder, exist_ok=True)

# 遍历文件夹中的每个 CSV 文件
for file_name in os.listdir(data_folder):
    if file_name.endswith(".csv"):  # 确保是 CSV 文件
        # 提取区名（假设文件名格式为 "dongcheng_cleaned.csv"）
        district_name = file_name.split("_")[0]

        # 读取数据
        file_path = os.path.join(data_folder, file_name)
        df = pd.read_csv(file_path)

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

        plt.figure(figsize=(8, 6))
        sns.scatterplot(x=df['publish_time'], y=df['price'])
        plt.title(f'{district_name} - Scatter plot of Publish Time vs Price')
        plt.xlabel('Publish Time')
        plt.ylabel('Price')
        plt.xticks(rotation=45)
        plt.savefig(f"{output_folder}/{district_name}_publish_time_price_scatter.png")
        plt.close()

print("所有图表已生成并保存到 output_charts 文件夹中！")
