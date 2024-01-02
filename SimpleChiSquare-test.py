import pandas as pd
from scipy.stats import chi2_contingency

# 读取 CSV 文件
filepath = r''  # 替换为您的文件路径
df = pd.read_csv(filepath)

# 假设您的 CSV 文件中有两列数据需要进行卡方检验
# 这里的 'column1' 和 'column2' 是示例列名，您需要替换为您的实际列名
crosstab = pd.crosstab(df['Sample1'], df['Sample2'])

# 执行卡方检验
chi2, p, dof, expected = chi2_contingency(crosstab)

# 打印结果
print(f"Chi-Square Value = {chi2}")
print(f"P-value = {p}")
print(f"Degrees of Freedom = {dof}")
print("Expected Counts:")
print(expected)

# 根据 p 值判断独立性
if p < 0.05:
    print("两个变量相关 (拒绝原假设)")
else:
    print("两个变量独立 (不能拒绝原假设)")
