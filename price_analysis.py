import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pylab import mpl

# 设置中文显示
mpl.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 指定默认字体，解决中文显示问题

# 指定数据文件夹路径
data_folder = "cleaned_data"
output_folder = "analysis_charts"

# 创建保存图表的文件夹（如果不存在）
os.makedirs(output_folder, exist_ok=True)

# 遍历文件夹中的每个 CSV 文件
for file_name in os.listdir(data_folder):
    if file_name.endswith(".csv"):  # 确保是 CSV 文件
        # 提取区名
        district_name = file_name.split("_")[0]

        # 读取数据
        file_path = os.path.join(data_folder, file_name)
        df = pd.read_csv(file_path)

        # 计算该区价格的中位数
        price_median = df['price'].median()

        # 绘制数值属性的热力图
        numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
        corr_matrix = df[numeric_columns].corr()  # 计算相关性矩阵

        plt.figure(figsize=(10, 8))
        sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm', cbar=True)
        plt.title(f'{district_name} - Heatmap of Numeric Attributes')
        plt.savefig(f"{output_folder}/{district_name}_heatmap.png")
        plt.close()


        # 绘制非数值属性和 price 的散点图

        non_numeric_columns = df.select_dtypes(exclude=['float64', 'int64']).columns
        non_numeric_columns = [col for col in non_numeric_columns if col != 'position']  # 去除 position 列

        for col in non_numeric_columns:
            # 统计每种取值中价格超过中位数的数量
            value_counts_above_median = (
                df[df['price'] > price_median][col]
                .value_counts()
                .to_dict()
            )
            # 构造统计信息
            stats = ", ".join(
                [f"{key}: {value}" for key, value in value_counts_above_median.items()]
            )

            # 绘制散点图
            plt.figure(figsize=(10, 6))
            sns.scatterplot(x=df[col], y=df['price'])
            plt.title(f'{district_name} - Scatter plot of {col} vs Price\n(>Median {price_median:.0f}: {stats})')
            plt.xlabel(col)
            plt.ylabel('Price')
            plt.xticks(rotation=45)  # 类别较多则适当旋转标签
            plt.savefig(f"{output_folder}/{district_name}_{col}_price_scatter.png")
            plt.close()

print("所有图表已生成并保存到 analysis_charts 文件夹中！")
