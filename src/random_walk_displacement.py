import numpy as np
import matplotlib.pyplot as plt

def random_walk_displacement(num_steps, num_simulations):
    """
    模拟随机行走并返回每次模拟的最终位移

    参数:
    num_steps (int): 随机行走的步数
    num_simulations (int): 模拟的次数

    返回:
    numpy.ndarray: 形状为(2, num_simulations)的数组，表示每次模拟的最终位移
    """
    # 检查输入参数的有效性
    if num_steps <= 0 or num_simulations <= 0:
        raise ValueError("num_steps and num_simulations must be positive integers")
    
    # 实现随机行走算法
    # 生成随机步长 ([-1, 1] 对于x和y方向)
    steps = np.random.choice([-1, 1], size=(2, num_simulations, num_steps))
    
    # 对步数维度求和得到最终位移
    final_displacements = np.sum(steps, axis=2)
    
    return final_displacements

def plot_displacement_distribution(final_displacements, bins=30):
    """
    绘制位移分布直方图

    参数:
    final_displacements (numpy.ndarray): 形状为(2, num_simulations)的数组，包含每次模拟的最终位移
    bins (int): 直方图的组数
    """
    # 计算每次模拟的最终位移大小
    x = final_displacements[0]
    y = final_displacements[1]
    r = np.sqrt(x**2 + y**2)
    
    # 绘制直方图
    plt.figure(figsize=(10, 6))
    plt.hist(r, bins=bins, density=True, alpha=0.7, edgecolor='black')
    plt.title('Final Displacement Distribution ({} steps, {} simulations)'.format(
        len(x), final_displacements.shape[1]))
    plt.xlabel('Displacement (r)')
    plt.ylabel('Probability Density')
    plt.grid(True)
    plt.show()

def plot_displacement_square_distribution(final_displacements, bins=30):
    """
    绘制位移平方分布直方图

    参数:
    final_displacements (numpy.ndarray): 形状为(2, num_simulations)的数组，包含每次模拟的最终位移
    bins (int): 直方图的组数
    """
    # 计算位移平方
    x = final_displacements[0]
    y = final_displacements[1]
    r_squared = x**2 + y**2
    
    # 创建包含三个子图的图形
    plt.figure(figsize=(18, 5))
    
    # 普通坐标
    plt.subplot(1, 3, 1)
    plt.hist(r_squared, bins=bins, density=True, alpha=0.7, edgecolor='black')
    plt.title('Displacement Squared Distribution')
    plt.xlabel('r²')
    plt.ylabel('Probability Density')
    plt.grid(True)
    
    # 半对数坐标
    plt.subplot(1, 3, 2)
    plt.hist(r_squared, bins=bins, density=True, alpha=0.7, edgecolor='black')
    plt.yscale('log')
    plt.title('Semi-log Plot')
    plt.xlabel('r²')
    plt.ylabel('Log Probability Density')
    plt.grid(True)
    
    # 对数坐标
    plt.subplot(1, 3, 3)
    plt.hist(r_squared, bins=np.logspace(np.log10(min(r_squared)), np.log10(max(r_squared)), bins), 
             density=True, alpha=0.7, edgecolor='black')
    plt.xscale('log')
    plt.yscale('log')
    plt.title('Log-log Plot')
    plt.xlabel('Log r²')
    plt.ylabel('Log Probability Density')
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # 可调整的参数
    num_steps = 1000  # 随机行走的步数
    num_simulations = 1000  # 模拟的次数
    bins = 30  # 直方图的组数

    # 完成主程序逻辑
    # 1. 调用random_walk_displacement获取模拟结果
    final_displacements = random_walk_displacement(num_steps, num_simulations)
    
    # 2. 绘制位移分布直方图
    plot_displacement_distribution(final_displacements, bins)
    
    # 3. 绘制位移平方分布直方图
    plot_displacement_square_distribution(final_displacements, bins)
