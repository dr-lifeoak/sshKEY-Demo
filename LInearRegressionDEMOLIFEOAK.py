# 导入必要的库
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 生成更多的模拟数据
np.random.seed(42)
X = 2 * np.random.rand(10000, 1)
y = 4 + 3 * X + np.random.randn(10000, 1)

# 可视化生成的所有数据点
plt.scatter(X, y, color='blue', alpha=0.1)
plt.title('Generated Data for Linear Regression')
plt.xlabel('X')
plt.ylabel('y')
plt.show()

# 创建并训练线性回归模型
model = LinearRegression()
model.fit(X, y)

# 打印模型的参数
print(f'Intercept (截距): {model.intercept_}')
print(f'Coefficient (斜率): {model.coef_[0][0]}')

# 预测新数据
new_X = np.array([[2.5]])  # 用于预测的新数据点
predicted_y = model.predict(new_X)
print(f'Predicted y for X={new_X[0][0]}: {predicted_y[0][0]}')

# 可视化模型的拟合线
plt.scatter(X, y, color='blue', alpha=0.1)
plt.plot(X, model.predict(X), color='red', linewidth=3)
plt.title('Linear Regression Model')
plt.xlabel('X')
plt.ylabel('y')
plt.show()
