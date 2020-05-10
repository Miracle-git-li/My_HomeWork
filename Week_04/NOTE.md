学习笔记
今天是2020年5月10号，很快，算法训练营的第四周已经结束，感觉每天徜徉在机器学习算法和基础的算法和数据结构中是一件非常有趣的事情，在计算机的世界里奇思妙想得以实现，想要汲取新知识的渴望不断膨胀。好了，废话不多说，下面就是这周所学到的关于算法的知识。

一、首先学习到了关于搜索的算法——深度优先搜索(DFS)和广度优先搜索(BFS)
    关于搜索，也即遍历有三点特性：1、每个节点都要访问一次 2、每个节点仅访问一次 3、对于节点的访问顺序不限也就引申出了DFS和BFS，当然还有按照优先级搜索
    对于深度优先搜索的代码：
1、递归写法
visited = set()
def dfs(node, visited):
    if node in visited: return
    visited.add(node)
    for next_node in node.children:
        if not next_node in visited:
            dfs(next_node, visited)
2、非递归写法
def dfs(self, tree):
    if tree.root is None:
        return []
    visited, stack = [], [tree.node]
    while stack:
        node = stack.pop()
        visited.add(node)
        process(node)
        nodes = generate_related_nodes(node)
        stack.push(nodea)
深度优先的非递归写法其实就是维护一个栈， 从栈中取出和加入要搜索的node。
对于广度优先搜索的代码：
def bfs(graph, start, end):
    queue = []
    queue.append([start])
    visited.add(start)
    while queue:
        node = queue.popleft()
        visited.add(node)
        process(node)
        nodes = generate_related_node(node)
        queue.push(nodes)
广度优先搜索就是维护一个队列， 从队列中加入，取出要搜索的node, 有时也用到双端队列deque

二、贪心算法 Greedy
    是一种（在每步中都采用当下状态最好或最优的选择， 从而希望导致结果是全局最好或最优）的算法。 
    一旦一个问题可以通过贪心来解决， 那么贪心法一般是解决这个问题的最好办法。由于贪心法的高效性以及其所求得的答案比较接近最优结果，贪心法也可以用作辅助算法或直接解决一些要求结果不特别精确的问题。

三、二分查找
    二分查找的前提:
    1、目标函数单调性（单调递增或单调递减）
    2、存在上下界
    3、能够通过索引访问
代码模板：
left, right = 0, len(array) - 1
while left <= right:
    mid = (left + right) // 2
    if array[mid] == target:
        break or return result
    elif array[mid] < target:
        left = mid + 1
    else:
        right = mid - 1


使用二分查找，寻找一个半有序数组 [4, 5, 6, 7, 0, 1, 2] 中间无序的地方
思路：
首先也是先定义一个左右边界， left, right = 0, len(array)-1 , 然后开始循环 while left<= right: （需要注意这里要有等号） 计算mid=(left+right)//2
先判断中间值与左右边界值的大小
当左边界array[left] 小于或等于中间值array[mid] 时， 说明中间值的左边是有序递增的数组，如果target在这个递增数组中，则可以将右边界设置right = mid-1
否则， target在中间值的右边数组， 则将左边界设置 left+1
当中间值小于右边界的值时， 说明中间值到右边界的数组是有序数组， 如果target在其中， 则设置左边界left = mid + 1 ,否则， 目标值在左边界到中间值的无序数组中，则设置右边界，right = mid - 1

半有序数组的二分查找与正常二分查找其实并没有太大区别， 仅仅是在第一层判断中， 不把中间值与目标值直接比较， 而是中间值与边界值先比较， 然后再与目标值进行比较。

