#Entry和Text组件
> Entry和Text组件都是可接收用户输入的输入框组件，区别是Entry是单行输入框组件，Text是多行输入框组件，而且Text
可以为不同的部分添加不同的格式，甚至响应事件。<br>

> 不管是Entry还是Text组件，程序都提供了get()方法来获取文本框中的内容;但如果程序要改变文本框中的内容，则需要
调用二者的insert()方法来实现。<br>

> 如果要删除Entry或者Text组件中的部分内容，则可通过delete(self,first,last=None)方法实现，该方法指定删除从
first到last之间的内容。<br>

> 关于Entry和Text支持的索引需要说明一下，由于Entry是单行文本框组件，因此它的索引很简单比如要指定第4个符到
第八个字符,索引指定为(3,8)即可。但Text是多行文本框组件，因此它的索引需要同时指定行号和列号，比如1.0代表第一
行、第一列(行号从1开始，列号从0开始),如果要指定第二行第三个字符到第三行第七个字符，索引应指为(2.2,3.6)。

> 此外，正如从前面程序所看到的，Entry支持双向绑定，程序可以将Entry与变量绑定在一起，这样程序就可以通过该
变量来改变、获取Entry组件中的内容。

