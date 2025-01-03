import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, StandardScaler

# 读取数据
df = pd.read_csv('cleaned_data/dongcheng_cleaned.csv')

# 选择特征和目标变量
features = ['area', 'decoration', 'floor', 'orientation']
target = 'price'
df = df[features + [target]]


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

# 可视化预测值与实际值
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.6)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', linestyle='--')
plt.title("Predicted vs Actual Price")
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.show()
