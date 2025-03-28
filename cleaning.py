import pandas as pd
import os

def process_file(file_path, output_path):
    # 读取 CSV 文件
    data = pd.read_csv(file_path)

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

    # 确保输出路径存在
    os.makedirs(output_path, exist_ok=True)

    # 保存到新的 CSV 文件
    output_file = os.path.join(output_path, os.path.basename(file_path))
    data.to_csv(output_file, index=False, encoding='utf-8-sig')

# 处理多个文件
process_file("output/dongcheng_cleaned.csv", "cleaned_data/")
process_file("output/haidian_cleaned.csv", "cleaned_data/")
process_file("output/huairou_cleaned.csv", "cleaned_data/")
process_file("output/tongzhou_cleaned.csv", "cleaned_data/")
