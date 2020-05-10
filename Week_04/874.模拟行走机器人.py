#
# @lc app=leetcode.cn id=874 lang=python3
#
# [874] 模拟行走机器人
#

# @lc code=start
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dx = [0,1,0,-1]
        dy = [1,0,-1,0]
        x = y = di = 0
        obstaclesSet = set(map(tuple,obstacles))
        ans = 0
        for cmd in commands:
            if cmd == -1:
                di = (di + 1) % 4
            elif cmd == -2:
                di = (di - 1) % 4
            else:
                for k in range(cmd):
                    if (x+dx[di], y+dy[di]) not in obstaclesSet:
                        x += dx[di]
                        y += dy[di]
                        ans = max(ans, x*x+y*y)
        return ans         
# @lc code=end

