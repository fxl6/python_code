"""
演示Python中的input语句
获取键盘的输入信息
"""

print("请告诉我你是谁？")
name = input()
print("我知道了，你是:%s" % name)

name = input("请告诉我你是谁？")
print("我知道了，你是: %s" % name)


# 输入数字类型
num = input("请告诉我你的银行卡密码：")
# 数据类型转换
num = int(num)
print("你的银行卡密码是：", type(num))


# input()语句功能是，获取键盘输入的数据
# 可以使用：input(提示信息)，用以在使用者输入内容之前显示提示信息
# 要注意，无论键盘输入什么类型的数据，获取到的数据永远都是字符串类型
