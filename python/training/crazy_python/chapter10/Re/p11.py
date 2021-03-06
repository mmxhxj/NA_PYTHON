#coding = utf - 8

'''
创建正则表达式:
正则表达式就是一个用于匹配的模板，它可以匹配一批字符串，所有创建正则表达式就是创建一个特殊
的字符串。
'''

'''
正则表达式所支持的合法字符

字符                                 解释
x                                   字符x（x可以代表任意合法的字符）
\uhhhh                              十六进制值0xhhhh所表示的Unicode字符
\t                                  制标符('\u0009')
\n                                  新行(换行)符('\u000A')
\r                                  回车符('\u000D')
\f                                  换页符('\u000C')
\a                                  报警(bell)符('\u0007')
\c                                  Escape符('\u001B')
\cx                                 x对应的控制符。例如(,\cM匹配Ctrl+M。x值必须为A~Z或a~z之一)

除此之外，正则表达式中由一些特殊字符，这些特殊字符在正则表达式中有其特殊的用途，比如前面介绍的反斜线(\)
如果需要匹配这些特殊字符，就必须先将这些字符转义，也就是在前面添加一个反斜线(\)


=======================================================================================

正则表达式中的特殊字符

特殊字符                             说明
$                                   匹配一行的结尾。要匹配$符本身，使用\$
^                                   匹配一行的开头。要匹配^符本身，使用\^
()                                  标记子表达式（也就是组）的开始位置和结束位置。要匹配这些字符使用\(\)
[]                                  用于确定中括号表达式的开始位置和结束位置。要匹配这些字符使用\[\]
{}                                  用于标记前面子表达式的出现频度。要匹配这些字符使用\{\}
*                                   指定前面子表达式可以出现零次或多次。要匹配*字符本身，使用\*
+                                   指定前面子表达式可以出现一次或多次。要匹配+字符本身，使用\+
?                                   指定前面子表达式可以出现零次或一次。要匹配?字符本身，使用\?
.                                   匹配除换行符\n之外的任意单字符。要匹配.字符本身，使用\.
\                                   用于转义下一个字符，或指定八进制、十六进制字符。如果需匹配\字符，使用\\
|                                   指定在两项之间任选一项匹配。要匹配|字符本身，使用\|





>>> print(re.fullmatch(r'\u0041\\','A\\'))    #匹配A\          
<_sre.SRE_Match object; span=(0, 2), match='A\\'>
>>> print(re.fullmatch(r'\u0061\t','a\t'))    #匹配a<制表符>
<_sre.SRE_Match object; span=(0, 2), match='a\t'>
>>> print(re.fullmatch(r'\?\[','?['))         #匹配?[
<_sre.SRE_Match object; span=(0, 2), match='?['>


上面的正则表达式依然只能匹配单个字符，这是因为还未在正则表达式中使用通配符，通配符是可以匹配多个
字符的特殊字符。正则表达式中的通配符的功能远远超出了普通通配符的功能，它被成为"预定义字符"。



正则表达式所支持的预定以字符

预定义字符                            说明
.                                    默认可匹配所有除换行符之外的任意字符，在使用re.S或者re.DOTALL旗标之后，它还可以匹配换行符
\d                                   匹配(0~9的所有数字)
\D                                   匹配非数字
\s                                   匹配所有的空白符，包括空格、制表符、回车符、换页符、换行符等
\S                                   匹配所有的非空白字符
\w                                   匹配所有的单词字符，包括0~9的所有数字、26个英文字母和下画线(_)
\W                                   匹配所有的非单词字符


>>> re.fullmatch(r'c\wt','cat')     #c\wt可以匹配cat、cbt、cct、c0t、c9t等一批字符串
<_sre.SRE_Match object; span=(0, 3), match='cat'>
>>> re.fullmatch(r'c\wt','c9t')
<_sre.SRE_Match object; span=(0, 3), match='c9t'>

#匹配如000-000-0000形式的电话号码
>>> re.fullmatch(r'\d\d\d-\d\d\d-\d\d\d\d','123-456-8888')
<_sre.SRE_Match object; span=(0, 12), match='123-456-8888'>
'''