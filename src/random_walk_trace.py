import matplotlib.pyplot as plt
import numpy as np

def random_walk_2d(steps):
    """
    生成二维对角随机行走轨迹
    参数:
        steps (int): 行走步数
    返回:
        tuple: (x坐标数组, y坐标数组)
    """
    # 生成x和y方向的随机步长（-1或1）
    x_steps = np.random.choice([-1, 1], size=steps)
    y_steps = np.random.choice([-1, 1], size=steps)
    
    # 计算累积位置（从原点0开始）
    x_coords = np.cumsum(x_steps)
    y_coords = np.cumsum(y_steps)
    
    # 在数组开头插入起点(0,0)
    x_coords = np.insert(x_coords, 0, 0)
    y_coords = np.insert(y_coords, 0, 0)
    
    return x_coords, y_coords

def plot_single_walk(path):
    """
    绘制单条随机行走轨迹
    参数:
        path (tuple): 由random_walk_2d生成的坐标元组
    """
    x, y = path
    
    # 绘制轨迹线（蓝色细线）
    plt.plot(x, y, 'b-', linewidth=0.8, alpha=0.7)
    
    # 标记起点(绿色)和终点(红色)
    plt.scatter(x[0], y[0], c='lime', s=80, label=f'Start ({x[0]},{y[0]})')
    plt.scatter(x[-1], y[-1], c='red', s=80, label=f'End ({x[-1]},{y[-1]})')
    
    # 设置图形属性
    plt.axis('equal')  # 确保坐标轴比例相同
    plt.grid(True, linestyle='--', alpha=0.4)
    plt.title(f'2D Random Walk ({len(x)-1} steps)')
    plt.xlabel('X Position')
    plt.ylabel('Y Position')
    plt.legend(loc='best')
    plt.tight_layout()

def plot_multiple_walks():
    """在2x2网格中绘制四条独立随机行走轨迹"""
    # 创建画布和子图
    fig, axs = plt.subplots(2, 2, figsize=(10, 10))
    fig.suptitle('Comparison of 4 Random Walks (1000 steps each)', y=1.02)
    
    # 扁平化子图数组便于遍历
    axs = axs.ravel()
    
    for i in range(4):
        # 生成新轨迹
        x, y = random_walk_2d(1000)
        
        # 在当前子图绘制
        axs[i].plot(x, y, 'b-', linewidth=0.8, alpha=0.7)
        axs[i].scatter(x[0], y[0], c='lime', s=60)
        axs[i].scatter(x[-1], y[-1], c='red', s=60)
        
        # 设置子图属性
        axs[i].set_title(f'Trajectory {i+1}')
        axs[i].set_xlabel('X Position')
        axs[i].set_ylabel('Y Position')
        axs[i].axis('equal')
        axs[i].grid(True, linestyle='--', alpha=0.4)
    
    # 调整子图间距
    plt.tight_layout()

if __name__ == "__main__":
    # 任务1：单条轨迹可视化
    plt.figure(figsize=(8, 8))
    walk_path = random_walk_2d(1000)
    plot_single_walk(walk_path)
    plt.show()
    
    # 任务2：多条轨迹对比
    plot_multiple_walks()
    plt.show()
