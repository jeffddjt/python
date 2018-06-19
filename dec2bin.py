#   109160903456刘紫瑄2018.6.19
#coding=utf-8

def dec2bin(string_num):
    num = int(string_num) #将输入的字符串类型的数值转换为整形
    la = []  #声明一个数组变量并初始化为空数组
    if num < 0:  #判断数值是否小于0
        return '-' + dec2bin(abs(num)) #如果小于0 则取该数值的绝对值进行转换
    while True:  #进入循环
        num, remainder = divmod(num, 2) # 将num对2取余数，并将商赋值给num,余数赋值给remainder
        la.append(str(remainder)) #将余数追加到数组la中
        if num == 0: #判断数值是否为0
            return ''.join(la[::-1]) #如果为0，说明已经除完，则将数组翻转并拼接成字符串输出；否则进行下一轮循环

type = sys.getfilesystemencoding()
dec = input('Input the numeric value to be converted:') #等待用户从控制台输入数值
bin = dec2bin(dec)  #调用函数将输入的十进制数据转换为二进制数据
print('The number is converted to binary:', bin) #显示提示信息及转换结果
