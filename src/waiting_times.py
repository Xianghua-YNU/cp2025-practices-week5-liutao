import numpy as np
import matplotlib.pyplot as plt

def generate_coin_sequence(n_flips, p_head=0.08):
    """生成硬币序列，1表示正面，0表示反面"""
    return np.random.choice([0, 1], size=n_flips, p=[1 - p_head, p_head])

def calculate_waiting_times(coin_sequence):
    """计算两次正面之间的等待时间（反面次数）"""
    positions = np.nonzero(coin_sequence == 1)[0]
    diffs = np.diff(positions)
    return diffs - 1

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

def analyze_waiting_time(waiting_times):
    """分析等待时间的统计特性"""
    p = 0.08
    stats = {
        "mean": np.mean(waiting_times) if len(waiting_times) > 0 else np.nan,
        "std": np.std(waiting_times) if len(waiting_times) > 0 else np.nan,
        "theoretical_mean": (1 - p) / p,
        "exponential_mean": 1 / p
    }
    return stats

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

if __name__ == "__main__":
    np.random.seed(42)
    
    # 任务一：1000次抛掷
    waiting_times_1k, stats_1k = run_experiment(1000, "Task 1: 1000 Coin Flips")
    
    # 任务二：1000000次抛掷
    print("\n")
    waiting_times_1m, stats_1m = run_experiment(1000000, "Task 2: 1,000,000 Coin Flips")
    
    
    
