import pandas as pd
import os

# 定义处理 CSV 文件的函数
def process_file(file_path, output_path):
    # 读取 CSV 文件
    data = pd.read_csv(file_path)

    # 删除不需要的列
    data = data.drop(columns=['year_built', 'title'], errors='ignore')

    # 提取 followers 列中的数字部分
    data['followers'] = data['followers'].str.extract(r'(\d+)').astype(int)

    # 定义转换函数：将 publish_time 转换为天数
    def time_to_days(time_str):
        if '天' in time_str:
            return int(time_str.split('天')[0])
        elif '个月' in time_str:
            months = int(time_str.split('个月')[0])
            return months * 30  # 按 1 个月 30 天计算
        elif '年' in time_str:
            years = int(time_str.split('年')[0].replace('一', '1'))
            return years * 365  # 按 1 年 365 天计算
        else:
            return None  # 如果格式不匹配

    # 应用转换函数
    data['publish_time'] = data['publish_time'].apply(time_to_days)

    # 定义转换函数：提取房间数
    def extract_rooms(house_type):
        parts = house_type.split('室')
        if len(parts) > 1:
            bedrooms = int(parts[0])  # 提取卧室数
            living_rooms = int(parts[1].split('厅')[0])  # 提取厅数
            return bedrooms + living_rooms  # 总房间数
        return None  # 如果格式不匹配，返回 None

    # 应用转换函数
    data['rooms'] = data['house_type'].apply(extract_rooms)

    # 删除原来的 house_type 列
    data = data.drop(columns=['house_type'], errors='ignore')

    # 保存处理后的文件
    data.to_csv(output_path, index=False)

# 处理多个文件
files_to_process = [
    "output/dongcheng_cleaned.csv",
    "output/huairou_cleaned.csv",
    "output/haidian_cleaned.csv",
    "output/tongzhou_cleaned.csv"
]

# 输出文件夹
output_folder = "cleaned_data"

# 确保输出文件夹存在
os.makedirs(output_folder, exist_ok=True)

# 循环处理每个文件
for file in files_to_process:
    # 获取文件名（不含路径）
    file_name = os.path.basename(file)
    # 定义输出文件路径
    output_file = os.path.join(output_folder, file_name)
    # 处理文件并保存
    process_file(file, output_file)

print("所有文件已处理完成！")
