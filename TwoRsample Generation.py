import pandas as pd
import numpy as np

# 设置样本大小
num_samples = 100

# 随机生成两组样本数据的均值和标准差
# 使用numpy的random模块来生成随机均值和标准差
mean1, std1 = np.random.uniform(-5, 5), np.random.uniform(0.5, 2)
mean2, std2 = np.random.uniform(-5, 5), np.random.uniform(0.5, 2)

# 使用生成的均值和标准差来生成样本数据
sample1 = np.random.normal(mean1, std1, num_samples)
sample2 = np.random.normal(mean2, std2, num_samples)

# 创建一个DataFrame来存储这些数据
df_random = pd.DataFrame({'Sample1': sample1, 'Sample2': sample2})

# 保存DataFrame到CSV文件
df_random.to_csv('random_sample_data.csv', index=False)

# 打印生成的均值和标准差，以及DataFrame的前几行以作为展示
print("Sample1 - Mean:", mean1, "Std:", std1)
print("Sample2 - Mean:", mean2, "Std:", std2)
print(df_random.head())
