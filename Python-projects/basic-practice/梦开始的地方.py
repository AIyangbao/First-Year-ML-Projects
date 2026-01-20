import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Rectangle

# 创建图形和坐标轴
fig, ax = plt.subplots(figsize=(10, 6))
plt.subplots_adjust(bottom=0.15)

# 设置标题和标签
ax.set_title('动态正弦&余弦曲线', fontsize=12, pad=10)
ax.set_xlabel('角度（弧度）', fontsize=10)
ax.set_ylabel('函数值', fontsize=10)

# 设置坐标轴范围
ax.set_xlim(0, 2*np.pi)
ax.set_ylim(-2, 2)

# 创建x值数组
x = np.linspace(0, 2*np.pi, 1000)

# 初始化线条
line_sin, = ax.plot([], [], 'r-', label='sin(x)', linewidth=2)
line_cos, = ax.plot([], [], 'b-', label='cos(x)', linewidth=2)

# 添加图例
ax.legend(loc='upper right')

# 添加网格
ax.grid(True, alpha=0.3)

# 添加计时器
timer_text = ax.text(0.85, 0.95, '', transform=ax.transAxes, fontsize=12, 
                   bbox=dict(facecolor='white', alpha=0.8, boxstyle='round,pad=0.5'))

# 添加坐标显示
coord_text = ax.text(0.85, 0.02, '', transform=ax.transAxes, fontsize=8)

# 动画函数
def animate(frame):
    # 计算当前时间
    t = frame * 0.05
    
    # 更新计时器
    minutes = int(t // 60)
    seconds = int(t % 60)
    timer_text.set_text(f'{minutes:02d}:{seconds:02d}')
    
    # 计算函数值
    y_sin = np.sin(x + t)
    y_cos = np.cos(x + t)
    
    # 更新线条数据
    line_sin.set_data(x, y_sin)
    line_cos.set_data(x, y_cos)
    
    # 更新坐标显示（使用曲线上的一个点）
    idx = int((t % (2*np.pi)) / (2*np.pi) * 1000)
    if idx < 1000:
        coord_text.set_text(f'(x, y) = ({x[idx]:.3f}, {y_sin[idx]:.3f})')
    
    return line_sin, line_cos, timer_text, coord_text

# 创建动画
ani = animation.FuncAnimation(fig, animate, frames=500, interval=50, blit=True)

plt.show()


