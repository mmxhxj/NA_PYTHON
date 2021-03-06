#coding = utf - 8

'''
Python既可使用文件对象的方法来读取文件，也可使用其他模块的函数来读取文件。

文件对象提供了read()方法来按字节或字符读取文件内容，到底是读取字节还是字符，则取决于
是否使用了b模式，如果使用了b模式，则每次读取一个字节;如果没有使用b模式，则每次读取一
个字符。在调用该方法时可传入一个整数作为参数，用于指定最多读取多少字节或字符。
'''

#下面程序采用循环读取文件的内容:
f = open("test.txt",'r',True)
while True:
    #每次读取一个字符
    ch = f.read(1)
    #如果没有读取到数据，则跳出循环
    if not ch:
        break
    #输出ch
    print(ch,end='')
f.close()

'''
上面程序采用循环依次读取每一个字符(因为程序没有使用b模式)，没读取到一个字符，程序就输出该字符。

正如上面程序所看到的，当程序读写完文件之后，推荐立即调用close()方法来关闭文件，这样可以避免资源泄漏。
'''
