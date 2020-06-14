第八周 学习笔记 2020/6/14
1、位运算
    1. 指定位置的位运算
        1> 将x最右边n位清零 ：  x & (~0 << n)
        2> 获取x的第n个位置值： (x >> n) & 1
        3> 获取x的第n位的幂 ：  x & (1 << n)
        4> 仅将第n位为0：       x & (~(1 << n))
        5> 仅将第n位为1：       x | (1 << n)
        6> 将x最高位至第n位清零：x & ((1 << n) - 1)
    2. 实战位运算要点：
        1> 判断奇偶：
            x % 2 == 1 --->  (x & 1) == 1  (奇数)
            x % 2 == 0 --->  (x & 1) == 0  (偶数)
        2> 取中位数索引
            x >> 1 ---> x / 2
            mid = (left + right) / 2   ---> mid = (left + right) >> 1
        3> 清零最低位的1：
            x = x & (x-1)
        4> 得到最低位的1
            x & -x     -x = ~x + 1 
            如果x是偶数， 则 x & ~x = x
2、 布隆过滤器和LRU缓存
    1. 布隆过滤器(Bloom Filter):
        一个很长的二进制向量和一系列随机映射函数。布隆过滤器可以用于检索一个元素是否存在一个集合中。
        优点是：空间效率和查询时间都远远超过一般算法
        缺点是：有一定的误识别率和删除困难
    python代码实现：
        from bitarray import bitarray
        import mmh3
        calss BloomFilter:
            def __init__(self, size, hash_num):
                self.size = size
                self.hash_num = hash_num
                self.bit_array = bitarray(size)
                self.bit_array.setall(0)
            def add(self, s):
                for seed in range(self.hash_num):
                    result = mmh3.hash(s, seed) % self.size
                    self.bit_array[result] = 1
            def lookup(self, s):
                for seed in range(self.hash_num):
                    result = mmh3.hash(s, seed) % self.size
                    if self.bit_array[result] == 0:
                        return "Nope"
                    return "Probly"
    2. LRU cache (leat recent use):
        两个要素：大小， 替换策略
        Hash Table  +  Double Linkedlist
        O(1)查询 、 O(1) 修改和更新
    python代码实现
        class LRUcache(Object):
            def __init__(self, capacity):
                self.dic = collections.OrderedDict()
                self.remain = capacity
            def get(self, key):
                if key not in self.dic:
                    return -1
                v = self.dic.pop(key)
                self.dic[key] = v
                return v
            def put(self, key, value):
                if key in self.dic:
                    self.dic.pop(key)
                else:
                    if self.remain > 0:
                        self.remain -= 1
                    else:
                        self.dic.popitem(last = False)
                self.dic[key] = value

3、 排序算法
    1. 比较类排序{交换排序(冒泡排序 、 快速排序)，插入排序(简单插入排序、 希尔排序)， 选择排序(简单选择排序、 堆排序)， 归并排序(归并排序) }
    2. 非比较类排序{基数排序， 桶排序， 计数排序}

4、 初级排序代码实现
    1.冒泡排序
        它重复走访要排序的数列， 一次比较两个元素，如果他们顺序错误就交换
        def bubbleSort(arr):
            for i in range(1, len(arr)):
                for j in range(0, len(arr)-i):
                    if arr[j] > arr[j+1]:
                        arr[j], arr[j+1] = arr[j+1], arr[j]
            return arr
    2.选择排序
        无论什么数据进去都是O(n**2)的时间复杂度， 所以用选择排序的时候， 数据规模越小越好，唯一的好处是不占用额外空间
        def selectionSort(arr):
            for i in range(len(arr)-1):
                minIndex = i
                for j in range(i+1, len(arr)):
                    if a[j] < arr[minIndex]:
                        minIndex =j
                if i != min Index:
                    arr[i], arr[minIndex] = arr[minIndex], arr[i]
            return arr
    3.插入排序
        从第1个元素开始，该元素认为已经被排序
        取出下一个元素，在已排序的元素序列中从后往前扫描
        如果该元素大于新元素， 该元素移动到下一位
        直到排序的元素小于或等于新元素
        将新元素插入到该位置
        def insertSort(arr):
            for i in range(len(arr)):
                preIndex = i-1
                current = arr[i]
                while preIndex >= 0 and arr[preIndex] > current:
                    arr[preIndex+1] = arr[preIndex]
                    preIndex -= 1
                arr[preIndex+1] = current
            return arr 
    

