import numpy as np
import matplotlib.pyplot as plt

def generate_coin_sequence(n_flips, p_head=0.08):
    """生成硬币序列，1表示正面，0表示反面"""
    return np.random.choice([0, 1], size=n_flips, p=[1 - p_head, p_head])
    #这个函数模拟抛硬币实验，生成一个由0和1组成的随机序列。

def calculate_waiting_times(coin_sequence):
    """计算两次正面之间的等待时间（反面次数）"""
    positions = np.nonzero(coin_sequence == 1)[0]
    diffs = np.diff(positions)
    return diffs - 1
    #这个函数计算硬币序列中连续两次正面之间出现的反面次数。

def plot_waiting_time_histogram(waiting_times, log_scale=False, n_flips=None):
    """绘制等待时间直方图"""
    if len(waiting_times) == 0:
        print("No waiting times to plot.")
        return
    
    plt.figure()
    max_wt = np.max(waiting_times)
    bins = np.arange(0, max_wt + 2)
    plt.hist(waiting_times, bins=bins, align='left', rwidth=0.8, edgecolor='black')
    plt.xlabel('Waiting Time (number of tails)')
    plt.ylabel('Frequency')
    
    title = 'Waiting Time Distribution'
    if n_flips is not None:
        title += f' (n_flips={n_flips})'
    plt.title(title)
    
    if log_scale:
        plt.yscale('log')
    plt.xticks(np.arange(0, max_wt + 1))
    plt.show()
    #这个函数绘制等待时间的频率分布直方图，可选择使用对数坐标。
    
    stats = {
        "mean": np.mean(waiting_times) if len(waiting_times) > 0 else np.nan,
        "std": np.std(waiting_times) if len(waiting_times) > 0 else np.nan,
        "theoretical_mean": (1 - p) / p,
        "exponential_mean": 1 / p
    }
    return stats
    #这个函数计算等待时间的均值、标准差，并与理论值进行比较。
    
def run_experiment(n_flips, title):
    """分析等待时间的统计特性"""
    print(f"\n{title}")
    coin_seq = generate_coin_sequence(n_flips)
    waiting_times = calculate_waiting_times(coin_seq)
    stats = analyze_waiting_time(waiting_times)
    
    print(f"Experimental Mean: {stats['mean']:.2f}")
    print(f"Experimental Std: {stats['std']:.2f}")
    print(f"Theoretical Mean (Geometric): {stats['theoretical_mean']:.2f}")
    print(f"Theoretical Mean (Exponential): {stats['exponential_mean']:.2f}")
    
    plot_waiting_time_histogram(waiting_times, log_scale=False, n_flips=n_flips)
    plot_waiting_time_histogram(waiting_times, log_scale=True, n_flips=n_flips)
    return waiting_times, stats
    
def run_experiment(n_flips, title):
    """运行一次等待时间实验"""
    print(f"\n{title}")
    coin_seq = generate_coin_sequence(n_flips)
    waiting_times = calculate_waiting_times(coin_seq)
    stats = analyze_waiting_time(waiting_times)
    
    print(f"Experimental Mean: {stats['mean']:.2f}")
    print(f"Experimental Std: {stats['std']:.2f}")
    print(f"Theoretical Mean (Geometric): {stats['theoretical_mean']:.2f}")
    print(f"Theoretical Mean (Exponential): {stats['exponential_mean']:.2f}")
    
    plot_waiting_time_histogram(waiting_times, log_scale=False, n_flips=n_flips)
    plot_waiting_time_histogram(waiting_times, log_scale=True, n_flips=n_flips)
    return waiting_times, stats
    
    #这个函数执行完整的等待时间实验流程，包括生成序列、计算等待时间、
    分析统计特性和绘制直方图。

if __name__ == "__main__":
    # 设置随机种子以保证可重复性
    np.random.seed(42)
    
    # 任务一：1000次抛掷
    waiting_times_1k, stats_1k = run_experiment(1000, "Task 1: 1000 Coin Flips")
    
    # 任务二：1000000次抛掷
    print("\n")
    waiting_times_1m, stats_1m = run_experiment(1000000, "Task 2: 1,000,000 Coin Flips")
