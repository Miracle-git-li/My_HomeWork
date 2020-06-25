# 学习笔记  
经过在算法训练营的70天刻意练习， 我发现自己在对写代码这一块又有较大的提升，而且通过覃超老师的讲解，对于算法和数据结构的知识框架和体系也有了较为深刻的理解，主要是本不是科班出身，但是听完老师的课之后还是可以清晰的理解算法的运行技巧和数据结构的规则，感觉收获满满。
## 课程总结  
### 1、高级动态规划  
主要思路就是把问题抽象化， 定义状态， 马上套用模板， 写出嵌套循环， 把DP方程学下来。  
### 2、字符串算法
#### 1.字符串基础知识  
在python中， 字符串是不可变的(immutable) --> 优点：线程安全。  
#### 2.最长子序列  
动态转移方程：  
'''
dp[i][j] = dp[i-1][j-1]+1 if s1[i-1]==s2[i-1]
else dp[i][j] = max(dp[i-1],[j], dp[i][j-1])
'''
#### 3.最长字串  
动态转移方程：  
'''
dp[i][j] = dp[i-1][j-1]+1 if s1[i-1]=s2[j-1]
else dp[i][j] =0
'''  
### 3、字符串匹配算法  
#### 1.暴力法(brute force)  
'''
def forcw(txt, pat):
    n, m = len(txt), len(pat)
    for i in range(n-m-1):
        for j in range(m):
            if txt[i+j] != pat[j]:
                break
            if j == m:
                return i
    return -1
'''
#### 2.Rabin-karp 算法  
1>假设子串长度为M(pat), 目标字符串长度为N(txt)  
2>计算子串的hash值hash_pat  
3>计算目标字符串txt中每个长度为,的子串的hash值（共需要计算m-n+1次）  
4>比较hash值：如果hash值不同， 字符串必然不匹配， 如果hash值相同，还需要时使用朴素算法再次判断  
#### 3.KMP算法  
(knuth-Morris-pratt)的思想是：当字符串与目标字符串不匹配时，这时已经知道了前面匹配过的一部分字符串，设法利用这个已知信息，将目标字符串前缀对应上字符串后缀相同的位置。  
### 不同路径Ⅱ的动态转移方程  
'''
if 0 == i and 0 == j:
    dp[i][j] = 1
elif 0 == i and 0 != j:
    if 0 == obstacleGrid[i][j]:
        dp[i][j] = dp[i][j - 1]
elif 0 != i and 0 == j:
    if 0 == obstacleGrid[i][j]:
        dp[i][j] = dp[i - 1][j]
else:
    if 0 == obstacleGrid[i][j]:
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
'''


