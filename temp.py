import matplotlib.pyplot as plt
import numpy as np

# 配置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']  # 使用黑体或其他中文字体
plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号
plt.rcParams['font.size'] = 11

# 设置随机种子
np.random.seed(42)

# 生成两组数据
x = np.linspace(0, 1, 100)

# 第一组：二次函数关系
y_quadratic = 2 * x**2 - 1.5 * x + 0.5 + np.random.normal(0, 0.05, 100)

# 第二组：三次函数关系
y_cubic = 3 * x**3 - 2 * x**2 + 0.5 * x + 0.3 + np.random.normal(0, 0.08, 100)

# 创建并列的两张图
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# 第一张图：二次关系
axes[0].scatter(x, y_quadratic, alpha=0.6, s=60, marker='o', color='blue', label='散点数据（圆形）')

# 拟合二次多项式
coefficients_quad = np.polyfit(x, y_quadratic, 2)
polynomial_quad = np.poly1d(coefficients_quad)
xs = np.linspace(x.min(), x.max(), 300)
ys_quad = polynomial_quad(xs)
axes[0].plot(xs, ys_quad, 'r-', linewidth=2.5, label=f'二次拟合: $y={coefficients_quad[0]:.2f}x^2 + {coefficients_quad[1]:.2f}x + {coefficients_quad[2]:.2f}$')

axes[0].set_xlabel('$x$', fontsize=12)
axes[0].set_ylabel('$y$', fontsize=12)
axes[0].set_title('二次函数关系', fontsize=12, fontweight='bold')
axes[0].legend(fontsize=10)
axes[0].grid(alpha=0.3)

# 第二张图：三次关系
axes[1].scatter(x, y_cubic, alpha=0.6, s=60, marker='^', color='green', label='散点数据（三角形）')

# 拟合三次多项式
coefficients_cubic = np.polyfit(x, y_cubic, 3)
polynomial_cubic = np.poly1d(coefficients_cubic)
ys_cubic = polynomial_cubic(xs)
axes[1].plot(xs, ys_cubic, 'r-', linewidth=2.5, label=f'三次拟合: $y={coefficients_cubic[0]:.2f}x^3 + {coefficients_cubic[1]:.2f}x^2 + {coefficients_cubic[2]:.2f}x + {coefficients_cubic[3]:.2f}$')

axes[1].set_xlabel('$x$', fontsize=12)
axes[1].set_ylabel('$y$', fontsize=12)
axes[1].set_title('三次函数关系', fontsize=12, fontweight='bold')
axes[1].legend(fontsize=10)
axes[1].grid(alpha=0.3)

plt.tight_layout()
plt.savefig('quadratic_cubic_comparison.png', dpi=150, bbox_inches='tight')
print("图表已保存为 'quadratic_cubic_comparison.png'")
plt.show()
