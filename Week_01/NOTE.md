# 解释方差：
期望值与真实值之间的波动程度，衡量的是**稳定性**

# 解释偏差：
期望值与真实值之间的一致差距，衡量的是**准确性**

# 模型训练为什么要引入偏差和方差？请理论论证。
优化监督学习=优化模型的泛化误差，模型的泛化误差可分解为偏差、方差与噪声之和
**Err = bias + var + irreducible error** 

以回归任务为例,其实更准确的公式为：**Err = bias^2 + var + irreducible error^2** 

符号的定义：一个真实的任务可以理解为Y=f(x)+e，其中f(x)为规律部分，e为噪声部分
- 训练数据D训练的模型称之为![](https://tva1.sinaimg.cn/large/006y8mN6gy1g8lwz21bi9j300y00pdfl.jpg)，当我们使用相同的算法，但使用不同的训练数据D时就会得到多个![](https://tva1.sinaimg.cn/large/006y8mN6gy1g8lwz21bi9j300y00pdfl.jpg)。则![](https://tva1.sinaimg.cn/large/006y8mN6gy1g8lwzqiav7j301q00pq2p.jpg)代表了这个模型的期望，即使用某一算法训练模型所能得到的稳定的平均水平。
- 方差：模型的稳定性：![](https://tva1.sinaimg.cn/large/006y8mN6gy1g8lx3a2qc3j306400ot8j.jpg)
- 偏差：模型的准确性：![](https://tva1.sinaimg.cn/large/006y8mN6gy1g8lx6rqg34j305g00odfn.jpg)
- Err(x) = Err(f,![](https://tva1.sinaimg.cn/large/006y8mN6gy1g8lx8dhkplj300e00m0s6.jpg))+Err(f,Y)
    - Err(f,![](https://tva1.sinaimg.cn/large/006y8mN6gy1g8lx8dhkplj300e00m0s6.jpg))为可解释规则误差
    - Err(f,Y) 为噪声e部分，即为![](https://tva1.sinaimg.cn/large/006y8mN6gy1g8lxc64l5yj300g00b0pn.jpg)
    - ![](https://tva1.sinaimg.cn/large/006y8mN6gy1g8lxyj2g67j301k00mmwx.jpg) 可推导如下：
        ![](https://tva1.sinaimg.cn/large/006y8mN6gy1g8lxkvx39gj30gh01b3yj.jpg)
    - f为真实值，固定；![](https://tva1.sinaimg.cn/large/006y8mN6gy1g8lwzqiav7j301q00pq2p.jpg)代表了这个模型不同数据预测结果的期望，固定；所以f-![](https://tva1.sinaimg.cn/large/006y8mN6gy1g8lwzqiav7j301q00pq2p.jpg)固定
    - ![](https://tva1.sinaimg.cn/large/006y8mN6gy1g8lxlzjp9hj305s00mt8j.jpg)中![](https://tva1.sinaimg.cn/large/006y8mN6gy1g8lxm8gzmrj301z00mq2p.jpg)为常数。所以![](https://tva1.sinaimg.cn/large/006y8mN6gy1g8lxlzjp9hj305s00mt8j.jpg)=![](https://tva1.sinaimg.cn/large/006y8mN6gy1g8lxo2v9ozj30bw00m0sn.jpg) = 0
    - Err(x) = ![](https://tva1.sinaimg.cn/large/006y8mN6gy1g8lxvudtfgj30cm00mjra.jpg)

# 什么情况下引发高方差？
- 过高复杂度的模型，对训练集进行过拟合
    - 带来的后果就是在训练集合上效果非常好，但是在校验集合上效果极差
    - 更加形象的理解就是用一条高次方程去拟合线性数据

# 如何解决高方差问题？
- 在模型复杂程度不变的情况下，增加更多数据
- 在数据量不变的情况下，减少特征维度
- 在数据和模型都不变的情况下，加入正则化

# 以上方法是否一定有效？
- 增加数据如果和原数据分布一致，无论增加多少必定解决不了高方差
    - smote对样本进行扩充是否必定可以避免高方差？
    - 过采样是否解决高方差问题？
- 减少的特征维度如果是共线性的维度，对原模型没有任何影响
    - 罗辑回归中，如果把一列特征重复2遍，会对最后的结果产生影响么？
- 正则化通常都是有效的

# 如何解决高偏差问题？
- 尝试获得更多的特征
    - 从数据入手，进行特征交叉，或者特征的embedding化
- 尝试增加多项式特征
    - 从模型入手，增加更多线性及非线性变化，提高模型的复杂度
- 尝试减少正则化程度λ

# 以上方法是否一定有效？
- 特征越稀疏，高方差的风险越高
- 多个线性变换=一个线性变换，多个非线性变换不一定=一个多线性变换
- 正则化通常都是有效的

# 遇到过的机器学习中的偏差与方差问题？
- 从偏差-方差分解的角度看，Bagging主要关注降低方差，因此它在不剪枝决策树，神经网络等易受样本扰动的学习器上效果更为明显。
- 从偏差-方差分解的角度看，Boosting主要关注降低偏差，因此Boosting能基于泛化性能相当弱的学习器构建出很强的集成。

# 就理论角度论证Bagging、Boosting的方差偏差问题
- 基础：
    - bagging和boosting都要n个模型，假设基模型权重![](https://tva1.sinaimg.cn/large/006y8mN6gy1g8lyh07lb3j300a00c0ok.jpg)，相关系数![](https://tva1.sinaimg.cn/large/006y8mN6gy1g8lyi3r97uj300900c0oe.jpg)，方差![](https://tva1.sinaimg.cn/large/006y8mN6gy1g8lzqhhkfwj300h00g0rq.jpg)均相等
    - Var(x,y) = Var(x) + Var(y) + 2Cov(x,y)
- Bagging
    - Var(F) = ![](https://tva1.sinaimg.cn/large/006y8mN6gy1g8lyk4wjxkj302v00qa9u.jpg)
            = ![](https://tva1.sinaimg.cn/large/006y8mN6gy1g8lyp35ynkj308l00qglh.jpg)
        - 其中
            - ![](https://tva1.sinaimg.cn/large/006y8mN6gy1g8lypqw1tjj300d00c0q9.jpg)可以直接提取出来
            - ![](https://tva1.sinaimg.cn/large/006y8mN6gy1g8lyuaep07j308v00ya9x.jpg)
        - 所以，化简以上的式子可得：Var(F) = m * ![](https://tva1.sinaimg.cn/large/006y8mN6gy1g8lyw59y9oj300h00g0rq.jpg) * ![](https://tva1.sinaimg.cn/large/006y8mN6gy1g8lywg4870j300g00k0r2.jpg) + ![](https://tva1.sinaimg.cn/large/006y8mN6gy1g8lyzygc4lj304300lgle.jpg)
        - 以上为通式，对于bagging来说，每个基模型的权重等于1/m且期望近似相等，所以![](https://tva1.sinaimg.cn/large/006y8mN6gy1g8lz1clt7wj301g011gld.jpg)，带入即可
        - Var(F) = ![](https://tva1.sinaimg.cn/large/006y8mN6gy1g8lz7qrpwsj304f015t8i.jpg)
        - E(F) = ![](https://tva1.sinaimg.cn/large/006y8mN6gy1g8lz97enuuj3059011743.jpg)
    - 结论：
        - 整体模型的期望近似于基模型的期望，这也就意味着整体模型的偏差和基模型的偏差近似
        - 整体模型的方差小于等于基模型的方差（当相关性为1时取等号），随着基模型数（m）的增多，整体模型的方差减少，从而防止过拟合的能力增强，模型的准确度得到提高
        - bagging的防止过拟合的极限在1/m项趋近于0，所以并不是可以无穷的降低方差达到提高模型准确性的效果的

- Boosting 同理
    - boosting的前提是弱模型之间高度相关，我们不妨设相关度为1
    - Var(F) = ![](https://tva1.sinaimg.cn/large/006y8mN6gy1g8lzwvy93dj302k00kmwx.jpg)
    - ![](https://tva1.sinaimg.cn/large/006y8mN6gy1g8lzj06hv1j304300qwea.jpg)
    - 结论：
        - 整体模型的期望近似于基模型的期望之和，模型越多期望越容易拟合真实值
        - 整体模型的方差等于基模型的数量平方成正比，越多模型不稳定性越高，越容易过拟合。
        - Gradient Boosting Decision Tree为典型例子
    
# 遇到过的深度学习中的偏差与方差问题？
神经网络的拟合能力非常强，因此它的训练误差（偏差）通常较小；
但是过强的拟合能力会导致较大的方差，使模型的测试误差（泛化误差）增大；
因此深度学习的核心工作之一就是研究如何降低模型的泛化误差，这类方法统称为正则化方法。
- dropout
- dense中的normalization
- 数据的shuffle

# 方差、偏差与模型的复杂度之间的关系？
![](https://tva1.sinaimg.cn/large/006y8mN6gy1g8ly6pdyouj30dn07eq38.jpg)


学习笔记: 2020-4-18
    我是初次学习算法与数据结构，之前也不是科班出身，在第一周初次接触算法与数据结构的学习的过程当遇到了不少的问题，我就以初学者在理解概念和做题时遇到问题如何解决这一角度来谈谈自己的感受。
    首先，在做题方面，因为刚接触写代码，之前一直认为编程写代码就是打一堆英文字母的缩写就完事， 但是真正接触了代码之后才发现其中的逻辑结构之严密，需要考虑到方方面面， 比如在做“盛最多水”这个题的时候，需要考虑到所有的假设空间，我一开始只是想到for循环来遍历每一根柱子所围成的面积，一开始的测试样例通过了，沾沾自喜地提交(submit)之后发现没有通过， 想了好久也不知道问题出现在哪，后来想到覃老师的话，我忽然意识到自己又陷入了之前做数学题的坏习惯“死磕”，然后看了题解之后才弄明白，使用while循环可以完整地遍历整个条形的情况。当然，小白学算法所遇到的困难不仅仅是做题没思路，就是在概念理解上也会觉得不知所云，这就是我接下来要讲的第二点。
    我在看视频课的时候发现并不是想象中零基础教授算法和数据结构的概念，老师讲的结构和逻辑都很清楚，但是做为一个一点基础也没有的我来说听第一遍的时候总是云里雾里，处于懵的状态，当然，我在这一点也做了应对措施，我讲讲我的应对经验。我先用1.25倍（老师建议1.5倍，我真的跟不上，手动狗头）的速度快速听一遍，尽可能地把自己听懂的总结出来，然后立马再看一遍，把老师讲的每一个要点都总结在本上，然后与第一遍总结的做对比，完善，第二天早上再看一遍笔记，理解，然后再看老师讲的内容就很有体会了。但是还是有很多基本知识点老师可能觉得太基本的没讲，然后从书中找到相应的章节看一遍，这样就能很好的理解本周所讲的内容了。
    总之，对于小白来学这个课的基本就是几个字，“用心，重复”，正如覃老师所讲的“过遍数”。刚开始学这个领域的只是，感觉到新奇，有意思，我想我能在这“70天”的刻意练习中收获多多，加油！

//查询和使用stack、queue和deque的接口
//stack和queue的背后是用一个数组来进行模拟， 在这个数组上加一些API来实现stack或者一个queue
1、使用列表作为栈stack
使用list方法可以讲列表作为栈，其中最后添加的元素是检索到的第一个元素（"先进后厨"）。要将项目添加到栈的顶部，使用append()。要从栈顶部检索元素，使用pop()
>>>stack = [3, 4, 5]
>>>stack.append(6)
stack = [3, 4, 5, 6]
>>>stack.pop()
6
stack = [3, 4, 5]
2、使用列表作为队列
也可以将列表用作队列，其中添加的第一个元素是检索到的第一个元素（“先进先出”）
>>>from collections import deque
>>>queue = deque(["a", "b", "c"])
>>>queue.append("d")
>>>queue.popleft()