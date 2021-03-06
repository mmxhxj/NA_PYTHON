#需求
<pre>
实现一个简单的英语字典查询与管理程序，能快速查找单词。

一个英文单词包含单词与单词的注释，结构如下：
words = [{"word": "about", "note": "在附近，关于"},
         {"word": "post", "note": "邮寄、投递"}]
所有的单词组成一个列表，每个单词与注释成为一个字典，程序的功能就是管理这样一组单词记录，程序有查找单词、增加单词、更新注释、删除单词、显示单词等功能。

1、单词存储
数据使用全局变量words = []存储，它是一个列表，每个元素是一个字典，字典是单词与注释的信息。
例如：
words = [{"word": "about", "note": "在附近，关于"},
         {"word": "post", "note": "邮寄、投递"}]

2、单词查找
二分法查找是一种高效的查找方法，在words中查找单词w，主要思想如下：
(1) 设置i = 0, j = len(words)-1，即i、j是第一与最后一个下标；
(2) 如果i <= j就计算m = (i+j)//2，m是中间一个下标，如果i > j程序结束；
(3) 如果words[m]["word"] == w["word"]，那么说明words[m]就是要找的单词，m就是这个单词在列表中的位置；
(4) 如果words[m]["word"] > w["word"]，说明word[m]这个单词比要找的单词大，由于是从小到大排序的，因此设置j = m-1，构造[i, m-1]范围回到(2继续)查找；
(5) 如果words[m]["word"] < w["word"]，说明word[m]这个单词比要找的单词小，由于是从小到大排序的，因此设置i = m+1，构造[m+1, j]范围回到(2继续)查找；
(6) 如果全部查找完毕没有找到单词，那么这个单词是新的单词，它应该放在words[i]的位置。
</pre>
