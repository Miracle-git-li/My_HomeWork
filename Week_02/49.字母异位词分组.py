#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_dict = {}
        result_list = []
        # 把每个字符串分类
        for each_str in strs:
            # 排序字符串变成列表再转成字符串
            key = "".join(sorted(each_str))
            if key in result_dict.keys(): result_dict[key].append(each_str)
            else: result_dict[key] = [each_str]
        for key, value in result_dict.items():
            result_list.append(value)
        return result_list
  



# @lc code=end

