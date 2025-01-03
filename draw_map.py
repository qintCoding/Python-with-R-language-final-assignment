import os
import pandas as pd
import folium
from folium.plugins import HeatMap
import requests

# 设置高德地图 API Key
AMAP_API_KEY = '0a714fba59879ad6613b6488e00ce706'

# 数据文件夹路径
data_folder = "cleaned_data"
output_folder = "analysis_charts"

# 创建输出文件夹
os.makedirs(output_folder, exist_ok=True)


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


for file_name in os.listdir(data_folder):
    if file_name.endswith(".csv"):  # 确保是 CSV 文件
        district_name = file_name.split("_")[0]

        # 读取数据
        file_path = os.path.join(data_folder, file_name)
        df = pd.read_csv(file_path)

        # 添加经纬度列
        df['latitude'], df['longitude'] = zip(
            *df['position'].apply(geocode_address)
        )

        # 删除无效地址
        df = df.dropna(subset=['latitude', 'longitude'])

        # 创建基础地图（背景设置为 OpenStreetMap）
        m = folium.Map(location=[39.9042, 116.4074], zoom_start=12, tiles='OpenStreetMap')

        # 添加价格每平米的热力图
        heatmap_data_price_per_m = df[['latitude', 'longitude', 'price_per_m']].values.tolist()
        HeatMap(heatmap_data_price_per_m, name='Price per m² Heatmap', min_opacity=0.5, max_zoom=15).add_to(m)

        # 添加总价的热力图
        heatmap_data_price = df[['latitude', 'longitude', 'price']].values.tolist()
        HeatMap(heatmap_data_price, name='Total Price Heatmap', min_opacity=0.5, max_zoom=15).add_to(m)

        # 添加图层控制器（切换单价和总价热力图）
        folium.LayerControl().add_to(m)

        # 保存地图
        map_path = os.path.join(output_folder, f"{district_name}_heatmap.html")
        m.save(map_path)

        print(f"{district_name} 的热力图已保存至 {map_path}")

print("所有地图生成完毕！")
