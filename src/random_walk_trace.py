# 导入必要的库
import matplotlib.pyplot as plt  # 用于绘图可视化
import numpy as np  # 用于数值计算和随机数生成

def random_walk_2d(steps):
    """生成二维随机游走轨迹
    参数:
        steps (int): 随机游走的步数
    返回:
        tuple: 包含x和y坐标序列的元组 (x_coords, y_coords)
    """
    # 在x和y方向分别生成随机步长（-1或1）
    x_step = np.random.choice([-1,1], steps)  # x方向随机步长
    y_step = np.random.choice([-1,1], steps)  # y方向随机步长
    
    # 计算累积和得到完整路径坐标
    return (x_step.cumsum(), y_step.cumsum())  # 返回x和y坐标数组
    

def plot_single_walk(path):
    """绘制单个随机游走轨迹
    参数:
        path (tuple): 包含x和y坐标数组的元组
    """
    # 解包获取x和y坐标
    x_coords, y_coords = path
    
    # 绘制路径线，每个步点用圆点标记
    plt.plot(x_coords, y_coords, marker='.')
    
    # 用绿色标记起点(大小100)，红色标记终点(大小100)
    plt.scatter([x_coords[0]], [y_coords[0]], color='green', s=100, label='起点')
    plt.scatter([x_coords[-1]], [y_coords[-1]], color='red', s=100, label='终点')
    
    # 设置坐标轴等比例显示
    plt.axis('equal')
    
    # 显示图例
    plt.legend()

def plot_multiple_walks():
    """在2x2子图中绘制四个不同的随机游走轨迹"""
    # 创建2行2列的子图，图像尺寸12x12英寸
    fig, axes = plt.subplots(2, 2, figsize=(12, 12))
    axes = axes.ravel()  # 将子图数组展平为一维便于遍历
    
    # 生成并绘制4条不同的随机游走轨迹
    for i in range(4):
        # 生成1000步的随机游走路径
        path = random_walk_2d(1000)
        x_coords, y_coords = path
        
        # 在当前子图绘制路径
        axes[i].plot(x_coords, y_coords, marker='.')
        
        # 标记起点和终点
        axes[i].scatter([x_coords[0]], [y_coords[0]], color='green', s=100, label='起点')
        axes[i].scatter([x_coords[-1]], [y_coords[-1]], color='red', s=100, label='终点')
        
        # 设置等比例坐标轴
        axes[i].axis('equal')
        
        # 添加图例和子图标题
        axes[i].legend()
        axes[i].set_title(f'轨迹 {i+1}')
    
    # 自动调整子图间距防止重叠
    plt.tight_layout()

if __name__ == "__main__":
    # 任务1：绘制单个随机游走轨迹
    plt.figure(figsize=(8, 8))  # 创建8x8英寸的画布
    path = random_walk_2d(1000)  # 生成1000步的随机游走
    plot_single_walk(path)  # 绘制轨迹
    plt.title('单个随机游走轨迹')  # 添加主标题
    plt.show()  # 显示图像
    
    # 任务2：绘制四个不同的随机游走轨迹
    plot_multiple_walks()  # 绘制2x2子图
    plt.show()  # 显示图像
