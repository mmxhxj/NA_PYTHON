#coding = utf - 8

#下面程序示范了文件指针操作
f = open ('filept_test.py','rb')
#判断文件指针的位置
print(f.tell()) # 0
#将文件指针移动到第
f.seek(3)                            #1代码
print(f.tell()) # 3
#读取 个字节，文件指针自动后移 个数据
print(f.read(1)) # o
print(f.tell()) # 4
#将文件指针移动到第
f.seek(5)                           #1代码
print(f.tell()) # 5
#将文件指针向后移动 个数据
f. seek (5,1)                       #1代码
print (f.tell() ) # 10
#将文件指针移动到倒数第 10
f.seek(-10,2)                       #1代码
print (f.tell())
print (f.read(1)) #d


'''
上面程序中粗体字代码示范了使用seek()方法来移动文件指针，包括从文件开头、 指针当前
置、文件结尾处开始计算。运行上面程序 结合程序输 出结果可以体会文件指针移动的效果
当文件指针位于哪里时， 程序就会读取哪个位置的数据：当程序读取多少个数据时， 文件指针就会自动向后移动多少个位置。
'''
