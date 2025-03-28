import matplotlib.pyplot as plt
import numpy as np

def random_walk_2d(steps):
    """生成二维随机行走轨迹
    
    参数:
        steps (int): 随机行走的步数
        
    返回:
        tuple: 包含x和y坐标序列的元组 (x_coords, y_coords)
    """
    # 生成随机步长 ([-1, 1])
    x_steps = np.random.choice([-1, 1], size=steps)
    y_steps = np.random.choice([-1, 1], size=steps)
    
    return (x_coords, y_coords)

def plot_single_walk(path):
    """绘制单个随机行走轨迹
    
    参数:
        path (tuple): 包含x和y坐标序列的元组
    """
    x, y = path
    
    plt.figure(figsize=(8, 8))
    plt.plot(x, y, 'b-', alpha=0.7, linewidth=0.7, label='Path')
    plt.scatter(x[0], y[0], c='green', s=100, label='Start (0,0)')
    plt.scatter(x[-1], y[-1], c='red', s=100, label=f'End ({x[-1]},{y[-1]})')
    
    plt.axis('equal')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.title(f'2D Random Walk ({len(x)-1} steps)')
    plt.xlabel('X position')
    plt.ylabel('Y position')
    plt.legend()
    plt.show()

def plot_multiple_walks():
    """在2x2子图中绘制四个不同的随机行走轨迹"""
    plt.figure(figsize=(12, 12))
    
    for i in range(4):
        x, y = random_walk_2d(1000)
        ax = plt.subplot(2, 2, i+1)
        ax.plot(x, y, 'b-', alpha=0.7, linewidth=0.7)
        ax.scatter(x[0], y[0], c='green', s=50)
        ax.scatter(x[-1], y[-1], c='red', s=50)
        
        ax.set_title(f'Random Walk {i+1} (End: {x[-1]},{y[-1]})')
        ax.set_xlabel('X position')
        ax.set_ylabel('Y position')
        ax.axis('equal')
        ax.grid(True, linestyle='--', alpha=0.5)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # 1. 生成并绘制单个轨迹
    single_path = random_walk_2d(1000)
    plot_single_walk(single_path)
    
    # 2. 生成并绘制多个轨迹
    plot_multiple_walks()
    
