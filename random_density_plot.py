import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# 设置随机种子以确保可重复性
np.random.seed(42)

# 生成随机数（1000个，从正态分布中）
random_numbers = np.random.normal(loc=100, scale=15, size=1000)

# 创建图表
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# 绘制直方图和密度曲线
axes[0].hist(random_numbers, bins=30, density=True, alpha=0.7, color='blue', edgecolor='black')

# 添加密度曲线（使用核密度估计）
density = stats.gaussian_kde(random_numbers)
x = np.linspace(random_numbers.min(), random_numbers.max(), 100)
axes[0].plot(x, density(x), 'r-', linewidth=2, label='KDE密度曲线')
axes[0].set_xlabel('值')
axes[0].set_ylabel('密度')
axes[0].set_title('随机数分布（直方图 + 密度曲线）')
axes[0].legend()
axes[0].grid(alpha=0.3)

# 绘制纯密度图
axes[1].fill_between(x, density(x), alpha=0.7, color='skyblue', edgecolor='darkblue', linewidth=2)
axes[1].plot(x, density(x), 'b-', linewidth=2)
axes[1].set_xlabel('值')
axes[1].set_ylabel('密度')
axes[1].set_title('随机数密度图')
axes[1].grid(alpha=0.3)

plt.tight_layout()
plt.savefig('random_density_plot.png', dpi=150, bbox_inches='tight')
print("图表已保存为 'random_density_plot.png'")
plt.show()

# 打印统计信息
print(f"随机数统计信息：")
print(f"平均值: {random_numbers.mean():.2f}")
print(f"标准差: {random_numbers.std():.2f}")
print(f"最小值: {random_numbers.min():.2f}")
print(f"最大值: {random_numbers.max():.2f}")
