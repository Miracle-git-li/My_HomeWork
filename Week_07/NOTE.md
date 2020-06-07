第七周 2020/6/7 学习笔记

这周学习的知识点比较多，是关于搜索算法的，废话不多说，直接上总结的知识点：
1、Trie树(前缀树)
· 基本结构：
    · Trie树，称为字典树，又称单词查找树或者键树， 是一种树形结构。典型应用是用于统计和排序大量的字符串(但不仅限于字符串)，所以经常被搜索引擎系统用于文本词频统计。
    · 他的优点是：最大限度地减少无畏地字符串比较，查询效率比哈希表高。
· 基本性质：
    1、节点本身不存在完整单词
    2、从根节点到某一节点，路径上经过的字符串连接起来，为该节点对应的字符串
    3、每个节点的所有子节点路径代表字符串都不相同
    · 节点存储额外信息： 比如该路径的单词所出现的频次
· 核心思想：
    Tire树等的核心思想是空间换书简
    利用字符串的公共前缀来来降低查询时间的开销以达到提高效率的目的
· 实现Trie树有需要注意的点： 一开始要初始一个字典和一个结尾字典， 即self.root = {} 、 self.end_of_word = "#"
· 相关题目： 单词搜索

2、 并查集
· 适用场景：
    组团、匹配问题
· 基本操作：
    · makeSet(s)    ：建立一个新的并查集，其中包含s个单元素集合
    · unionSet(x, y)：把元素x和元素y所在的集合合并， 要求x和y所在的集合不相交，如果相交则不合并
    · find(x)       ：找到元素x所在的集合的代表，该操作也可用于判断两个元素是否位于同一个集合， 只要将他们各自的代表(fater节点)比较一下就可以了。
· 并查集代码实现：
    def init(p):
        p = [i for i in range(n)]
    def union(self, p, i, j):
        p1 = self.parent(p, i)
        p2 = self.parent(p, j)
        p[p1] = p2
    def parent(self, p, i):
        root = i
        while p[root] != root:
            root = p[root]
        while p[i] != i:
            x = i
            i = p[i]
            p[x] = root
        return root
· 相关题目： 朋友圈

3、 双向BFS代码实现
    def BFS(graph, start, end):
        front = {start}
        back = {end}
        graph = set(graph)
        while front:
            new_set = {}
            process(front)
            front = new_set
            if len(front)> len(back): # 双向BFS与BFS 的区别
                front, back = back, front
· 双向BFD的相关题目： 单词接龙、 最小基因变化

4、 启发式搜索（Heuristic Search A*）
    A*基于BFS代码
    def AstarSearch(graph, start, end):
        pq = collection.priority_queue()  # 优先级->股价函数
        pq.append([start])
        visited.add(start)
        while pq:
            node = pq.pop(start)
            visited.add(node)
            process(node)
            nodes = generated_related_nodes(node)
            uncisited = [node for node in nodes if node not in visited]
            qp.push(unvisited)
· 估价函数： 
    又称启发式函数，h(n)， 他用来评价哪些节点最有希望是我们要找的节点， h(n)会返回一个非负实数，也可以认为是从节点n的目标节点路径的股价成本。
    启发式函数是一种告知搜索方向的方法， 他提供了一种明知的方法来猜测哪个邻居节点会导致一个目标。
· A*相关题目：二进制矩阵中的最短路径

5、高级树：AVL树和红黑树
· 遇到极端情况， 二叉树退化为链表
· 要保证性能的关键： 保证维度 -> 左右子树节点平衡
· 如何平衡？
    1> AVL树
        1. 发明者：G.M.Adelson-Velsky 和 Evhenii Landis
        2. Balence Factor(平衡因子)
           是他左子树的高度减去右子树的高度（有时相反）
           balance factor = {-1, 0, 1}
        3. 通过旋转操作来进行平衡(有四种旋转方法)
    · AVL总结
        1. 平衡二叉搜索树
        2. 每个节点存balance factor
        3. 四种旋转操作
    2> 红黑树（Red-black Tree）
        红黑树是一种近似平衡的二叉搜索树， 他能够确保任何一个节点的左右子树的高度差小于两倍。 具体而言，
        红黑树是满足以下条件的二叉搜素树：
        1. 每个根节点要么是红色， 要么是黑色
        2. 根节点是黑色
        3. 每个叶节点（NIL节点， 空节点）是黑色
        4. 不能有相邻接的两个红色节点
        5. 从任一节点到其每个叶子的所有路径都包含相同数目的黑色节点

