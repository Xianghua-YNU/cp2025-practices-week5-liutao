import matplotlib.pyplot as plt
import numpy as np

def random_walk_2d(steps):
    """生成二维随机行走轨迹
    
    参数:
        steps (int): 随机行走的步数
        
    返回:
        tuple: 包含x和y坐标序列的元组 (x_coords, y_coords)
    """
    # 生成x和y方向的随机步长（-1或1）
    x_steps = np.random.choice([-1, 1], size=steps)
    y_steps = np.random.choice([-1, 1], size=steps)
    
    # 计算累积和得到轨迹坐标
    x_coords = np.cumsum(x_steps)
    y_coords = np.cumsum(y_steps)
    
    # 在坐标序列前插入起点(0,0)
    x_coords = np.insert(x_coords, 0, 0)
    y_coords = np.insert(y_coords, 0, 0)
    
    return x_coords, y_coords

def plot_single_walk(path):
    """绘制单个随机行走轨迹
    
    参数:
        path (tuple): 包含x和y坐标序列的元组
    """
    x_coords, y_coords = path
    
    # 绘制轨迹线
    plt.plot(x_coords, y_coords, 'b-', linewidth=0.5, label='Path')
    
    # 标记起点和终点
    plt.scatter(x_coords[0], y_coords[0], c='green', s=50, label='Start (0,0)')
    plt.scatter(x_coords[-1], y_coords[-1], c='red', s=50, label=f'End ({x_coords[-1]},{y_coords[-1]})')
    
    # 设置图形属性
    plt.axis('equal')
    plt.title(f'2D Random Walk ({len(x_coords)-1} steps)')
    plt.xlabel('X position')
    plt.ylabel('Y position')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend()
    plt.tight_layout()

def plot_multiple_walks():
    """在2x2子图中绘制四个不同的随机行走轨迹"""
    # 创建2x2的子图布局
    fig, axes = plt.subplots(2, 2, figsize=(10, 8))
    fig.suptitle('Four Different 2D Random Walks (1000 steps each)', y=1.02)
    
    for i, ax in enumerate(axes.flat):
        # 生成随机行走轨迹
        x_coords, y_coords = random_walk_2d(1000)
        
        # 绘制轨迹线
        ax.plot(x_coords, y_coords, linewidth=0.5)
        
        # 标记起点和终点
        ax.scatter(x_coords[0], y_coords[0], c='green', s=30)
        ax.scatter(x_coords[-1], y_coords[-1], c='red', s=30)
        
        # 设置子图属性
        ax.set_title(f'Walk {i+1}')
        ax.set_xlabel('X position')
        ax.set_ylabel('Y position')
        ax.axis('equal')
        ax.grid(True, linestyle='--', alpha=0.5)
    
    plt.tight_layout()

if __name__ == "__main__":
    # 生成并绘制单个轨迹
    plt.figure(figsize=(8, 6))
    path = random_walk_2d(1000)
    plot_single_walk(path)
    plt.show()
    
    # 生成并绘制多个轨迹
    plot_multiple_walks()
    plt.show()
