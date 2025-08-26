"""
有一排n栋房子，每栋房子都可以涂成三种颜色之一：红色、蓝色或绿色。将每栋房子涂成某种颜色的成本是不同的。您必须粉刷所有房屋，确保没有两个相邻房屋具有相同的颜色。
用某种颜色粉刷每栋房屋的成本由 n x 3 成本矩阵表示。例如，cost[0][0]是将0号房子涂成红色的成本； cost[1][2] 是将房屋 1 涂成绿色的成本，依此类推...求粉刷所有房屋的最小成本。
注意：
所有成本均为正整数。
示例：
输入：[[17,2,17],[16,16,5],[14,3,19]]
输出：10
解释：将房子 0 涂成蓝色，油漆将房子 1 涂成绿色，将房子 2 涂成蓝色。
最低成本：2 + 5 + 3 = 10。

shuru = [[17, 2, 17], [16, 16, 5], [14, 3, 19]]
"""


# 状态转移方程：f(n, i) = min(f(n-1, !i的两种颜色)) + cost(n, i)
def pintHose(costs):
    n = len(costs)
    # 滚动数组  两种状态  来回切换 并且设置边界条件

    # 定义dp
    dp = [[0, 0, 0], [0, 0, 0]]
    # 边界条件
    dp[0] = [costs[0], costs[1], costs[2]]
    # 真实索引从0开始
    for i in range(1, n):
        ind = i % 2
        pre_ind = not ind  # 取反可以跳转到先前状态的索引
        dp[ind][0] = min(dp[pre_ind][1], dp[pre_ind][2]) + costs[i][0]
        dp[ind][1] = min(dp[pre_ind][0], dp[pre_ind][2]) + costs[i][1]
        dp[ind][2] = min(dp[pre_ind][1], dp[pre_ind][0]) + costs[i][2]
    ind = (n - 1) % 2  # 最后一个房子的花费在哪种状态中

    return min(dp[ind])


def paintHouse(costs):
    """
    dp[i][c] 表示：粉刷到第 i 栋房子，且第 i 栋使用颜色 c（0=红,1=蓝,2=绿）时的最小总成本。
    转移：
      dp[i][红] = costs[i][红] + min(dp[i-1][蓝], dp[i-1][绿])
      dp[i][蓝] = costs[i][蓝] + min(dp[i-1][红], dp[i-1][绿])
      dp[i][绿] = costs[i][绿] + min(dp[i-1][红], dp[i-1][蓝])
    答案：min(dp[n-1][红], dp[n-1][蓝], dp[n-1][绿])
    """
    # 基本校验
    if not costs:
        return 0
    n = len(costs)
    for row in costs:
        if len(row) != 3:
            raise ValueError("每一行必须包含 3 个颜色的成本。")

    # 建立 dp 表，n 行 × 3 列
    dp = [[0] * 3 for _ in range(n)]

    # 初始化第 0 栋
    dp[0][0] = costs[0][0]  # 红
    dp[0][1] = costs[0][1]  # 蓝
    dp[0][2] = costs[0][2]  # 绿

    # 自底向上填表
    for i in range(1, n):
        dp[i][0] = costs[i][0] + min(dp[i - 1][1], dp[i - 1][2])  # 本房刷红
        dp[i][1] = costs[i][1] + min(dp[i - 1][0], dp[i - 1][2])  # 本房刷蓝
        dp[i][2] = costs[i][2] + min(dp[i - 1][0], dp[i - 1][1])  # 本房刷绿

    # 结果：最后一栋刷三种颜色的最小值
    return min(dp[n - 1][0], dp[n - 1][1], dp[n - 1][2])


# 也可以提供一个带路径恢复的版本，帮助理解选了哪些颜色
def paintHouse_with_path(costs: List[List[int]]):
    if not costs:
        return 0, []
    n = len(costs)
    for row in costs:
        if len(row) != 3:
            raise ValueError("每一行必须包含 3 个颜色的成本。")

    dp = [[0] * 3 for _ in range(n)]
    parent = [[-1] * 3 for _ in range(n)]  # 记录转移来源颜色

    dp[0] = costs[0][:]

    for i in range(1, n):
        for c in range(3):
            # 上一层可选的颜色（不等于 c）
            candidates = [(dp[i - 1][pc], pc) for pc in range(3) if pc != c]
            best_prev_cost, best_prev_color = min(candidates, key=lambda x: x[0])
            dp[i][c] = costs[i][c] + best_prev_cost
            parent[i][c] = best_prev_color

    # 收尾：找到最后一行的最优颜色
    last_color = min(range(3), key=lambda c: dp[n - 1][c])
    min_cost = dp[n - 1][last_color]

    # 回溯路径
    path = [0] * n
    path[n - 1] = last_color
    for i in range(n - 2, -1, -1):
        path[i] = parent[i + 1][path[i + 1]]

    color_names = ["红", "蓝", "绿"]
    path_colors = [color_names[c] for c in path]
    return min_cost, path_colors


if __name__ == "__main__":
    costs = [[17, 2, 17], [16, 16, 5], [14, 3, 19]]
    print("最小成本：", paintHouse(costs))  # 10
    cost, plan = paintHouse_with_path(costs)
    print("最小成本：", cost, "颜色方案：", plan)