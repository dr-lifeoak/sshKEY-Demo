import pandas as pd
import scipy.stats as stats

# 读取CSV文件
data = pd.read_csv(r'')  # 将'path_to_your_file.csv'替换为自己的文件的路径

# 假设数据分为两个不同的sample
sample1 = data['Sample1']
sample2 = data['Sample2']

# 执行独立样本t检验
t_statistic, p_value = stats.ttest_ind(sample1, sample2)

# 打印结果
print("t统计量:", t_statistic)
print("p值:", p_value)

# 判断是否拒绝零假设
alpha = 0.05
if p_value < alpha:
    print("有足够的证据拒绝零假设，即两个样本组之间存在显著差异。")
else:
    print("没有足够的证据拒绝零假设，即两个样本组之间不存在显著差异。")

